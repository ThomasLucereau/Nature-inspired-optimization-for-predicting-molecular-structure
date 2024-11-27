import plotly.graph_objs as go
import numpy as np
from scipy.spatial import ConvexHull, Delaunay
from itertools import combinations
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import mpld3

def plot_polyhedron(sa,vertice):

    vertices = [[vertice[3*i][0], vertice[3*i+1][0],vertice[3*i+2][0]] for i in range(int(len(vertice)/3))]
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

    ax.set_title('Configuration '+str(sa.nb_atoms)+' atomes'+'\n Plus basse énergie : '+str(sa.best_E))
    plt.savefig('polyèdre'+str(sa.nb_atoms)+'.png')

    plt.show()

camera_position = np.array([-1, -1, 0.5])

def visu_polyhedron(sa,vertices):
    plot_polyhedron(sa,vertices)

vertic =[[ 0.24998706],
  [ 0.40942927],
  [-0.60669696],
  [-0.43085758],
  [ 0.40193882],
  [ 0.28559297],
  [-0.05191625],
  [-0.56542917],
  [-0.1394932 ],
  [ 0.65007794],
  [ 0.12275294],
  [ 0.40214129]
]

"""

    x, y, z = vertices.T

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

    hull = ConvexHull(vertices)

    for simplex in hull.simplices:
        face = [vertices[i] for i in simplex]
        poly = Poly3DCollection([face], alpha=1, linewidths=0.5, edgecolors='k',)
        ax.add_collection3d(poly)

    ax.set_title('Configuration '+str(sa.nb_atoms)+' atomes'+'\n Plus basse énergie : '+str(sa.best_E))
    plt.savefig('polyhedre'+str(sa.nb_atoms)+'.png')

    plt.show()

"""