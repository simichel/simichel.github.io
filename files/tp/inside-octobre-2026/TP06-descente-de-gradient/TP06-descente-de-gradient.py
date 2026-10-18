"""
===============================================================================
Projet : Descente de gradient
Auteur : Sixtine MICHEL
Date de creation : 24/09/2026

Description :
    Mini-TP guide sur le principe de la descente de gradient.

    Completer les TODO dans l'ordre, puis executer le programme avec Spyder.
    Choisir un backend graphique interactif (Automatic ou Qt), redemarrer la
    console IPython si necessaire, puis conserver plt.show(block=True).

    Une "bille" est placee sur une fonction mathematique. A chaque iteration :
        - on calcule la pente locale ;
        - on se deplace dans la direction opposee a cette pente ;
        - on se rapproche progressivement d'un minimum local.

    Cette idee est a la base de nombreuses methodes d'optimisation utilisees
    notamment en intelligence artificielle.

Dependances :
    - numpy
    - matplotlib

Execution :
    python 06-descente_de_gradient.py
===============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# =============================================================================
# PARAMETRES
# =============================================================================

# Bornes du domaine affiche selon les axes x et y.
X_MIN = -4
X_MAX = 4
Y_MIN = -4
Y_MAX = 4

# Coordonnees depuis lesquelles commence la descente.
POINT_INITIAL = np.array([3.4, -3.0], dtype=float)
# Taille du pas effectue dans la direction opposee au gradient.
TAUX_APPRENTISSAGE = 0.20
# Nombre maximal de pas de descente calcules.
NB_ITERATIONS = 120
# Duree entre deux images de l'animation, en millisecondes.
INTERVALLE_ANIMATION = 70


# =============================================================================
# FONCTION A OPTIMISER
# =============================================================================

def fonction(x, y):
    """
    Fonction mathematique dont on cherche un minimum.

    La fonction contient plusieurs reliefs afin de rendre la trajectoire
    plus interessante qu'une simple parabole.

    Parametres
    ----------
    x : float ou numpy.ndarray
    y : float ou numpy.ndarray

    Retour
    ------
    float ou numpy.ndarray
        Valeur de la fonction.
    """

    # TODO 1 — Evaluer les quatre termes de la fonction.
    # f = 0.18*(x**2+y**2) + 0.8*sin(x)
    #     + 0.6*cos(1.5*y) + 0.15*sin(x*y).
    # La sortie doit fonctionner pour des nombres et des tableaux.
    return 0.0 * (x + y)


# =============================================================================
# CALCUL DU GRADIENT
# =============================================================================

def gradient_numerique(x, y, epsilon=1e-4):
    """
    Approxime le gradient de la fonction par differences finies.

    Le gradient contient deux composantes :
        - variation selon x ;
        - variation selon y.

    Parametres
    ----------
    x : float
        Coordonne x.
    y : float
        Coordonne y.
    epsilon : float
        Petit pas utilise pour approximer les derivees.

    Retour
    ------
    numpy.ndarray
        Vecteur [df/dx, df/dy].
    """

    # Derivee partielle selon x.
    # TODO 2 — Approximer df/dx par difference centree.
    # Formule : (f(x+epsilon,y)-f(x-epsilon,y))/(2*epsilon).
    dfdx = 0.0

    # Derivee partielle selon y.
    # TODO 3 — Approximer df/dy par difference centree.
    # Formule : (f(x,y+epsilon)-f(x,y-epsilon))/(2*epsilon).
    dfdy = 0.0

    # TODO 4 — Renvoyer [dfdx, dfdy] dans un tableau de flottants.
    return np.zeros(2)


# =============================================================================
# UNE ETAPE DE DESCENTE
# =============================================================================

def effectuer_pas(point, taux_apprentissage):
    """
    Effectue un pas de descente de gradient.

    Parametres
    ----------
    point : numpy.ndarray
        Position actuelle [x, y].
    taux_apprentissage : float
        Taille du pas effectue.

    Retour
    ------
    numpy.ndarray
        Nouvelle position.
    """

    # Calcul de la pente locale.
    # TODO 5 — Calculer le gradient aux coordonnees du point courant.
    gradient = np.zeros(2)

    # Le signe moins permet de descendre dans la direction opposee au gradient.
    # TODO 6 — Calculer point - taux_apprentissage*gradient.
    nouveau_point = point.copy()

    return nouveau_point


# =============================================================================
# CALCUL COMPLET DE LA TRAJECTOIRE
# =============================================================================

def calculer_trajectoire(point_initial, nb_iterations, taux_apprentissage):
    """
    Calcule tous les points successifs de la descente de gradient.

    Retour
    ------
    numpy.ndarray
        Tableau contenant la trajectoire.
    """

    # TODO 7 — Initialiser la trajectoire avec une copie du point initial et
    # creer une seconde copie dans point.
    trajectoire = [np.zeros(2)]
    point = np.zeros(2)

    for _ in range(nb_iterations):
        # TODO 8 — Effectuer un nouveau pas et mettre a jour point.
        point = point.copy()

        # TODO 9 — Ajouter une copie du nouveau point a trajectoire.
        trajectoire.append(trajectoire[-1].copy())

    return np.array(trajectoire)


# =============================================================================
# VISUALISATION
# =============================================================================

def lancer_visualisation():
    """
    Affiche le paysage mathematique et anime la descente de gradient.

    La fenetre contient :
        - a gauche : une carte de niveaux avec la trajectoire ;
        - a droite : la valeur de la fonction au fil des iterations.
    """

    # Grille utilisee pour dessiner le paysage.
    # TODO 10 — Creer 250 valeurs regulieres sur chaque axe, puis utiliser
    # np.meshgrid(xs, ys) pour construire X et Y.
    xs = np.zeros(250)
    ys = np.zeros(250)
    X, Y = np.meshgrid(xs, ys)
    # TODO 11 — Evaluer fonction(X, Y) sur toute la grille.
    Z = np.zeros_like(X)

    # Calcul de la trajectoire.
    trajectoire = calculer_trajectoire(
        POINT_INITIAL,
        NB_ITERATIONS,
        TAUX_APPRENTISSAGE
    )

    # Valeurs successives de la fonction.
    # TODO 12 — Evaluer la fonction sur les deux colonnes de trajectoire.
    # Sortie : un tableau contenant une valeur par iteration.
    valeurs = np.zeros(len(trajectoire))

    # Creation de la fenetre.
    figure, (axe_paysage, axe_cout) = plt.subplots(
        1,
        2,
        figsize=(13, 6),
        gridspec_kw={"width_ratios": [1.3, 1]}
    )

    figure.suptitle(
        "Descente de gradient : chercher un minimum",
        fontsize=16
    )

    # -------------------------------------------------------------------------
    # Carte du paysage.
    # -------------------------------------------------------------------------

    axe_paysage.contourf(
        X,
        Y,
        Z,
        levels=35,
        cmap="viridis"
    )

    axe_paysage.contour(
        X,
        Y,
        Z,
        levels=20,
        colors="black",
        linewidths=0.25,
        alpha=0.5
    )

    axe_paysage.set_xlim(X_MIN, X_MAX)
    axe_paysage.set_ylim(Y_MIN, Y_MAX)
    axe_paysage.set_aspect("equal")
    axe_paysage.set_xlabel("x")
    axe_paysage.set_ylabel("y")
    axe_paysage.set_title("Paysage de la fonction")

    # Trace initiale de la trajectoire.
    ligne_traj, = axe_paysage.plot(
        [],
        [],
        marker="o",
        markersize=3,
        linewidth=1.5
    )

    # Point courant.
    point_courant, = axe_paysage.plot(
        [],
        [],
        marker="o",
        markersize=10
    )

    # -------------------------------------------------------------------------
    # Courbe de la valeur de la fonction.
    # -------------------------------------------------------------------------

    axe_cout.set_xlim(0, NB_ITERATIONS)
    axe_cout.set_ylim(
        float(np.min(valeurs)) - 0.2,
        float(np.max(valeurs)) + 0.2
    )
    axe_cout.set_xlabel("Iteration")
    axe_cout.set_ylabel("f(x, y)")
    axe_cout.set_title("Valeur de la fonction")
    axe_cout.grid(alpha=0.25)

    ligne_cout, = axe_cout.plot([], [])

    texte = axe_cout.text(
        0.05,
        0.95,
        "",
        transform=axe_cout.transAxes,
        va="top",
        bbox={"facecolor": "white", "alpha": 0.85}
    )

    # -------------------------------------------------------------------------
    # Animation.
    # -------------------------------------------------------------------------

    def mettre_a_jour(frame):
        """
        Affiche progressivement les points de la trajectoire.
        """

        # Portion deja parcourue.
        trajet_visible = trajectoire[:frame + 1]

        ligne_traj.set_data(
            trajet_visible[:, 0],
            trajet_visible[:, 1]
        )

        # Position actuelle.
        point = trajectoire[frame]

        point_courant.set_data(
            [point[0]],
            [point[1]]
        )

        # Evolution de la fonction.
        ligne_cout.set_data(
            np.arange(frame + 1),
            valeurs[:frame + 1]
        )

        # Gradient actuel.
        gradient = gradient_numerique(
            point[0],
            point[1]
        )

        texte.set_text(
            f"Iteration : {frame}\n"
            f"x = {point[0]:.3f}\n"
            f"y = {point[1]:.3f}\n"
            f"f(x,y) = {valeurs[frame]:.3f}\n"
            f"|gradient| = {np.linalg.norm(gradient):.3f}"
        )

        return (
            ligne_traj,
            point_courant,
            ligne_cout,
            texte
        )

    animation = FuncAnimation(
        figure,
        mettre_a_jour,
        frames=len(trajectoire),
        interval=INTERVALLE_ANIMATION,
        repeat=True,
        blit=False
    )

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.show(block=True)

    return animation


# =============================================================================
# PROGRAMME PRINCIPAL
# =============================================================================

def main():
    """
    Point d'entree du programme.
    """

    lancer_visualisation()


# =============================================================================
# EXECUTION
# =============================================================================

if __name__ == "__main__":
    main()
