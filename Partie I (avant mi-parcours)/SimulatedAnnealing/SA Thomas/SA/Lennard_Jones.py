import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

"====================================Implémentation des fonctions================================================="
def distance (molecule,i,j):
    return np.sqrt((molecule[3*i]-molecule[3*j])**2+(molecule[3*i+1]-molecule[3*j+1])**2+(molecule[3*i+2]-molecule[3*j+2])**2)
def Lennard_Jones_E(molecule,nb_atoms):
    taille = len(molecule)/3
    somme = 0
    for i in range(int(taille)):
        for j in range(i):
                beta = 1/(distance(molecule,i,j))**6
                somme += beta**2 - beta
    return 4*somme



xi,yi,zi,xj,yj,zj = sp.symbols('xi yi zi xj yj zj')


expr = 1/((xi-xj)**2+(yi-yj)**2+(zi-zj)**2)**12 - 1/((xi-xj)**2+(yi-yj)**2+(zi-zj)**2)**6
def dfdx():
    exp = sp.diff(expr,xi)
    return sp.lambdify([xi,yi,zi,xj,yj,zj], exp)

df_dx = dfdx()

def LJ_grad(molecule):
    taille = len(molecule)
    gradient = np.array([[0] for i in range(taille)])

    for i in range(taille):
        df_dx_i = 0
        if i % 3 == 0:
            for j in range(int(i/3)):
                df_dx_i += df_dx(molecule[i],molecule[i+1],molecule[i+2],molecule[3*j], molecule[3*j+1], molecule[3*j+2])
            for z in range(int(i/3),int(taille/3)):
                df_dx_i += df_dx(molecule[i], molecule[i + 1], molecule[i + 2], molecule[3 * z],molecule[3 * z + 1], molecule[3 * z + 2])

        if i % 3 == 1:
            for j in range(int(i / 3)):
                df_dx_i += df_dx(molecule[i-1], molecule[i], molecule[i + 1], molecule[3 * j], molecule[3 * j + 1],
                                 molecule[3 * j + 2])
            for z in range(int(i / 3), int(taille / 3)):
                df_dx_i += df_dx(molecule[i - 1], molecule[i], molecule[i + 1], molecule[3 + z],
                                 molecule[3 * z + 1], molecule[3 * z + 2])

        if i % 3 == 2:
            for j in range(int((i-2) / 3)):
                df_dx_i += df_dx(molecule[i-2], molecule[i-1], molecule[i], molecule[3 * j], molecule[3 * j + 1],
                                 molecule[3 * j + 2])
            for z in range(int((i-2) / 3), int(taille / 3)):
                df_dx_i += df_dx(molecule[i - 2], molecule[i - 1], molecule[i], molecule[3 + z],
                                 molecule[3 * z + 1], molecule[3 * z + 2])
        gradient[i] = df_dx_i

    return gradient




"============================================== Améliorations ==============================================================="

def tolerance(sa,tolerance_initiale):
    result = 1/(sa.iter)**4
    if sa.iter == 1 or result > tolerance_initiale:
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








