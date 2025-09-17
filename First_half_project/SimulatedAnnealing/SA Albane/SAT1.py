import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Fonction à minimiser
def f(vector):
    return ((1.5 - vector[0] + vector[0] * vector[1])**2 +
            (2.25 - vector[0] + vector[0] * vector[1]**2)**2 +
            (2.265 - vector[0] + vector[0] * vector[1]**3)**2)

# Loi de décroissance de la Température = logarithmique 
def logarithmic_decay(T0, t):
    return T0 / np.log(t + 1)

# SA
def simulated_annealing(fonction, pt_depart, temp_initial, n_etapes, limites):
    pt_en_cours = pt_depart
    chemin = [pt_depart]
    for step in range(1, n_etapes + 1):  
        voisin = pt_en_cours + np.random.uniform(-0.01, 0.01, pt_en_cours.shape)  
        voisin = np.clip(voisin, limites[0], limites[1])
        delta = fonction(voisin) - fonction(pt_en_cours)
        temp_actuelle = logarithmic_decay(temp_initial, step)
        if delta < 0 or (delta > 0 and np.random.rand() < np.exp(-delta / temp_actuelle)):
            pt_en_cours = voisin
            chemin.append(pt_en_cours)

    return [pt_en_cours, chemin]

# Paramètres
pt_depart = np.array([3, 0.5])
temp_initial = 1000
n_etapes = 50000  #
limites = np.array([[-5, -5], [5, 5]])  # Limites pour x et y


resultat = simulated_annealing(f, pt_depart, temp_initial, n_etapes, limites)
solution_finale, chemin = resultat


valeur_minimale = f(solution_finale)
print(f'Solution trouvée: {solution_finale}')
print(f'Valeur minimale trouvée: {valeur_minimale}')

fig = plt.figure(figsize=(14, 6))
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

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)
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
