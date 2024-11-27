import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import numba as nb
import math
"====================================Implémentation des fonctions================================================="

@nb.njit()
def distance (molecule,i,j) -> float:
    a = ((molecule[3*i][0]-molecule[3*j][0])**2+(molecule[3*i+1][0]-molecule[3*j+1][0])**2+(molecule[3*i+2][0]-molecule[3*j+2][0])**2)**(1/2)
    return a

@nb.njit()
def Lennard_Jones_E(molecule: nb.types.float64[:, :]) -> float:
    taille = len(molecule)/3
    somme = 0.0
    beta = 0.0
    for i in range(int(taille)):
        for j in range(i):
            dist = distance(molecule,i,j)
            beta = 1/(dist)**6
            somme = somme + (beta**2 - beta)
    return 4*somme

@nb.njit()
def df_dx(a,b,c,d,e,f) -> nb.float64:
    if a==b:
        return 4*((-24*a + 24*d)**(1/13)/((a - d)**2 + (b - e)**2 + (c - f)**2))**13 - 4*((-12*a + 12*d)**(1/7)/((a - d)**2 + (b - e)**2 + (c - f)**2))**(7)
    return 0
@nb.njit()
def LJ_grad(molecule):
    taille = len(molecule)

    gradient = []

    for i in range(taille):
        df_dx_i = 0.0

        if i % 3 == 0:
            #print(i,'0')
            for j in range(1,int(i/3)):
                df_dx_i = df_dx_i + df_dx(molecule[i][0],molecule[i+1][0],molecule[i+2][0],molecule[3*j][0], molecule[3*j+1][0], molecule[3*j+2][0])
            for z in range(int(i/3),int(taille/3)):
                df_dx_i = df_dx_i + df_dx(molecule[i][0], molecule[i + 1][0], molecule[i + 2][0], molecule[3 * z][0],molecule[3 * z + 1][0], molecule[3 * z + 2][0])

        if i % 3 == 1:
            #print(i,'1')
            for j in range(int(i / 3)):
                df_dx_i = df_dx_i + df_dx(molecule[i-1][0], molecule[i][0], molecule[i + 1][0], molecule[3 * j][0], molecule[3 * j + 1][0],
                                          molecule[3 * j + 2][0])
            for z in range(int(i / 3), int(taille / 3)):
                df_dx_i =df_dx_i + df_dx(molecule[i - 1][0], molecule[i][0], molecule[i + 1][0], molecule[3 + z][0],
                                         molecule[3 * z + 1][0], molecule[3 * z + 2][0])

        if i % 3 == 2:
            #print(i,'2')
            for j in range(int((i-2) / 3)):
                df_dx_i = df_dx_i + df_dx(molecule[i-2][0], molecule[i-1][0], molecule[i][0], molecule[3 * j][0], molecule[3 * j + 1][0],
                                          molecule[3 * j + 2][0])
            for z in range(int((i-2) / 3), int(taille / 3)):
                df_dx_i = df_dx_i + df_dx(molecule[i - 2][0], molecule[i - 1][0], molecule[i][0], molecule[3 + z][0],
                                          molecule[3 * z + 1][0], molecule[3 * z + 2][0])

        gradient.append([df_dx_i])

    return gradient






"============================================== Améliorations ==============================================================="

def tolerance(swarm,tolerance_initiale):
    result = 1/(swarm.iter)**4
    if swarm.iter == 1 or result > tolerance_initiale:
        return tolerance_initiale
    return result



def plot_evolution_energy(sa):
    x = np.linspace(1, int(sa.fin_iter), int(sa.fin_iter))
    y = sa.E_hist
    z = sa.temp_hist
    t = [i*np.max(y)/np.max(z) for i in z]
    plt.plot(x, y, color='red')
    #plt.plot(x, t, color = 'blue')
    plt.savefig(str('energy_'+sa.f.__name__+'.png'))








