import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from progressbar import ProgressBar, Bar
from matplotlib import cm


"====================================Implémentation des fonctions================================================="

def f1(vector):
    """
    Fonction de Beale
    min : (3,0.5)
    """
    return ((1.5-vector[0]+vector[0]*vector[1])**2
            + (2.25-vector[0]+vector[0]*vector[1]**2)**2 + (2.625-vector[0]+vector[0]*vector[1]**3)**2)
def f2(vector):
    """
    Fonction de Rastrigin
    min : (0,0)
    """
    return 20 + (vector[0]**2 - 10*np.cos(2*np.pi*vector[0])) + (vector[1]**2 - 10*np.cos(2*np.pi*vector[1]))

def f3(vector):
    """
    Fonction de quadratique
    min : (0,0)
    """
    return vector[0]**2 + vector[1]**2

def f4(vector):
    """
    Fonction de Ackley
    min : (0,0)
    """
    return -20 * np.exp(-0.2*np.sqrt(0.5*(vector[0]**2 + vector[1]**2))) - np.exp(0.5*(np.cos(2*np.pi*vector[0])+ np.cos(2*np.pi*vector[1]))) + np.exp(1) + 20

def f5(vector):
    """
    Fonction de Rosenbrock
    min : (1,1)
    """
    return 100*(vector[1]-vector[0]**2)**2 + (1-vector[0])**2

def f6 (vector):
    a,b = vector[0],vector[1]
    return (a-3.14)**2 - (b-2.72)**2 + np.sin(3*a + 1.41) + np.sin(4*b-1.73)


x, y = sp.symbols('x y')

expr1 = ((1.5-x+x*y)**2 + (2.25-x+x*y**2)**2 + (2.625-x+x*y**3)**2)
expr2 = 20 + (x**2 - 10*sp.cos(2*sp.pi*x)) + (y**2 - 10*sp.cos(2*sp.pi*y))
expr3 = x**2 + y**2
expr4 = -20 * sp.exp(-0.2*sp.sqrt(0.5*(x**2 + y**2))) - sp.exp(0.5*(sp.cos(2*sp.pi*x)+ sp.cos(2*sp.pi*y))) + sp.exp(1) + 20
expr5 = 100*(y-x**2)**2 + (1-y)**2
expr6 = (x-3.14)**2 - (y-2.72)**2 + sp.sin(3*x + 1.41) + sp.sin(4*y-1.73)


functions = [f1, f2 , f3, f4, f5,f6] #liste des fonctions qu'on voudrait tester
domaine = [4.5, 5.12, 5, 5, 3, 5] #Liste de leurs domaines de définition
expr = [expr1, expr2, expr3, expr4,expr5, expr6]


"============================================================================================================="













"=================================================== Fonctions de Plotting ==================================="
