import Sa_N_dimensions as SA
import plot_solution as plot
import numpy as np
import LennardJones_Final as LJf

"""
Paramètres de l'optimisation
"""
nb_particles = 5


nb_coordinates_particle = 3
temperature_initiale = 1e25
temperature_finale = 0.001
nb_iter = 1e7



"""
Plotting ...
"""



sa_LJ = SA.SimulatedAnnealing(temperature_initiale, temperature_finale, nb_iter,nb_coordinates_particle,nb_particles)
sa_LJ.anneal()


print("=========================Résultats==============================")
print(" --- Position initiale --- ",sa_LJ.initial_x)
print(" --- Energie initiale --- ", sa_LJ.initial_E)
print(" --- Résultat optimisation --- ", sa_LJ.best_x)
print(" --- Énergie associée --- ", sa_LJ.best_E)
print(sa_LJ.saut)
print(sa_LJ.temp)
LJf.plot_evolution_energy(sa_LJ)
plot.visu_polyhedron(sa_LJ,list(sa_LJ.best_x))

"""
def analyse(debut=3,fin=100):
    L=[]
    for i in range(debut,fin+1):
        sa = SA.SimulatedAnnealing(temperature_initiale, temperature_finale, nb_iter, nb_coordinates_particle,
                                    i)
        sa.anneal()
        L.append(sa.best_E)

    return L

#print(analyse(3,15))
"""