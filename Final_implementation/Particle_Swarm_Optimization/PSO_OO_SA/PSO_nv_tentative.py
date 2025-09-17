import time

import numpy as np
import Fonctions
import random as rd
from progressbar import Bar, ProgressBar

class Swarm:
    def __init__(self,nb_atoms,nb_particles,nb_coordinates_particle, max_iter = 1000):

        self.nb_atoms = nb_atoms
        self.nb_particles = nb_particles
        self.f = Fonctions.Lennard_Jones_E
        self.domain = 1
        self.best_position_particle = dict()
        self.best_energy_particle = dict()
        self.global_best_position = np.random.uniform( -self.domain, self.domain,(nb_coordinates_particle*self.nb_atoms,1))
        self.global_best_fitness = self.f(self.global_best_position)
        self.particles = [Particle(self, np.random.uniform( -self.domain, self.domain,(nb_coordinates_particle*self.nb_atoms,1)),np.eye(nb_coordinates_particle*nb_atoms, 1), i, self.f) for i in range(self.nb_particles)]


        self.max_iter = max_iter
        self.iter = 1



    def update_best(self,position,energy,nb_particle):
        # Update global best position and fitness based on current swarm state
        if energy < self.global_best_fitness:
            self.global_best_fitness = energy
            self.global_best_position = position
        self.best_position_particle[nb_particle] = position
        self.best_energy_particle[nb_particle] = energy


    def update_particles(self):

        # Update positions and velocities of all particles in the swarm
        for particle in self.particles:
            particle.update_particle()


    def optimize(self):
        # Main optimization loop
        print("Optimisation ...")
        bar = ProgressBar(100, widgets=[Bar('=', '[', ']')])
        bar.start()
        progress = 0
        #self.start_particle()
        while self.iter < self.max_iter:
            self.update_particles()
            self.iter += 1
            if self.iter % (self.max_iter / 100) == 0:
                progress += 1
                bar.update(progress)
        bar.finish()


class Particle:

    weight = 0.2# compris entre 0 et 1
    cognitive = 0.5
    social = 1

    def __init__(self, swarm, position, velocity, particle_number, f):

        self.swarm = swarm
        self.particle_nb = particle_number
        self.position = position
        self.velocity = velocity
        self.best_position = position
        self.f = f
        self.value = self.f(position)
        self.best_value = self.f(self.best_position)
        self.run = 0
        self.swarm.best_energy_particle[self.particle_nb] = self.best_value
        self.swarm.best_position_particle[self.particle_nb] = self.best_position



    def update_position_velocity(self):
        # Update position and velocity of the particle based on PSO equations
        r1, r2 = rd.random(), rd.random()
        sa = SimulatedAnnealing(1e3, 0.001, 1e2,3,self.swarm.nb_atoms,self)
        ideal_position = sa.anneal()
        self.velocity = self.weight * self.velocity + self.cognitive*r1*(ideal_position - self.position) + self.social*r2*(self.swarm.global_best_position - self.position)
        self.position = self.position + self.velocity



    def evaluate_fitness(self):
        # Evaluate fitness of the particle based on the objective function
        self.value = self.f(self.position)


    def update_best_position(self):
        self.evaluate_fitness()
        # Update personal best position if current position is better
        if self.best_value < self.value:
            self.best_position = self.position
            self.best_value = self.value
            self.swarm.update_best(self.best_position, self.best_value, self.particle_nb)


    def update_particle(self):
        self.update_position_velocity()
        self.update_best_position()
        self.swarm.update_best(self.best_position,self.best_value,self.particle_nb)



class SimulatedAnnealing:
    def __init__(self, temp, temp_final, fin_iter,nb_coordinates_particle,nb_atoms,particle):

        self.temp_initial = temp
        self.particle = particle
        self.temp = temp
        self.temp_final = temp_final
        self.fin_iter = fin_iter
        self.nb_atoms = nb_atoms
        self.domain = 0.7
        self.f = Fonctions.Lennard_Jones_E
        self.iter = 1
        self.nb_coordinates_particle = nb_coordinates_particle

        self.initial_x = self.particle.position
        self.initial_E = self.f(self.initial_x)
        self.curr_x = self.initial_x
        self.curr_E = self.initial_E

        self.best_x = self.initial_x
        self.best_E = self.initial_E


    def acceptance_probability(self, new_E):
        return np.exp(-(new_E - self.curr_E)/self.temp)

    def cooling_schedule(self):
        if self.iter < 5e6:
            self.temp = self.temp_initial
        else:
            self.temp = self.temp_initial * np.exp(-1e-5*self.iter)

        return

    def acceptance_function(self, new_x):

        new_E = self.f(new_x)

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


    def modifier(self):
        alea = 1e-4
        new_x = np.random.uniform(-alea, alea, (self.nb_atoms*self.nb_coordinates_particle, 1)) + self.curr_x
        return new_x

    def gradient_descent_2d(self):

        learning_rate = 0.001
        tolerance_ini = 1e-6

        tolerance = Fonctions.tolerance(self,tolerance_ini)
        evaluation = np.inf
        while tolerance < evaluation:
            grad = Fonctions.LJ_grad(self.curr_x)
            grad = np.array(grad)

            evaluation = np.min([np.abs(dfdx) for dfdx in grad])

            self.curr_x -= learning_rate * grad

        self.curr_E = self.f(self.curr_x)

        if self.curr_E < self.best_E:
            self.best_E = self.curr_E
            self.best_x = self.curr_x
        return


    def anneal(self):

        progress = 0

        while self.iter < self.fin_iter:

            new_x = self.modifier()
            self.acceptance_function(new_x)

            taille = np.max(self.curr_x)

            if taille > self.domain :
                self.domain = taille

            self.cooling_schedule()
            self.iter += 1

            if self.iter % (self.fin_iter/100) == 0:
                progress += 1
        return self.best_x

