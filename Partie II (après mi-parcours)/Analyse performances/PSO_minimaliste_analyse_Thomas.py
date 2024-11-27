import numpy as np
import functions_for_alternative as Functions
import random as rd
from progressbar import Bar, ProgressBar
import matplotlib.pyplot as plt

#Parameters

nb_atoms = 5
max_iter = 1e3
min_energy = -9.103852
nombres_a_tester = [1,10,100,1000]
seuils = np.array([0]*len(nombres_a_tester))

for nb_particles in nombres_a_tester:

    energy_list = [0]*2*int(max_iter)
    for t in range (10):

        nb_coordinates_particle = 3

        #Fonction de Lennard-Jones

        f = Functions.Lennard_Jones_E

        # Fixed variables

        weight = 0.5  # compris entre 0 et 1
        cognitive = 0.1
        social = 0.9
        domain = 1

        fin_iter = int(max_iter)

        #Common variables
        i=0
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
            global energy_list
            global fin_iter
            global i

            global_best_energy = np.max(best_energies)
            index = best_energies.index(global_best_energy)
            global_best_position = particles[index]
            if global_best_energy > 0.6e6:
                energy_list[i] += 0.6e6
            else:
                energy_list[i] += global_best_energy
            if abs(global_best_energy - min_energy ) < 0.001 and i < fin_iter:
                fin_iter = i

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

        bar = ProgressBar(100, widgets=[Bar('=', '[', ']')])
        bar.start()
        progress = 0


        while i < max_iter:
            update_global_best()
            update_particles()
            i += 1
            if i % (max_iter / 100) == 0:
                progress += 1
                bar.update(progress)
        bar.finish()
        seuils[nombres_a_tester.index(nb_particles)] += fin_iter

    energy_list = np.array(energy_list)/10

    x = np.linspace(1,2*int(max_iter), 2*int(max_iter))
    plt.plot(x,energy_list, label = 'nb_particles = '+ str(nb_particles))


zero = [0]*int(max_iter)*2
x = np.linspace(1,2*int(max_iter), 2*int(max_iter))
plt.plot(x,zero, '--')
plt.title('vitesse de convergence en fonction du nb de particules pour ' + str(nb_atoms) + ' atomes')
plt.semilogx()
plt.legend()
plt.savefig('tracé énergie')

print(seuils/10)

