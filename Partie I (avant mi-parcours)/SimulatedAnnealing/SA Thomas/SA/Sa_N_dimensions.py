import numpy as np
import random as rd
import LennardJones_Final as LJt
from progressbar import ProgressBar, Bar




class SimulatedAnnealing:
    def __init__(self, temp, temp_final, fin_iter,nb_coordinates_particle,nb_atoms):

        self.temp_initial = temp
        self.temp = temp
        self.temp_final = temp_final
        self.fin_iter = fin_iter
        self.nb_atoms = nb_atoms
        self.domain = 0.7
        self.f = LJt.Lennard_Jones_E
        self.iter = 1
        self.nb_coordinates_particle = nb_coordinates_particle

        self.initial_x = np.random.uniform( -self.domain, self.domain, (self.nb_atoms*self.nb_coordinates_particle,1))
        self.initial_E = self.f(self.initial_x, self.nb_atoms)
        self.curr_x = self.initial_x
        self.curr_E = self.initial_E

        self.best_x = self.initial_x
        self.best_E = self.initial_E

        self.x_hist = [self.curr_x]
        self.E_hist = [self.curr_E]
        self.temp_hist = [self.temp]
        self.saut = 0

    def acceptance_probability(self, new_E):
        return np.exp(-(new_E - self.curr_E)/self.temp)

    def cooling_schedule(self):
        if self.iter < 5e6:
            self.temp = self.temp_initial
        else:
            self.temp = self.temp_initial * np.exp(-1e-5*self.iter)

        return

    def acceptance_function(self, new_x):

        new_E = self.f(new_x, self.nb_atoms)

        if new_E < self.curr_E:
            self.curr_E = new_E
            self.curr_x = new_x
            if new_E < self.best_E:
                self.best_E = new_E
                self.best_x = new_x
                self.gradient_descent_2d()

        else:
            proba = rd.random()
            if proba < self.acceptance_probability(new_E):
                self.curr_E = new_E
                self.curr_x = new_x
                self.saut += 1
        self.x_hist.append(self.curr_x)
        self.E_hist.append(self.curr_E)


    def modifier(self):
        alea = 1e-4
        new_x = np.random.uniform(-alea, alea, (self.nb_atoms*self.nb_coordinates_particle, 1)) + self.curr_x
        return new_x

    def gradient_descent_2d(self):

        learning_rate = 0.001
        tolerance_ini = 1e-6

        tolerance = LJt.tolerance(self,tolerance_ini)
        evaluation = np.inf
        while tolerance < evaluation:
            grad = LJt.LJ_grad(self.curr_x)
            grad = np.array(grad)

            evaluation = np.min([np.abs(dfdx) for dfdx in grad])

            self.curr_x -= learning_rate * grad

        self.curr_E = self.f(self.curr_x,self.nb_atoms)
        self.x_hist.append(self.curr_x)
        self.E_hist.append(self.curr_E)

        if self.curr_E < self.best_E:
            self.best_E = self.curr_E
            self.best_x = self.curr_x
        return


    def anneal(self):
        print("Optimisation ...")
        bar = ProgressBar(100, widgets=[Bar('=', '[', ']')])
        bar.start()
        progress = 0

        while self.iter < self.fin_iter:

            new_x = self.modifier()
            self.acceptance_function(new_x)

            taille = np.max(self.curr_x)

            if taille > self.domain :
                self.domain = taille


            self.x_hist.append(self.curr_x)
            self.E_hist.append(self.curr_E)
            self.temp_hist.append(self.temp)

            self.cooling_schedule()
            self.iter += 1


            if self.iter % (self.fin_iter/100) == 0:
                progress += 1
                bar.update(progress)

        bar.finish()






















