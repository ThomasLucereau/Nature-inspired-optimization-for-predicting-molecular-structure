import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm

nb_particles = 1
nb_coordinates_particle = 2
recherche = 4.5
nb_search = 1000000000




x = np.linspace(-recherche, recherche, 30)
y = np.linspace(-recherche, recherche, 30)


def f(vector):
    return ((1.5-vector[0]+vector[0]*vector[1])**2
            + (2.25-vector[0]+vector[0]*vector[1]**2)**2 + (2.265-vector[0]+vector[0]*vector[1]**3)**2)


def random_search(function):
    zero = np.zeros((nb_coordinates_particle, nb_particles))
    return_value = zero
    for i in range(nb_search):
        value = np.random.uniform(-recherche, recherche, zero.shape)
        if function(value) < function(return_value):
            return_value = value
    return 'arg_min :', return_value, 'min :', function(return_value)


print(random_search(f))


