import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from celluloid import Camera

nb_particles = 1
nb_coordinates_particle = 2
nb_search = 1000000



def f2(vector):
    return 20 + (vector[0]**2 - 10*np.cos(2*np.pi*vector[0])) + (vector[1]**2 - 10*np.cos(2*np.pi*vector[1]))



def f1(vector):
    return ((1.5-vector[0]+vector[0]*vector[1])**2
            + (2.25-vector[0]+vector[0]*vector[1]**2)**2 + (2.265-vector[0]+vector[0]*vector[1]**3)**2)


def random_search(function,recherche):
    """
    :param function: fonction à optimiser
    :param recherche: domaine de définition sur lequel chercher [-recherche, recherche]
    :return: abscisse du minimum de la fonction, minimum de la fonction, liste des différents minimas trouvés (en thérorie)
    """
    L=[]
    zero = np.zeros((nb_coordinates_particle, nb_particles))
    return_value = np.random.uniform(-recherche, recherche, zero.shape)
    for i in range(nb_search):
        value = np.random.uniform(-recherche, recherche, zero.shape)
        if function(value) < function(return_value):
            return_value = value
            L.append(return_value)
    return  return_value, function(return_value),L

def gif_maker(f,recherche):
    """

    :param f: fonction à optimiser
    :param recherche: borne du domaine de définition
    :return: gif illustrant la recherche
    """

    result = random_search(f,recherche) #on lance une recherche de minima aléatoire

    L = result[2] #on récupère la liste des abscisses des minimas

    x = np.linspace(-recherche, recherche, 30)
    y = np.linspace(-recherche, recherche, 30)

    X, Y = np.meshgrid(x, y)
    Z = f((X, Y))


    """
    Dans ce qui suit, on illustre le parcours des différents minimas dans un gif
    
    Pour chaque minima on fait 5 frame pour que la vidéo soit visuelle
    """

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.view_init(elev=65., azim=90)
    camera = Camera(fig)
    for i in range(len(L)):
        for j in range(5): # 5 frame par minima

            ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                            cmap=cm.coolwarm, alpha=0.8, edgecolor='none')

            scatter, = ax.plot([L[i][0]], [L[i][1]], [f((L[i][0], L[i][1]))], "o", markersize=8, color="red")
            plt.pause(0.5)
            camera.snap()

    print(result[0])
    print(len(L))

    for i in range(25):
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap=cm.coolwarm, alpha=0.8, edgecolor='none')
        scatter, = ax.plot([L[-1][0]], [L[-1][1]], [f((L[-1][0], L[-1][1]))], "o", markersize=0, color="red")
        plt.pause(0.5)
        camera.snap()

    ani = camera.animate()
    name=str('animation'+ f.__name__ +'.gif')
    print(name)
    ani.save(name, writer='PillowWriter', fps=5)

    return


gif_maker(f2, 5.12)






