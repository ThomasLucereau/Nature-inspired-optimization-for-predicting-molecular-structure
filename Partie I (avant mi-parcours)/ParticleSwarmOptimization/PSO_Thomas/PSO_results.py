import PSO



"""
Paramètres de l'optimisation
"""
nb_particles = 10000
nb_coordinates_particle = 2
max_iter = 1e3

nb_fonction = 5

"""
Plotting ...
"""

swarm = PSO.Swarm(nb_fonction,nb_particles,nb_coordinates_particle, max_iter)

swarm.optimize()

print("=========================Résultats==============================")

print(" --- Résultat optimisation --- ", swarm.global_best_position)
print(" --- Énergie associée --- ", swarm.global_best_fitness)

print("================================================================")
