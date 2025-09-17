import numpy as np

#fonction = fonction à minimiser 
#pt_depart = point de départ de l'algo (tableau numpy)
#temp_initial = température initiale
#taux_descente = taux de refroidissement 
#n_étapes = nombre d'étapes 

def f(vector):
    return ((1.5-vector[0]+vector[0]*vector[1])**2
            + (2.25-vector[0]+vector[0]*vector[1]**2)**2 + (2.265-vector[0]+vector[0]*vector[1]**3)**2)


def simulated_annealing(fonction, pt_depart, temp_initial, taux_descente, n_etapes):
    pt_en_cours = pt_depart #intialisation du point en cours au point de départ
    temps_act = temp_initial #initialisation de la température à la température initiale

    for step in range(n_etapes): #boucle sur le nombre d'étapes
        voisin = pt_en_cours + np.random.uniform(-1, 1, pt_en_cours.shape) #création d'un voisin aléatoire
        delta = fonction(voisin) - fonction(pt_en_cours) #calcul de la différence de fonction entre le voisin et le point en cours
        if  delta<0 or delta>0 and fonction(voisin) < np.exp(-delta/temps_act): #si la différence est négative ou si elle est positive  on autorise une remontée avec une certaine probabilité
            pt_en_cours = voisin

        temps_act *= taux_descente

    return pt_en_cours



print(simulated_annealing(f, np.array([0, 0]), 100, 0.9, 1000))