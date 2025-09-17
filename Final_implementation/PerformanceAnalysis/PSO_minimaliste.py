import numpy as np
import functions_for_alternative as Functions
import random as rd
from progressbar import Bar, ProgressBar
import time
import matplotlib.pyplot as plt


def test(nb_atoms : int,nb_particles : int):

    # Fonctions that'll be used later

    def update_global_best():
        global global_best_energy
        global global_best_position
        global_best_energy = np.max(best_energies)
        i = best_energies.index(global_best_energy)
        global_best_position = particles[i]

    def update_particle(i):
        global global_best_position
        r1, r2 = rd.random(), rd.random()
        velocities[i] = weight * velocities[i] + cognitive * r1 * (best_positions[i] - particles[i]) + social * r2 * (global_best_position - particles[i]) + np.random.uniform(-0.01, 0.01, size=(1,3*nb_atoms))  # bruit ajouté
        position = particles[i] + velocities[i]
        energy = f(position)
        if energy < best_energies[i]:
            best_energies[i] = energy
            best_positions[i] = position
    def update_particles():
        for i in range(nb_particles):
            update_particle(i)
        update_global_best()

    #Parameters
    start_time = time.time()
    t = 0
    nb_coordinates_particle = 3
    max_time = 120


    #Fonction de Lennard-Jones
    f = Functions.Lennard_Jones_E

    # Fixed variables
    weight = 0.5  # compris entre 0 et 1
    cognitive = 0.5
    social = cognitive - 1
    domain = 1

    #Common variables
    particles = np.random.uniform( -domain, domain,(nb_particles, nb_coordinates_particle*nb_atoms))
    best_energies = [f(particles[i]) for i in range(nb_particles)]
    velocities = np.zeros((nb_particles, nb_coordinates_particle*nb_atoms))
    best_positions = particles
    global_best_position = None

    #Optimization :
    print("Optimisation ...")

    while t < max_time:
        update_global_best()
        update_particles()
        t = time.time() - start_time

    return(np.max(best_energies))

def set_test():
    set_particules = [4,5,6,7,8,9,10,11, 12, 13]
    Y = []
    for part in set_particules:
        resultat = abs (-3 - test(5,part))
        print("Pour", part, "particules :", resultat)
        Y.append(resultat)
    plt.plot(set_particules,Y)
    plt.show()

set_test()
