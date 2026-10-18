"""
===============================================================================
Mini-TP : Propagation d'une epidemie
Auteur : Sixtine MICHEL

Objectif :
    Completer progressivement une simulation dans laquelle des individus se
    deplacent, se contaminent lorsqu'ils sont proches, puis deviennent
    immunises.

Consignes :
    - completer les TODO dans l'ordre ;
    - executer regulierement le programme dans Spyder ;
    - utiliser un backend graphique interactif (Automatic ou Qt) ;
    - ne pas modifier la partie VISUALISATION.

Dependances : numpy, matplotlib
===============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap


# =============================================================================
# PARAMETRES GENERAUX
# =============================================================================

# Nombre total d'individus dans la population.
NB_INDIVIDUS = 140
# Largeur et hauteur du monde carre.
TAILLE_MONDE = 100
# Distance maximale permettant une contamination.
RAYON_CONTAMINATION = 4.0
# Probabilite de contamination lors d'un contact.
PROBABILITE_CONTAMINATION = 0.20
# Nombre d'etapes pendant lesquelles un individu reste infecte.
DUREE_INFECTION = 90
# Valeur maximale de chaque composante de vitesse.
VITESSE_MAX = 1.1
# Nombre d'individus infectes au lancement de la simulation.
NB_INFECTES_INITIAUX = 4
# Duree entre deux images de l'animation, en millisecondes.
INTERVALLE_ANIMATION = 60

# Codes entiers utilises pour representer les trois etats de sante.
SAIN = 0
INFECTE = 1
IMMUNISE = 2

COULEURS_ETATS = ["#2E86AB", "#D1495B", "#6A994E"]
CARTE_COULEURS = ListedColormap(COULEURS_ETATS)


# =============================================================================
# CREATION DE LA POPULATION
# =============================================================================

def creer_population():
    """Cree les tableaux decrivant la population initiale."""

    # TODO 1 — Generer les positions initiales.
    # Creer un tableau de forme (NB_INDIVIDUS, 2) avec des valeurs aleatoires
    # uniformes comprises entre 0 et TAILLE_MONDE.
    positions = np.column_stack((
        np.linspace(5, TAILLE_MONDE - 5, NB_INDIVIDUS),
        np.full(NB_INDIVIDUS, TAILLE_MONDE / 2),
    ))

    # TODO 2 — Generer les vitesses initiales.
    # Creer un tableau de meme forme, avec des composantes aleatoires comprises
    # entre -VITESSE_MAX et VITESSE_MAX.
    vitesses = np.zeros((NB_INDIVIDUS, 2), dtype=float)

    # Tout le monde commence sain.
    etats = np.full(NB_INDIVIDUS, SAIN, dtype=int)

    # TODO 3 — Choisir les premiers individus infectes.
    # Tirer NB_INFECTES_INITIAUX indices distincts parmi NB_INDIVIDUS.
    # La valeur provisoire rend le programme executable mais n'est pas aleatoire.
    infectes = np.arange(NB_INFECTES_INITIAUX)
    etats[infectes] = INFECTE

    # Chaque compteur indique depuis combien de generations la personne est
    # infectee. Au depart, tous les compteurs sont nuls.
    durees = np.zeros(NB_INDIVIDUS, dtype=int)

    return {
        "positions": positions,
        "vitesses": vitesses,
        "etats": etats,
        "durees": durees,
    }


# =============================================================================
# DEPLACEMENTS
# =============================================================================

def deplacer_individus(population):
    """Deplace les individus et les fait rebondir sur les quatre bords."""

    positions = population["positions"]
    vitesses = population["vitesses"]

    # TODO 4 — Appliquer un pas de deplacement.
    # Construire la nouvelle position en ajoutant 1.0 fois la vitesse.
    # La notation [:] modifie le tableau stocke dans le dictionnaire population.
    positions[:] = positions

    # On examine chaque individu separement.
    for i in range(NB_INDIVIDUS):

        # TODO 5 — Completer les conditions des bords gauche et droit.
        # x se trouve dans positions[i, 0] et vx dans vitesses[i, 0].
        if False:
            positions[i, 0] = 0
            vitesses[i, 0] = -vitesses[i, 0]

        if False:
            positions[i, 0] = TAILLE_MONDE
            vitesses[i, 0] = -vitesses[i, 0]

        # TODO 6 — Completer les conditions des bords bas et haut.
        # y se trouve dans positions[i, 1] et vy dans vitesses[i, 1].
        if False:
            positions[i, 1] = 0
            vitesses[i, 1] = -vitesses[i, 1]

        if False:
            positions[i, 1] = TAILLE_MONDE
            vitesses[i, 1] = -vitesses[i, 1]


# =============================================================================
# CONTAMINATION
# =============================================================================

def contaminer_population(population):
    """Contamine eventuellement les personnes saines proches d'un infecte."""

    positions = population["positions"]
    etats = population["etats"]

    nouveaux_infectes = []

    for i in range(NB_INDIVIDUS):

        # TODO 7 — Traiter uniquement une personne saine.
        if False:
            infecte_proche = False

            for j in range(NB_INDIVIDUS):

                # TODO 8 — Verifier si la personne j est infectee.
                if False:

                    # TODO 9 — Calculer la distance entre i et j.
                    # Formule : sqrt((xj-xi)**2 + (yj-yi)**2).
                    dx = 0.0
                    dy = 0.0
                    distance = 0.0

                    if distance < RAYON_CONTAMINATION:
                        infecte_proche = True
                        break

            # TODO 10 — Contaminer selon la probabilite si un infecte est proche.
            # Combiner infecte_proche et le tirage aleatoire avec and.
            if False:
                nouveaux_infectes.append(i)

    # On attend la fin du parcours pour eviter qu'une personne nouvellement
    # infectee en contamine une autre durant la meme generation.
    etats[nouveaux_infectes] = INFECTE


# =============================================================================
# GUERISON / IMMUNISATION
# =============================================================================

def mettre_a_jour_infections(population):
    """Met a jour la duree des infections et immunise les personnes gueries."""

    etats = population["etats"]
    durees = population["durees"]

    for i in range(NB_INDIVIDUS):

        # TODO 11 — Si i est infecte, augmenter sa duree d'infection de 1.
        if False:
            durees[i] = durees[i]

            # TODO 12 — Immuniser i lorsque la duree maximale est atteinte.
            if False:
                etats[i] = IMMUNISE


# =============================================================================
# STATISTIQUES
# =============================================================================

def compter_etats(population):
    """Renvoie les nombres de personnes saines, infectees et immunisees."""

    etats = population["etats"]

    sains = 0
    infectes = 0
    immunises = 0

    # TODO 13 — Parcourir les etats et incrementer le bon compteur.
    for etat in etats:
        if False:
            sains = sains + 1
        elif False:
            infectes = infectes + 1
        elif False:
            immunises = immunises + 1

    return sains, infectes, immunises


# =============================================================================
# VISUALISATION — PARTIE FOURNIE
# =============================================================================

def lancer_visualisation():
    """Lance l'animation et affiche l'evolution des trois populations."""

    population = creer_population()

    sains, infectes, immunises = compter_etats(population)
    historique = {
        "sains": [sains],
        "infectes": [infectes],
        "immunises": [immunises],
    }

    figure, (axe_monde, axe_stats) = plt.subplots(
        1,
        2,
        figsize=(13, 6),
        gridspec_kw={"width_ratios": [2, 1]}
    )
    figure.suptitle("Propagation simplifiee d'une epidemie", fontsize=16)

    nuage = axe_monde.scatter(
        population["positions"][:, 0],
        population["positions"][:, 1],
        c=population["etats"],
        cmap=CARTE_COULEURS,
        vmin=0,
        vmax=2,
        s=45,
        edgecolors="black",
        linewidths=0.3
    )
    axe_monde.set_xlim(0, TAILLE_MONDE)
    axe_monde.set_ylim(0, TAILLE_MONDE)
    axe_monde.set_aspect("equal")
    axe_monde.set_title("Population mobile")
    axe_monde.set_xlabel("x")
    axe_monde.set_ylabel("y")

    ligne_sains, = axe_stats.plot(
        [0], historique["sains"], color=COULEURS_ETATS[SAIN], label="Sains"
    )
    ligne_infectes, = axe_stats.plot(
        [0], historique["infectes"], color=COULEURS_ETATS[INFECTE], label="Infectes"
    )
    ligne_immunises, = axe_stats.plot(
        [0], historique["immunises"], color=COULEURS_ETATS[IMMUNISE], label="Immunises"
    )
    axe_stats.set_title("Evolution de la population")
    axe_stats.set_xlabel("Generation")
    axe_stats.set_ylabel("Nombre d'individus")
    axe_stats.set_ylim(0, NB_INDIVIDUS)
    axe_stats.grid(alpha=0.25)
    axe_stats.legend()

    texte_stats = axe_monde.text(
        0.02,
        0.98,
        "",
        transform=axe_monde.transAxes,
        va="top",
        bbox={"facecolor": "white", "alpha": 0.85}
    )

    def mettre_a_jour(frame):
        """Calcule une generation puis rafraichit les graphiques."""

        deplacer_individus(population)
        contaminer_population(population)
        mettre_a_jour_infections(population)

        sains, infectes, immunises = compter_etats(population)
        historique["sains"].append(sains)
        historique["infectes"].append(infectes)
        historique["immunises"].append(immunises)

        nuage.set_offsets(population["positions"])
        nuage.set_array(population["etats"].astype(float))
        texte_stats.set_text(
            f"Generation : {frame}\n"
            f"Sains : {sains}\n"
            f"Infectes : {infectes}\n"
            f"Immunises : {immunises}"
        )

        x = np.arange(len(historique["sains"]))
        ligne_sains.set_data(x, historique["sains"])
        ligne_infectes.set_data(x, historique["infectes"])
        ligne_immunises.set_data(x, historique["immunises"])
        axe_stats.set_xlim(0, max(50, len(x)))

        return (
            nuage,
            ligne_sains,
            ligne_infectes,
            ligne_immunises,
            texte_stats
        )

    animation = FuncAnimation(
        figure,
        mettre_a_jour,
        interval=INTERVALLE_ANIMATION,
        blit=False,
        cache_frame_data=False
    )

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.show(block=True)
    return animation


def main():
    """Point d'entree du mini-TP."""

    lancer_visualisation()


if __name__ == "__main__":
    main()
