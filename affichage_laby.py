import networkx as nx
import matplotlib.pyplot as plt

def afficher_labyrinthe(Labyrinthe, colonnes, lignes):
    nodes = list(Labyrinthe.nodes())
    pos = {}
    for i in range(len(nodes)):
        n = nodes[i]
        l = i // colonnes
        c = i % colonnes
        pos[n] = (c, l)

    plt.clf() # Efface le dessin
   
   
    nx.draw(Labyrinthe, pos, with_labels=True) 
   
    edge_labels = nx.get_edge_attributes(Labyrinthe, 'weight')
   
    nx.draw_networkx_edge_labels(Labyrinthe, pos, edge_labels)

    plt.show()

if __name__ == "__main__":
    # Création du labyrinthe de test
    aretes = [(0, 1, 1), (0, 4, 2), (1, 0, 3), (1, 5, 4), (2, 6, 5), (3, 7, 6), (4, 0, 7), (4, 5, 8), (5, 1, 9) , \
     (5, 4, 1), (5, 6, 2), (5, 9, 3), (6, 2, 4), (6, 5, 5), (6, 7, 6), (6, 10, 8), (7, 3, 9), (7, 6, 1), (8, 9, 2),\
     (9, 5, 3), (9, 8, 4), (9, 10, 5), (10, 6, 6), (10, 9, 7), (10, 11, 8), (11, 10, 9)]
    colonnes = 4
    lignes = 3
    
    nb_sommets = colonnes * lignes
    
    noeuds = list(range(nb_sommets))
    
    Labyrinthe = nx.Graph()
    
    Labyrinthe.add_nodes_from(noeuds)
    
    Labyrinthe.add_weighted_edges_from(aretes)

    # Lance le test de la fonction afficher_labyrinthe()
    afficher_labyrinthe(Labyrinthe, colonnes, lignes)

