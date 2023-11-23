import networkx as nx
import matplotlib.pyplot as plt

def afficher_labyrinthe(Labyrinthe, colonnes, lignes):
    """ 
    """
    nodes = list(Labyrinthe.nodes()) 
    pos = {}
    for i in range(len(nodes)):
        n = nodes[i]
        l = i // colonnes
        c = i % colonnes
        pos[n] = (c, l)
    plt.clf() # Efface le dessin
    nx.draw(Labyrinthe, pos, with_labels=True)
    plt.show()

if __name__ == "__main__":
    # Création du labyrinthe de test
    aretes = [(0, 1), (0, 4), (1, 0), (1, 5), (2, 6), (3, 7), (4, 0), (4, 5), (5, 1) , \
     (5, 4), (5, 6), (5, 9), (6, 2), (6, 5), (6, 7), (6, 10), (7, 3), (7, 6), (8, 9),\
     (9, 5), (9, 8), (9, 10), (10, 6), (10, 9), (10, 11), (11, 10)]
    colonnes = 4
    lignes = 3
    nb_sommets = colonnes * lignes
    noeuds = list(range(nb_sommets))
    Labyrinthe = nx.Graph()
    Labyrinthe.add_nodes_from(noeuds)
    Labyrinthe.add_edges_from(aretes)

    # Lance le test de la fonction afficher_labyrinthe()
    afficher_labyrinthe(Labyrinthe, colonnes, lignes)

