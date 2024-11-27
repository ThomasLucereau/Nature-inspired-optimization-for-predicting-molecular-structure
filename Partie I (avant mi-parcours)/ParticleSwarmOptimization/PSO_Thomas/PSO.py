import numpy as np
import Fonctions
import random as rd
from progressbar import Bar, ProgressBar

class Swarm:
    def __init__(self,nb_fonction,nb_particles,nb_coordinates_particle, max_iter = 1000):

        self.nb_fonction = nb_fonction - 1
        self.nb_particles = nb_particles
        self.f = Fonctions.functions[self.nb_fonction]
        self.domain = Fonctions.domaine[self.nb_fonction]
        self.particles = [Particle(self, np.random.uniform( -self.domain, self.domain,(nb_coordinates_particle,1)),np.random.uniform(-1, 1,(nb_coordinates_particle, 1)), i, self.f) for i in range(self.nb_particles)]
        self.global_best_position = None
        self.global_best_fitness = float('inf')
        self.max_iter = max_iter
        self.iter = 1


    def update_global_best(self):
        # Update global best position and fitness based on current swarm state
        for particle in self.particles:
            if particle.best_value < self.global_best_fitness:
                self.global_best_position = particle.best_position
                self.global_best_fitness = particle.best_value

    def update_particles(self):
        self.update_global_best()
        # Update positions and velocities of all particles in the swarm
        for particle in self.particles:
            particle.update_position_velocity()
            particle.update_best_position()


    def optimize(self):
        # Main optimization loop
        print("Optimisation ...")
        bar = ProgressBar(100, widgets=[Bar('=', '[', ']')])
        bar.start()
        progress = 0
        while self.iter < self.max_iter:
            self.update_particles()
            self.update_global_best()
            self.iter += 1
            if self.iter % (self.max_iter / 100) == 0:
                progress += 1
                bar.update(progress)
        bar.finish()

class Particle:

    weight = 0.2 # compris entre 0 et 1
    cognitive = 0.1
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

    def update_position_velocity(self):
        # Update position and velocity of the particle based on PSO equations
        r1, r2 = rd.random(), rd.random()
        self.velocity = self.weight*self.velocity + self.cognitive*r1*(self.best_position - self.position)  + self.social*r2*(self.swarm.global_best_position - self.position)
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


