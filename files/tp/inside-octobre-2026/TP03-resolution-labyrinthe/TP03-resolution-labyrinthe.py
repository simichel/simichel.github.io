"""
===============================================================================
Mini-TP : Resolution visuelle d'un labyrinthe
Auteur : Sixtine MICHEL

Objectif :
    Completer la generation d'un labyrinthe puis sa resolution avec un
    parcours en largeur (BFS, Breadth-First Search).

Consignes :
    - completer les TODO dans l'ordre ;
    - executer regulierement le programme dans Spyder ;
    - utiliser un backend graphique interactif (Automatic ou Qt) ;
    - ne pas modifier la partie ANIMATION.

Dependances : numpy, matplotlib
===============================================================================
"""

from collections import deque
import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


# =============================================================================
# PARAMETRES
# =============================================================================

# Dimensions de la grille ; des valeurs impaires simplifient sa construction.
NB_LIGNES = 21
NB_COLONNES = 31
# Duree entre deux images de l'animation, en millisecondes.
INTERVALLE_ANIMATION = 35

# Codes entiers des differents contenus possibles d'une case.
MUR = 0
PASSAGE = 1
EXPLORE = 2
FRONTIERE = 3
CHEMIN = 4
DEPART = 5
ARRIVEE = 6

COULEURS_LABYRINTHE = [
    "black",
    "white",
    "lightblue",
    "orange",
    "gold",
    "limegreen",
    "red",
]
CARTE_COULEURS = ListedColormap(COULEURS_LABYRINTHE)


# =============================================================================
# GENERATION DU LABYRINTHE
# =============================================================================

def creer_labyrinthe(nb_lignes, nb_colonnes):
    """Genere un labyrinthe parfait par exploration aleatoire."""

    # Des dimensions impaires permettent d'alterner cellules et murs.
    if nb_lignes % 2 == 0:
        nb_lignes += 1
    if nb_colonnes % 2 == 0:
        nb_colonnes += 1

    # Au depart, la grille ne contient que des murs.
    grille = np.zeros((nb_lignes, nb_colonnes), dtype=int)

    depart = (1, 1)
    grille[depart] = PASSAGE

    # La pile memorise le chemin de generation. Sa derniere case est la case
    # depuis laquelle on cherche a avancer.
    pile = [depart]

    # TODO 1 — Definir les quatre directions de generation.
    # On doit avancer de deux cases verticalement ou horizontalement afin de
    # conserver un mur entre deux cellules logiques.
    directions = []

    while pile:
        ligne, colonne = pile[-1]
        voisins = []

        for dl, dc in directions:
            # TODO 2 — Calculer les coordonnees (nl, nc) du candidat.
            nl = ligne
            nc = colonne

            # TODO 3 — Conserver uniquement un candidat valide.
            # Il doit rester a l'interieur de la bordure et correspondre a une
            # cellule encore egale a MUR.
            if False:
                voisins.append((nl, nc, dl, dc))

        if voisins:
            # TODO 4 — Choisir aleatoirement un candidat dans voisins.
            # La valeur provisoire est valide mais ne produit aucune variete.
            nl, nc, dl, dc = voisins[0]

            # TODO 5 — Creuser puis avancer.
            # 1. Ouvrir le mur situe a mi-chemin avec une division entiere // 2.
            # 2. Ouvrir la nouvelle cellule (nl, nc).
            # 3. Ajouter cette cellule au sommet de la pile.
            # La valeur provisoire interrompt cette branche sans bloquer le TP.
            pile.pop()

        else:
            # Aucun voisin disponible : on revient a la case precedente.
            pile.pop()

    return grille


# =============================================================================
# VOISINS ACCESSIBLES
# =============================================================================

def voisins_accessibles(grille, case):
    """Retourne les cases voisines accessibles depuis une case."""

    ligne, colonne = case
    voisins = []

    # TODO 6 — Definir les quatre deplacements du parcours.
    # Cette fois, on se deplace d'une seule case dans chaque direction.
    directions = []

    for dl, dc in directions:
        # TODO 7 — Calculer les coordonnees de la case voisine.
        nl = ligne
        nc = colonne

        # TODO 8 — Verifier que la case est dans la grille et n'est pas un mur.
        if False:
            voisins.append((nl, nc))

    return voisins


# =============================================================================
# PREPARATION DU PARCOURS EN LARGEUR
# =============================================================================

def preparer_resolution(grille, depart, arrivee):
    """Prepare la file, l'ensemble visite et les liens de parente du BFS."""

    # Une deque permet d'ajouter a droite et de retirer a gauche efficacement.
    return {
        "file": deque([depart]),
        "visites": {depart},
        "parents": {depart: None},
        "depart": depart,
        "arrivee": arrivee,
        "termine": False,
        "chemin": [],
    }


# =============================================================================
# UNE ETAPE DU BFS
# =============================================================================

def etape_bfs(grille, etat):
    """Effectue une seule etape du parcours en largeur."""

    if etat["termine"]:
        return

    if not etat["file"]:
        # La file vide signifie qu'aucun chemin n'a ete trouve.
        etat["termine"] = True
        return

    # TODO 9 — Retirer la plus ancienne case de la file.
    # Une deque fournit la methode popleft(). La valeur provisoire retire la
    # case la plus recente et correspond donc a une pile, pas a un BFS.
    case = etat["file"].pop()

    if case == etat["arrivee"]:
        etat["termine"] = True

        chemin = []
        courant = case

        while courant is not None:
            # TODO 10 — Reconstruire le chemin.
            # Ajouter courant au chemin, puis remonter vers son parent.
            chemin.append(courant)
            courant = None

        # La reconstruction part de l'arrivee : on inverse la liste.
        etat["chemin"] = chemin[::-1]
        return

    for voisin in voisins_accessibles(grille, case):

        # TODO 11 — Traiter uniquement un voisin encore jamais visite.
        if False:
            # TODO 12 — Memoriser puis planifier ce voisin.
            # 1. L'ajouter a l'ensemble des visites.
            # 2. Memoriser que case est son parent.
            # 3. L'ajouter a droite de la file.
            pass


# =============================================================================
# CONSTRUCTION DE L'IMAGE
# =============================================================================

def construire_image(grille, etat):
    """Construit la grille de codes couleur affichee par Matplotlib."""

    image = grille.copy()

    for ligne, colonne in etat["visites"]:
        # TODO 13 — Colorer en EXPLORE une case visitee qui n'est pas un mur.
        pass

    for ligne, colonne in etat["file"]:
        # TODO 14 — Colorer en FRONTIERE chaque case encore dans la file.
        pass

    for ligne, colonne in etat["chemin"]:
        # TODO 15 — Colorer en CHEMIN chaque case du chemin final.
        pass

    # Le depart et l'arrivee restent prioritaires sur les autres couleurs.
    dl, dc = etat["depart"]
    al, ac = etat["arrivee"]
    image[dl, dc] = DEPART
    image[al, ac] = ARRIVEE

    return image


# =============================================================================
# ANIMATION — PARTIE FOURNIE
# =============================================================================

def lancer_visualisation():
    """Genere un labyrinthe et anime sa resolution."""

    grille = creer_labyrinthe(NB_LIGNES, NB_COLONNES)

    depart = (1, 1)
    arrivee = (grille.shape[0] - 2, grille.shape[1] - 2)
    etat = preparer_resolution(grille, depart, arrivee)

    figure, axe = plt.subplots(figsize=(10, 7))
    figure.suptitle(
        "Resolution d'un labyrinthe par parcours en largeur",
        fontsize=15
    )

    image = axe.imshow(
        construire_image(grille, etat),
        cmap=CARTE_COULEURS,
        vmin=0,
        vmax=6,
        interpolation="nearest"
    )
    axe.set_xticks([])
    axe.set_yticks([])

    texte = axe.set_title(
        "Bleu : explore | Orange : frontiere | Jaune : chemin"
    )

    def mettre_a_jour(frame):
        """Effectue quelques etapes de BFS puis rafraichit l'affichage."""

        for _ in range(4):
            if not etat["termine"]:
                etape_bfs(grille, etat)

        image.set_data(construire_image(grille, etat))

        if etat["termine"] and etat["chemin"]:
            texte.set_text(
                f"Chemin trouve ! Longueur : {len(etat['chemin'])} cases"
            )
        else:
            texte.set_text(f"Cases explorees : {len(etat['visites'])}")

        return image, texte

    animation = FuncAnimation(
        figure,
        mettre_a_jour,
        interval=INTERVALLE_ANIMATION,
        blit=False,
        cache_frame_data=False
    )

    plt.tight_layout()
    plt.show(block=True)
    return animation


def main():
    """Point d'entree du mini-TP."""

    lancer_visualisation()


if __name__ == "__main__":
    main()
