"""
===============================================================================
Mini-TP : Jeu de la vie de Conway
Auteur : Sixtine MICHEL

Objectif :
    Completer les 11 TODO dans l'ordre afin de programmer les regles du Jeu de
    la vie de John Conway sur une grille NumPy.

Consignes :
    - executer regulierement le programme dans Spyder ;
    - choisir un backend graphique interactif (Automatic ou Qt) ;
    - redemarrer la console IPython si ce reglage vient d'etre modifie ;
    - conserver plt.show(block=True).

Regles du Jeu de la vie :
    1. Une cellule vivante avec moins de 2 voisines vivantes meurt.
    2. Une cellule vivante avec 2 ou 3 voisines vivantes survit.
    3. Une cellule vivante avec plus de 3 voisines vivantes meurt.
    4. Une cellule morte avec exactement 3 voisines vivantes devient vivante.

Dependances : numpy, matplotlib
===============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# =============================================================================
# PARAMETRES GENERAUX DE LA SIMULATION
# =============================================================================

# Taille de la grille.
NB_LIGNES = 50
NB_COLONNES = 70

# Probabilite qu'une cellule soit vivante dans une grille aleatoire.
PROBABILITE_VIE = 0.25

# Duree entre deux generations, en millisecondes.
INTERVALLE_ANIMATION = 120


# =============================================================================
# CREATION DE LA GRILLE
# =============================================================================

def creer_grille_aleatoire(nb_lignes, nb_colonnes, probabilite_vie=0.25):
    """
    Cree une grille aleatoire de cellules vivantes et mortes.

    Parametres
    ----------
    nb_lignes : int
        Nombre de lignes de la grille.
    nb_colonnes : int
        Nombre de colonnes de la grille.
    probabilite_vie : float
        Probabilite qu'une cellule soit vivante au depart.

    Retour
    ------
    numpy.ndarray
        Tableau 2D contenant des 0 (cellules mortes)
        et des 1 (cellules vivantes).
    """

    # TODO 1 — Tirer une valeur aleatoire entre 0 et 1 pour chaque case.
    # Entrees : nb_lignes et nb_colonnes.
    # Sortie  : tableau de forme (nb_lignes, nb_colonnes).
    valeurs_aleatoires = np.zeros((nb_lignes, nb_colonnes), dtype=float)

    # TODO 2 — Comparer chaque valeur a la probabilite de vie.
    # Le booleen obtenu est converti en entier : False -> 0 et True -> 1.
    grille = np.zeros((nb_lignes, nb_colonnes), dtype=int)

    return grille


def creer_grille_vide(nb_lignes, nb_colonnes):
    """
    Cree une grille entierement vide.

    Parametres
    ----------
    nb_lignes : int
        Nombre de lignes de la grille.
    nb_colonnes : int
        Nombre de colonnes de la grille.

    Retour
    ------
    numpy.ndarray
        Tableau 2D rempli de zeros.
    """

    # Un zero represente une cellule morte.
    return np.zeros((nb_lignes, nb_colonnes), dtype=int)


# =============================================================================
# MOTIFS PREDEFINIS
# =============================================================================

def ajouter_planeur(grille, ligne, colonne):
    """
    Ajoute un planeur ("glider") dans la grille.

    Un planeur est un petit motif de 5 cellules qui se deplace
    diagonalement au fil des generations.

    Parametres
    ----------
    grille : numpy.ndarray
        Grille dans laquelle ajouter le motif.
    ligne : int
        Ligne de depart du motif.
    colonne : int
        Colonne de depart du motif.
    """

    # Coordonnees relatives des cellules vivantes du planeur.
    motif = [
        (0, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]

    # On active chaque cellule du motif.
    for dl, dc in motif:
        l = (ligne + dl) % grille.shape[0]
        c = (colonne + dc) % grille.shape[1]
        grille[l, c] = 1


def ajouter_oscillateur(grille, ligne, colonne):
    """
    Ajoute un oscillateur simple de type "blinker".

    Ce motif alterne entre une ligne horizontale et une ligne verticale.

    Parametres
    ----------
    grille : numpy.ndarray
        Grille dans laquelle ajouter le motif.
    ligne : int
        Ligne centrale du motif.
    colonne : int
        Colonne centrale du motif.
    """

    # Trois cellules vivantes alignees horizontalement.
    for dc in (-1, 0, 1):
        l = ligne % grille.shape[0]
        c = (colonne + dc) % grille.shape[1]
        grille[l, c] = 1


def creer_grille_demo(nb_lignes, nb_colonnes):
    """
    Cree une grille contenant plusieurs motifs faciles a observer.

    Cette configuration est utile pour une demonstration pedagogique :
    on peut suivre des planeurs, des oscillateurs et quelques cellules
    aleatoires dans une meme simulation.

    Parametres
    ----------
    nb_lignes : int
        Nombre de lignes de la grille.
    nb_colonnes : int
        Nombre de colonnes de la grille.

    Retour
    ------
    numpy.ndarray
        Grille initialisee avec plusieurs motifs.
    """

    # On commence avec une grille vide.
    grille = creer_grille_vide(nb_lignes, nb_colonnes)

    # On ajoute deux planeurs a differents endroits.
    ajouter_planeur(grille, 5, 5)
    ajouter_planeur(grille, 15, 25)

    # On ajoute deux oscillateurs.
    ajouter_oscillateur(grille, 10, 45)
    ajouter_oscillateur(grille, 35, 20)

    # On ajoute une petite zone aleatoire dans le coin inferieur droit.
    hauteur_zone = min(12, nb_lignes)
    largeur_zone = min(18, nb_colonnes)

    zone = creer_grille_aleatoire(
        hauteur_zone,
        largeur_zone,
        probabilite_vie=0.30
    )

    grille[
        nb_lignes - hauteur_zone:nb_lignes,
        nb_colonnes - largeur_zone:nb_colonnes
    ] = zone

    return grille


# =============================================================================
# CALCUL DU NOMBRE DE VOISINES VIVANTES
# =============================================================================

def compter_voisines_vivantes(grille, ligne, colonne):
    """
    Compte le nombre de cellules vivantes autour d'une cellule.

    Le voisinage utilise ici les 8 cases autour de la cellule :
    haut, bas, gauche, droite et les 4 diagonales.

    La grille est consideree comme torique :
    sortir a droite revient a gauche, et sortir en haut revient en bas.

    Parametres
    ----------
    grille : numpy.ndarray
        Etat actuel du monde.
    ligne : int
        Ligne de la cellule etudiee.
    colonne : int
        Colonne de la cellule etudiee.

    Retour
    ------
    int
        Nombre de voisines vivantes, compris entre 0 et 8.
    """

    # On memorise la taille de la grille.
    nb_lignes, nb_colonnes = grille.shape

    # Compteur du nombre de voisines vivantes.
    compteur = 0

    # TODO 3 — Parcourir les trois decalages de ligne : -1, 0 et 1.
    # Utiliser directement le tuple (-1, 0, 1).
    for decalage_ligne in ():

        # TODO 4 — Parcourir les trois decalages de colonne : -1, 0 et 1.
        # Utiliser directement le tuple (-1, 0, 1).
        for decalage_colonne in ():

            # TODO 5 — Exclure la cellule centrale de son propre voisinage.
            # Les deux decalages doivent etre nuls en meme temps.
            if False:
                continue

            # TODO 6 — Calculer les coordonnees de la voisine avec le modulo.
            # Rappel : (coordonne + decalage) % taille.
            ligne_voisine = ligne
            colonne_voisine = colonne

            # TODO 7 — Ajouter l'etat 0 ou 1 de la voisine au compteur.
            compteur = compteur

    return int(compteur)


# =============================================================================
# APPLICATION DES REGLES DU JEU DE LA VIE
# =============================================================================

def calculer_generation_suivante(grille):
    """
    Calcule l'etat complet de la grille a la generation suivante.

    Parametres
    ----------
    grille : numpy.ndarray
        Etat actuel de la grille.

    Retour
    ------
    numpy.ndarray
        Nouvelle grille obtenue apres application des regles de Conway.
    """

    # TODO 8 — Creer une grille de zeros ayant la meme forme et le meme type.
    # Utiliser np.zeros_like pour conserver la forme et le type de grille.
    nouvelle_grille = grille.copy()

    # On parcourt toutes les cellules.
    for ligne in range(grille.shape[0]):
        for colonne in range(grille.shape[1]):

            # On compte les voisines vivantes.
            nb_voisines = compter_voisines_vivantes(
                grille,
                ligne,
                colonne
            )

            # Etat actuel de la cellule :
            # 1 = vivante, 0 = morte.
            cellule_vivante = grille[ligne, colonne] == 1

            # -----------------------------------------------------------------
            # Cas 1 : la cellule est vivante.
            # -----------------------------------------------------------------
            if cellule_vivante:

                # TODO 9 — Une cellule vivante survit avec 2 ou 3 voisines.
                # Tester l'appartenance de nb_voisines au tuple (2, 3).
                if cellule_vivante and False:
                    nouvelle_grille[ligne, colonne] = 1

            # -----------------------------------------------------------------
            # Cas 2 : la cellule est morte.
            # -----------------------------------------------------------------
            else:

                # TODO 10 — Une cellule morte nait avec exactement 3 voisines.
                if nb_voisines < 0:
                    nouvelle_grille[ligne, colonne] = 1

    return nouvelle_grille


# =============================================================================
# OUTILS DE MESURE
# =============================================================================

def compter_cellules_vivantes(grille):
    """
    Compte le nombre total de cellules vivantes dans la grille.

    Parametres
    ----------
    grille : numpy.ndarray
        Grille a analyser.

    Retour
    ------
    int
        Nombre de cellules vivantes.
    """

    # TODO 11 — Sommer les 1 de la grille puis convertir le resultat en int.
    # Comme les cellules vivantes valent 1, leur somme donne la population.
    return 0


# =============================================================================
# AFFICHAGE ET ANIMATION
# =============================================================================

def lancer_visualisation(grille_initiale, intervalle=120):
    """
    Lance une visualisation animee du Jeu de la vie.

    La fenetre affiche :
        - la grille principale ;
        - le numero de la generation ;
        - le nombre de cellules vivantes ;
        - une courbe montrant l'evolution de la population.

    Parametres
    ----------
    grille_initiale : numpy.ndarray
        Etat initial du monde.
    intervalle : int
        Temps entre deux generations, en millisecondes.
    """

    # -------------------------------------------------------------------------
    # Etat interne de la simulation.
    # -------------------------------------------------------------------------

    # La grille courante est stockee dans une liste afin de pouvoir
    # la remplacer depuis la fonction d'animation imbriquee.
    etat = {
        "grille": grille_initiale.copy(),
        "generation": 0,
        "historique": [compter_cellules_vivantes(grille_initiale)],
        "pause": False,
    }

    # -------------------------------------------------------------------------
    # Creation de la fenetre.
    # -------------------------------------------------------------------------

    # Deux zones sont affichees :
    # - la simulation a gauche ;
    # - l'evolution de la population a droite.
    figure, (axe_grille, axe_population) = plt.subplots(
        1,
        2,
        figsize=(13, 6),
        gridspec_kw={"width_ratios": [3, 1]}
    )

    # Titre general de la fenetre.
    figure.suptitle(
        "Jeu de la vie de Conway - Simulation",
        fontsize=16
    )

    # -------------------------------------------------------------------------
    # Affichage initial de la grille.
    # -------------------------------------------------------------------------

    image = axe_grille.imshow(
        etat["grille"],
        cmap="binary",
        interpolation="nearest",
        vmin=0,
        vmax=1
    )

    # On masque les graduations car les coordonnees exactes
    # ne sont pas utiles pour cette demonstration.
    axe_grille.set_xticks([])
    axe_grille.set_yticks([])

    # Titre initial.
    titre_grille = axe_grille.set_title(
        f"Generation 0 | Cellules vivantes : {etat['historique'][0]}"
    )

    # -------------------------------------------------------------------------
    # Affichage initial de la courbe de population.
    # -------------------------------------------------------------------------

    ligne_population, = axe_population.plot(
        [0],
        etat["historique"]
    )

    axe_population.set_title("Population")
    axe_population.set_xlabel("Generation")
    axe_population.set_ylabel("Cellules vivantes")
    axe_population.grid(alpha=0.25)

    # Texte d'aide en bas de la fenetre.
    figure.text(
        0.5,
        0.02,
        "Espace : pause / reprise    |    R : nouvelle grille aleatoire",
        ha="center",
        fontsize=10
    )

    # -------------------------------------------------------------------------
    # Gestion du clavier.
    # -------------------------------------------------------------------------

    def gerer_clavier(evenement):
        """
        Gere les interactions clavier avec la simulation.

        Touches :
            ESPACE : met l'animation en pause ou la relance.
            R      : remplace la grille par une nouvelle grille aleatoire.
        """

        # Mise en pause ou reprise de l'animation.
        if evenement.key == " ":
            etat["pause"] = not etat["pause"]

        # Regeneration d'une grille aleatoire.
        elif evenement.key in ("r", "R"):
            etat["grille"] = creer_grille_aleatoire(
                NB_LIGNES,
                NB_COLONNES,
                PROBABILITE_VIE
            )

            # On remet les compteurs a zero.
            etat["generation"] = 0
            etat["historique"] = [
                compter_cellules_vivantes(etat["grille"])
            ]

    # On associe la fonction precedente aux touches du clavier.
    figure.canvas.mpl_connect("key_press_event", gerer_clavier)

    # -------------------------------------------------------------------------
    # Fonction appelee a chaque image de l'animation.
    # -------------------------------------------------------------------------

    def mettre_a_jour(_):
        """
        Met a jour la simulation d'une generation et rafraichit l'affichage.

        Cette fonction est appelee automatiquement par FuncAnimation.
        """

        # Si l'utilisateur a mis le programme en pause,
        # on ne calcule pas de nouvelle generation.
        if not etat["pause"]:

            # Calcul de la generation suivante.
            etat["grille"] = calculer_generation_suivante(
                etat["grille"]
            )

            # Mise a jour du numero de generation.
            etat["generation"] += 1

            # Calcul puis memorisation du nombre de cellules vivantes.
            population = compter_cellules_vivantes(
                etat["grille"]
            )
            etat["historique"].append(population)

        # ---------------------------------------------------------------------
        # Mise a jour de l'image principale.
        # ---------------------------------------------------------------------

        image.set_data(etat["grille"])

        # Mise a jour du titre avec les valeurs actuelles.
        titre_grille.set_text(
            f"Generation {etat['generation']} | "
            f"Cellules vivantes : {etat['historique'][-1]}"
        )

        # ---------------------------------------------------------------------
        # Mise a jour de la courbe de population.
        # ---------------------------------------------------------------------

        generations = list(range(len(etat["historique"])))

        ligne_population.set_data(
            generations,
            etat["historique"]
        )

        # On recalcule automatiquement les limites de la courbe.
        axe_population.relim()
        axe_population.autoscale_view()

        return image, ligne_population, titre_grille

    # -------------------------------------------------------------------------
    # Creation de l'animation.
    # -------------------------------------------------------------------------

    animation = FuncAnimation(
        figure,
        mettre_a_jour,
        interval=intervalle,
        blit=False,
        cache_frame_data=False
    )

    # Ajustement des marges de la fenetre.
    plt.tight_layout(rect=[0, 0.05, 1, 0.93])

    # Affichage de la fenetre.
    plt.show(block=True)

    # Cette ligne evite que certains environnements Python
    # detruisent prematurement l'objet animation.
    return animation


# =============================================================================
# PROGRAMME PRINCIPAL
# =============================================================================

def main():
    """
    Point d'entree principal du programme.

    Cree une grille de demonstration puis lance l'animation.
    """

    # Creation d'une grille contenant plusieurs motifs reconnaissables.
    grille = creer_grille_demo(
        NB_LIGNES,
        NB_COLONNES
    )

    # Lancement de la visualisation.
    lancer_visualisation(
        grille,
        intervalle=INTERVALLE_ANIMATION
    )


# =============================================================================
# EXECUTION DU PROGRAMME
# =============================================================================

# Ce test permet d'executer main() uniquement lorsque le fichier
# est lance directement avec Python.
if __name__ == "__main__":
    main()
