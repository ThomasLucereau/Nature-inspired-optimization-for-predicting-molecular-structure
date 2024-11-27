import plotly.graph_objs as go
import numpy as np
from scipy.spatial import ConvexHull, Delaunay
from itertools import combinations
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import mpld3

def plot_polyhedron(vertice, nb_atoms,best_E):

    vertices = [[vertice[3*i], vertice[3*i+1],vertice[3*i+2]] for i in range(int(len(vertice)/3))]
    vertices = np.array(vertices)

    x, y, z = vertices.T

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    ax.view_init(elev=20, azim=30)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='k')

    hull = ConvexHull(vertices)

    for simplex in hull.simplices:
        face = [vertices[i] for i in simplex]

        poly = Poly3DCollection([face], alpha=0.5, linewidths=0.5, edgecolors='k',facecolors='r')


        ax.add_collection3d(poly)

    ax.set_title('Configuration '+str(nb_atoms)+' atomes'+'\n Plus basse énergie : '+str(best_E))
    plt.savefig('polyèdre'+str(nb_atoms)+'.png')

    plt.show()

camera_position = np.array([-1, -1, 0.5])





