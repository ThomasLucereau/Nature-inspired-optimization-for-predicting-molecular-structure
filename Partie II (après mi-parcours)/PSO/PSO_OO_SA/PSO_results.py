import PSO_nv_tentative as PSO2
import PSO
import PSO_Parallel as PSOP


"""
Paramètres de l'optimisation
"""
nb_atoms = 3
nb_particles = 10 # moduler le nb de particules en fonction du nombre d'atomes
nb_coordinates_particle = 3
max_iter = 1e6

#Il faudrait mesurer l'efficacité du prgm en calculant la complexité du prgrm en O(particules,iter) et chronométrer pour avoir le nb d'opérations par sec

#influence des particules

#influence du temps de calcul (itérations)

"""
Plotting ...
"""

swarm = PSO.Swarm(nb_atoms,nb_particles,nb_coordinates_particle, max_iter)

swarm.optimize()

print("=========================Résultats==============================")

#print(" --- Résultat optimisation --- ", swarm.global_best_position)
print(" --- Énergie associée --- ", swarm.global_best_fitness)

print("================================================================")
