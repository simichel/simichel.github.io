"""
===============================================================================
TP 00 : Introduction rapide a Python — 15 minutes
Auteur : Sixtine MICHEL

Objectif :
    Programmer une voiture dont la vitesse augmente puis diminue. Completer les
    six TODO dans l'ordre et executer apres chaque etape.

Avec Spyder : choisir un backend Automatic ou Qt, redemarrer la console si
necessaire, puis conserver plt.show(block=True).
===============================================================================
"""

from math import sqrt

import matplotlib.pyplot as plt


# Duree d'une etape de la simulation, en secondes.
DT = 1.0

# Numero de la derniere etape : la boucle ira donc de 0 a 15.
NB_ETAPES = 15

# Vitesse de la voiture a chaque etape, en metres par seconde.
VITESSES = [0, 1, 2, 4, 6, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Position du point auquel on comparera la position finale, en metres.
POINT_REFERENCE = 50.0


def simuler_voiture():
    """Calcule la position de la voiture pendant quinze secondes."""

    # Ces variables sont fournies : la voiture part de la position 0 m.
    position = 0.0
    temps = []
    positions = []

    print("Etape | Position (m) | Vitesse (m/s) | Distance a 0 (m) | Distance au point (m)")
    print("-------------------------------------------------------------------------------")

    # TODO 1 — Parcourir les etapes numerotees de 0 a 15.
    # Utiliser range(0, NB_ETAPES + 1).
    for etape in range(0, 0):

        # TODO 2 — Lire la vitesse correspondant a cette etape.
        # La valeur recherchee se trouve dans VITESSES a l'indice etape.
        vitesse = 0.0

        # TODO 3 — Calculer le deplacement puis mettre a jour la position.
        # Formules : deplacement = vitesse * DT
        #            position = position + deplacement
        deplacement = 0.0
        position = position

        # TODO 4 — Memoriser les deux resultats avec append.
        # Ajouter etape * DT dans temps et position dans positions.
        temps.append(temps[-1])
        positions.append(positions[-1])

        # TODO 5 — Calculer la distance a 0 puis au point de reference.
        # En une dimension : distance(a, b) = sqrt((a - b) ** 2).
        distance_origine = 0.0
        distance_point = 0.0

        # Affichage fourni : d signifie entier et .1f, une decimale.
        print(f"{etape:5d} | {position:12.1f} | {vitesse:13.1f} | "
              f"{distance_origine:16.1f} | {distance_point:21.1f}")

    return temps, positions


def afficher_resultat(temps, positions):
    """Trace l'evolution de la position dans une fenetre Matplotlib."""

    # TODO 6 — Tracer temps en abscisse et positions en ordonnee.
    # Utiliser marker="o" et linewidth=2.
    plt.plot([], [], marker="o", linewidth=2)

    # La mise en forme du graphique est fournie.
    plt.xlabel("Temps (s)")
    plt.ylabel("Position (m)")
    plt.title("Deplacement d'une voiture a vitesse variable")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show(block=True)


def main():
    """Lance la simulation puis affiche le graphique."""

    temps, positions = simuler_voiture()
    afficher_resultat(temps, positions)


if __name__ == "__main__":
    main()
