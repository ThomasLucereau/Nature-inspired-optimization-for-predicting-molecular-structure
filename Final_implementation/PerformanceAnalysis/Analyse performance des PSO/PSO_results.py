
import PSO



"""
Paramètres de l'optimisation
"""
nb_atoms = 5
nb_particles = 6 # moduler le nb de particules en fonction du nombre d'atomes
nb_coordinates_particle = 3
max_iter = 1e6
best_energy = -9.103852

#Il faudrait mesurer l'efficacité du prgm en calculant la complexité du prgrm en O(particules,iter) et chronométrer pour avoir le nb d'opérations par sec

#influence des particules

#influence du temps de calcul (itérations)

"""
Plotting ...
"""

swarm = PSO.Swarm(nb_atoms,nb_particles,nb_coordinates_particle,best_energy, max_iter)

swarm.optimize()

print("=========================Résultats==============================")

#print(" --- Résultat optimisation --- ", swarm.global_best_position)
print(" --- Énergie associée --- ", swarm.global_best_fitness)

print("================================================================")
