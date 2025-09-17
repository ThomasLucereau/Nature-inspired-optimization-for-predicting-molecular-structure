import numpy as np
import functions_for_alternative as Functions
import random as rd
from progressbar import Bar, ProgressBar


#Parameters

nb_atoms = 5
nb_particles = 6
nb_coordinates_particle = 3
max_iter = 1e5
best_energy = -9.103852

#Fonction de Lennard-Jones

f = Functions.Lennard_Jones_E

# Fixed variables

weight = 0.5  # compris entre 0 et 1
cognitive = 0.1
social = 0.9
domain = 1

#Common variables

particles = np.random.uniform( -domain, domain,(nb_particles, nb_coordinates_particle*nb_atoms))

best_energies = [f(particles[i]) for i in range(nb_particles)]
velocities = np.zeros((nb_particles, nb_coordinates_particle*nb_atoms))
best_positions = particles
global_best_position = None
global_best_energy = np.max(best_energies)

# Fonctions that'll be used later

def update_global_best():
    global global_best_energy
    global global_best_position

    global_best_energy = np.max(best_energies)
    i = best_energies.index(global_best_energy)
    global_best_position = particles[i]

def update_particle(i):
    r1, r2 = rd.random(), rd.random()
    velocities[i] = weight * velocities[i] + cognitive * r1 * (
                best_positions[i] - particles[i]) + social * r2 * (global_best_position - particles[i]) + np.random.uniform(-0.01, 0.01, size=(1,3*nb_atoms))  # bruit ajouté
    position = particles[i] + velocities[i]
    energy = f(position)
    if energy < best_energies[i]:
        best_energies[i] = energy
        best_positions[i] = position
def update_particles():
    for i in range(nb_particles):
        update_particle(i)
    update_global_best()

#Optimization :
print("Optimisation ...")



i=0

while abs(global_best_energy-best_energy) > 0.001:
    update_global_best()
    update_particles()
    i += 1
print(global_best_energy)
