import numpy as np
import matplotlib.pyplot as plt
import time

# Définition de la fonction de Goldstein-Price
def goldstein_price(x, y):
    term1 = (1 + ((x + y + 1)**2) * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
    term2 = (30 + ((2*x - 3*y)**2) * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return term1 * term2

# SA
def simulated_annealing(decay_type, max_iter=1000, initial_temp=1000, alpha=0.9):
    x, y = np.random.uniform(-2, 2), np.random.uniform(-2, 2)
    current_value = goldstein_price(x, y)
    best_x, best_y, best_value = x, y, current_value
    temperature = initial_temp
    convergence_time = None

    values = []
    temperatures = []
    start_time = time.time()
    
    for i in range(max_iter):
        new_x = x + np.random.uniform(-0.1, 0.1)
        new_y = y + np.random.uniform(-0.1, 0.1)
        new_value = goldstein_price(new_x, new_y)
        
        if new_value < best_value:
            best_x, best_y, best_value = new_x, new_y, new_value

        if new_value < current_value or np.random.rand() < np.exp((current_value - new_value) / temperature):
            x, y, current_value = new_x, new_y, new_value
        
        if current_value == best_value and convergence_time is None:
            convergence_time = time.time() - start_time
        
        values.append(best_value)
        temperatures.append(temperature)
        
        if decay_type == "exponentielle":
            temperature *= alpha
        elif decay_type == "linéaire":
            temperature -= initial_temp / max_iter
        elif decay_type == "géométrique":
            temperature = initial_temp / (1 + alpha * i)
        else:
            raise ValueError("Type de décroissance non supporté")

        if temperature <= 0:
            break

    if convergence_time is None:
        convergence_time = time.time() - start_time

    return best_x, best_y, best_value, values, temperatures, convergence_time

# Comparaison des trois décroi en T
decay_types = ["exponentielle", "linéaire", "géométrique"]
results = {}
theoretical_min_value = 3

for decay_type in decay_types:
    best_x, best_y, best_value, values, temperatures, convergence_time = simulated_annealing(decay_type)
    results[decay_type] = {
        "best_x": best_x,
        "best_y": best_y,
        "best_value": best_value,
        "values": values,
        "temperatures": temperatures,
        "convergence_time": convergence_time
    }
    print(f"Méthode: {decay_type}")
    print(f"Meilleur x: {best_x}")
    print(f"Meilleur y: {best_y}")
    print(f"Meilleure valeur: {best_value}")
    print(f"Temps de convergence: {convergence_time:.4f} secondes")
    print(f"Écart par rapport à la valeur théorique: {best_value - theoretical_min_value:.4f}")
    print()

# Tracé 
plt.figure(figsize=(14, 10))

# Graphique 
for decay_type in decay_types:
    plt.plot(results[decay_type]["values"], label=decay_type)
plt.axhline(theoretical_min_value, color='r', linestyle='--', label='Valeur théorique minimale')
plt.xlabel("Itérations")
plt.ylabel("Valeur de la fonction de Goldstein-Price")
plt.title("Évolution de la valeur de la fonction")
plt.legend()


plt.tight_layout()
plt.show()

# Ccl
best_method = min(results, key=lambda x: results[x]["best_value"])
print(f"La méthode la plus optimale est : {best_method}")
print(f"Valeur trouvée par cette méthode : {results[best_method]['best_value']}")
print(f"Écart par rapport à la valeur théorique : {results[best_method]['best_value'] - theoretical_min_value:.4f}")
print(f"Temps de convergence : {results[best_method]['convergence_time']:.4f} secondes")
