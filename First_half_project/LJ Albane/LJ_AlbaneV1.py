import numpy as np
from scipy.optimize import minimize

def lennard_jones_potential(r, epsilon):  #Calcul du potentiel de Lennard-Jones
    return 4.0 * epsilon * ((1 / r)**12 - (1 / r)**6)



