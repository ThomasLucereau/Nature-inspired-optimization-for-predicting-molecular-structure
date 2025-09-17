import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Fonction à minimiser
def f(vector):
    return ((1.5 - vector[0] + vector[0] * vector[1])**2 +
            (2.25 - vector[0] + vector[0] * vector[1]**2)**2 +
            (2.265 - vector[0] + vector[0] * vector[1]**3)**2)

def simulated_annealing(fonction, pt_depart, temp_initial, taux_descente, n_etapes):
    pt_en_cours = pt_depart
    temps_act = temp_initial
    chemin = [pt_depart]
    for step in range(n_etapes):
        voisin = pt_en_cours + np.random.uniform(-1, 1, pt_en_cours.shape)
        delta = fonction(voisin) - fonction(pt_en_cours)
        if delta < 0 or (delta > 0 and fonction(voisin) < np.exp(-delta / temps_act)):
            pt_en_cours = voisin
            chemin.append(pt_en_cours)
        temps_act *= taux_descente

    return [pt_en_cours, chemin]

pt_depart = np.array([3, 0.5])
temp_initial = 1000
taux_descente = 0.99  
n_etapes = 1000

resultat = simulated_annealing(f, pt_depart, temp_initial, taux_descente, n_etapes)
chemin = resultat[1]

#pt en cours image


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(121, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax2 = fig.add_subplot(122)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Fonction à minimiser')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f([X, Y])

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax2.contourf(X, Y, Z, 50, cmap='viridis')

point, = ax.plot([], [], [], marker='o', color='red', markersize=8)
point2, = ax2.plot([], [], marker='o', color='red', markersize=8)

text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes)

def update(frame):
    pt_en_cours = chemin[frame]
    point.set_data(pt_en_cours[0], pt_en_cours[1])
    point.set_3d_properties(f(pt_en_cours))
    point2.set_data(pt_en_cours[0], pt_en_cours[1])
    text.set_text(f'({pt_en_cours[0]:.2f}, {pt_en_cours[1]:.2f})')
    return point, point2, text

ani = FuncAnimation(fig, update, frames=len(chemin), interval=200, repeat=False)
plt.show()
