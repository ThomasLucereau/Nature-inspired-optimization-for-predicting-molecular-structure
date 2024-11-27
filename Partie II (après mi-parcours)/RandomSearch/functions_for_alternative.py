import numba as nb

"====================================Implémentation des fonctions================================================="

@nb.njit()
def distance (molecule,i,j) -> float:
    a = ((molecule[3*i]-molecule[3*j])**2+(molecule[3*i+1]-molecule[3*j+1])**2+(molecule[3*i+2]-molecule[3*j+2])**2)**(1/2)
    return a

@nb.njit()
def Lennard_Jones_E(molecule: nb.types.float64[:, :]) -> float:
    taille = len(molecule)/3
    somme = 0.0
    for i in range(int(taille)):
        for j in range(i):
            dist = distance(molecule,i,j)
            beta = 1/(dist)**6
            somme = somme + (beta**2 - beta)
    return 4*somme









