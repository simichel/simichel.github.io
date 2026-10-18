"""
===============================================================================
TP 00 : Introduction rapide a Python — 15 minutes
Auteur : Sixtine MICHEL

Objectif :
    Comparer une voiture programmee et une voiture aux vitesses aleatoires.
    Completer les sept TODO dans l'ordre et executer apres chaque etape.

Avec Spyder : choisir un backend Automatic ou Qt, redemarrer la console si
necessaire, puis conserver plt.show(block=True).
===============================================================================
"""

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


# Duree d'une etape de la simulation, en secondes.
DT = 1.0

# Numero de la derniere etape : la boucle ira donc de 0 a 15.
NB_ETAPES = 15

# Vitesse de la voiture a chaque etape, en metres par seconde.
VITESSES = [0, 1, 2, 4, 6, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Position du point auquel on comparera la position finale, en metres.
POINT_REFERENCE = 50.0


def simuler_voiture(vitesses, nom):
    """Calcule la position d'une voiture pendant quinze secondes."""

    # Ces variables sont fournies : la voiture part de la position 0 m.
    position = 0.0
    temps = []
    positions = []

    print(f"\n{nom}")
    print("Etape | Position (m) | Vitesse (m/s) | Distance a 0 (m) | Distance au point (m)")
    print("-------------------------------------------------------------------------------")

    # TODO 1 — Parcourir les etapes numerotees de 0 a 15.
    # Utiliser range(0, NB_ETAPES + 1).
    for etape in range(0, 0):

        # TODO 2 — Lire la vitesse correspondant a cette etape.
        # La valeur recherchee se trouve dans vitesses a l'indice etape.
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


def afficher_resultat(temps, positions, temps_aleatoire, positions_aleatoires):
    """Compare les positions des deux voitures dans une fenetre Matplotlib."""

    # TODO 6 — Tracer les deux voitures avec un label pour chacune.
    # Utiliser marker="o" et linewidth=2 pour les deux courbes.
    plt.plot([], [], marker="o", linewidth=2, label="Programmee")
    plt.plot([], [], marker="o", linewidth=2, label="Aleatoire")

    # La mise en forme du graphique est fournie.
    plt.xlabel("Temps (s)")
    plt.ylabel("Position (m)")
    plt.title("Comparaison de deux voitures")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show(block=True)


def main():
    """Simule une voiture programmee et une voiture aleatoire."""

    # Une graine fixe permet de retrouver les memes vitesses a chaque lancement.
    np.random.seed(42)

    # TODO 7 (bonus) — Creer 16 vitesses aleatoires entre 0 et 8 m/s.
    # Utiliser np.random.uniform avec size=NB_ETAPES + 1.
    vitesses_aleatoires = np.zeros(NB_ETAPES + 1, dtype=float)

    # Les deux voitures sont arretees au depart.
    vitesses_aleatoires[0] = 0.0

    temps, positions = simuler_voiture(VITESSES, "Voiture programmee")
    temps_aleatoire, positions_aleatoires = simuler_voiture(
        vitesses_aleatoires,
        "Voiture aleatoire",
    )
    afficher_resultat(
        temps,
        positions,
        temps_aleatoire,
        positions_aleatoires,
    )


if __name__ == "__main__":
    main()
