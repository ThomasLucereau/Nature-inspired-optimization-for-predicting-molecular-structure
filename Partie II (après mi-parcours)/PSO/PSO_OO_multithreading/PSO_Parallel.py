import time
from joblib import Parallel, delayed
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
        self.global_best_position = None
        self.global_best_fitness = float('inf')
        self.particles = [Particle(self, np.random.uniform( -self.domain, self.domain,(nb_coordinates_particle*self.nb_atoms,1)),np.random.uniform(-1, 1,(nb_coordinates_particle*nb_atoms, 1)), i, self.f) for i in range(self.nb_particles)]


        self.max_iter = max_iter
        self.iter = 1



    def update_best(self,position,energy,nb_particle):
        # Update global best position and fitness based on current swarm state
        if energy < self.global_best_fitness:
            self.global_best_fitness = energy
            self.global_best_position = position
        self.best_position_particle[nb_particle] = position
        self.best_energy_particle[nb_particle] = energy

    def update_particle(self,particle):
        particle.update_particle()
    def update_particles(self):

        # Update positions and velocities of all particles in the swarm
        modified_instances = Parallel(n_jobs= 4)(delayed(self.update_particle)(particle) for particle in self.particles)


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

    weight = 0.5# compris entre 0 et 1
    cognitive = 0.9
    social = 0.1

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
        self.swarm.update_best(self.best_position,self.best_value,self.particle_nb)





    def update_position_velocity(self):
        # Update position and velocity of the particle based on PSO equations

        r1, r2 = rd.random(), rd.random()
        self.velocity = self.weight*self.velocity + self.cognitive*r1*(self.best_position - self.position)  + self.social*r2*(self.swarm.global_best_position - self.position) #ajouter du bruit
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
            self.swarm.best_energy_particle[self.particle_nb] = self.best_value
            self.swarm.best_position_particle[self.particle_nb] = self.best_position


    def update_particle(self):
        self.update_position_velocity()
        self.update_best_position()
        self.swarm.update_best(self.best_position,self.best_value,self.particle_nb)
