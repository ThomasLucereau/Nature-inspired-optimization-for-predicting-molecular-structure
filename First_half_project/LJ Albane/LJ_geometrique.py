import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numba as nb

# Distance entre deux atomes i et j
@nb.njit()
def distance(molecule, i, j):
    dx = molecule[3*i] - molecule[3*j]
    dy = molecule[3*i+1] - molecule[3*j+1]
    dz = molecule[3*i+2] - molecule[3*j+2]
    return np.sqrt(dx**2 + dy**2 + dz**2)

# Potentiel de Lennard-Jones pour N molécules
@nb.njit()
def Lennard_Jones_E(molecule, nb_atoms):
    somme = 0.0
    for i in range(nb_atoms):
        for j in range(i+1, nb_atoms):
            dist = distance(molecule, i, j)
            if dist == 0:
                continue
            beta = 1 / (dist)**6
            somme += beta**2 - beta
    return 4 * somme

# Fonction de recuit simulé pour minimiser le potentiel de Lennard-Jones pour N molécules
def simulated_annealing(fonction, pt_depart, temp_initial, taux_descente, n_etapes, nb_atoms):
    pt_en_cours = pt_depart.copy()
    temps_act = temp_initial
    chemin = [pt_depart.copy()]
    E_hist = [fonction(pt_depart, nb_atoms)]  # Historique des énergies

    for step in range(n_etapes):
        voisin = pt_en_cours + np.random.uniform(-0.05, 0.05, pt_en_cours.shape) * (1 - step / n_etapes)
        voisin = np.clip(voisin, -2, 2)  # Limite les positions dans une boîte de [-2, 2]

        delta = fonction(voisin, nb_atoms) - fonction(pt_en_cours, nb_atoms)

        if delta < 0 or (delta > 0 and np.random.rand() < np.exp(-delta / temps_act)):
            pt_en_cours = voisin.copy()
            chemin.append(pt_en_cours.copy())
            E_hist.append(fonction(voisin, nb_atoms))

        temps_act *= taux_descente

    return pt_en_cours, chemin, E_hist

# Définition de la fonction à minimiser (potentiel de Lennard-Jones pour N molécules)
def f(positions, nb_atoms):
    if positions.size != 3 * nb_atoms:
        raise ValueError(f"Expected positions to have size {3 * nb_atoms}, but got {positions.size}")
    return Lennard_Jones_E(positions, nb_atoms)  # Calcule le potentiel de Lennard-Jones pour N molécules

# Fonction pour exécuter le recuit simulé et retourner l'énergie minimale pour un nombre donné d'atomes
def run_simulated_annealing(nb_atoms, n_trials=20):
    best_energy = float('inf')
    best_chemin = None
    best_E_hist = None
    
    for _ in range(n_trials):
        pt_depart = np.random.uniform(-2, 2, size=(3 * nb_atoms))  # Point de départ aléatoire dans une boîte de [-2, 2]
        temp_initial = 5000  # Température initiale
        taux_descente = 0.995  # Taux de descente
        n_etapes = 20000  # Nombre d'étapes

        # Exécute le recuit simulé
        resultat = simulated_annealing(f, pt_depart, temp_initial, taux_descente, n_etapes, nb_atoms)
        chemin = np.array(resultat[1])  # Chemin pris par le recuit simulé
        E_hist = np.array(resultat[2])  # Historique des énergies

        # Affiche l'énergie minimale trouvée
        min_energy = np.min(E_hist)
        if min_energy < best_energy:
            best_energy = min_energy
            best_chemin = chemin
            best_E_hist = E_hist
    
    print(f"Nombre d'atomes: {nb_atoms}, Énergie minimale trouvée : {best_energy:.2f}")
    return best_chemin, best_E_hist, best_energy

# Demande à l'utilisateur de définir le nombre d'atomes
nb_atoms = int(input("Entrez le nombre d'atomes : "))

# Exécute le recuit simulé pour le nombre d'atomes défini
chemin, E_hist, min_energy = run_simulated_annealing(nb_atoms)

# Compare avec les valeurs théoriques
theoretical_energies = {
    2: -1.000,
    3: -3.000,
    4: -6.000,
    5: -9.103852,
    6: -12.712062,
    7: -16.505384,
    8: -19.821489,
    9: -24.113360,
    10: -28.422532,
    11: -32.765970
}

theoretical_energy = theoretical_energies.get(nb_atoms, "N/A")

# Affiche les résultats
print(f"{nb_atoms} atomes: énergie trouvée = {min_energy:.2f}, énergie théorique = {theoretical_energy}")

# Plotting et animation
fig = plt.figure(figsize=(14, 6))

# Plot 3D pour le potentiel de Lennard-Jones
ax = fig.add_subplot(121, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Potentiel de Lennard-Jones pour N molécules')

# Définition de la grille pour le potentiel de Lennard-Jones
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        Z[i, j] = f(np.array([X[i, j]]*nb_atoms + [Y[i, j]]*nb_atoms + [0]*nb_atoms), nb_atoms)
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Plot 2D pour l'évolution de l'énergie
ax2 = fig.add_subplot(122)
ax2.set_xlabel('Étapes')
ax2.set_ylabel('Énergie')
ax2.set_title('Évolution de l\'énergie pendant le recuit simulé')
ax2.plot(np.arange(len(E_hist)), E_hist, color='blue')

# Initialisation pour l'animation du chemin pris
point, = ax.plot([], [], [], marker='o', color='red', markersize=8)
point2, = ax2.plot([], [], marker='o', color='red', markersize=8)
text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes)

# Fonction de mise à jour pour l'animation
def update(frame):
    pt_en_cours = chemin[frame]
    point.set_data(pt_en_cours[::3], pt_en_cours[1::3])
    point.set_3d_properties(pt_en_cours[2::3])
    point2.set_data([frame], [E_hist[frame]])
    text.set_text(f'Étape {frame}, Énergie: {E_hist[frame]:.2f}')
    return point, point2, text  # Retourne les objets à mettre à jour

ani = FuncAnimation(fig, update, frames=len(chemin), interval=20, repeat=False)
plt.show()
