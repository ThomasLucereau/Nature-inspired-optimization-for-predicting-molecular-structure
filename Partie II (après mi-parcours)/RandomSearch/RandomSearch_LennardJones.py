import numpy as np
import functions_for_alternative as Functions
import random as rd
from progressbar import Bar, ProgressBar

#Parameters

nb_atoms = 3
nb_coordinates_particle = 3
max_iter = 1e6


#Fonction de Lennard-Jones

f = Functions.Lennard_Jones_E

# Fixed variables
domain = 1

#Common variables

particle = np.random.uniform( -domain, domain,(1, nb_coordinates_particle*nb_atoms))[0]
print(particle)
best_energy = f(particle)
best_position = particle


# Fonctions that'll be used later


#Optimization :
print("Optimisation ...")

bar = ProgressBar(100, widgets=[Bar('=', '[', ']')])
bar.start()
progress = 0
i=0

while i < max_iter:
    particle = np.random.uniform(-domain, domain, (1, nb_coordinates_particle * nb_atoms))[0]
    if f(particle) < best_energy:
        best_energy = f(particle)
        best_position = particle
    i += 1
    if i % (max_iter / 100) == 0:
        progress += 1
        bar.update(progress)
bar.finish()

print(best_energy)

