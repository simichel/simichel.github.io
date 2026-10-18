"""
===============================================================================
Projet : Fourmis et pheromones
Auteur : Sixtine MICHEL
Date de creation : 24/09/2026

Description :
    Mini-TP guide sur un principe simple d'intelligence collective.

    Completer les TODO dans l'ordre, puis executer le programme avec Spyder.
    Choisir un backend graphique interactif (Automatic ou Qt), redemarrer la
    console IPython si necessaire, puis conserver plt.show(block=True).

    Des fourmis cherchent une source de nourriture :
        - elles explorent le monde ;
        - lorsqu'elles trouvent de la nourriture, elles retournent au nid ;
        - elles deposent des pheromones sur leur chemin ;
        - les autres fourmis ont tendance a suivre les zones odorantes ;
        - les pheromones s'evaporent progressivement.

    Aucun individu ne connait le chemin optimal, mais un comportement collectif
    peut emerger au cours du temps.

Dependances :
    - numpy
    - matplotlib

Execution :
    python 04-fourmis_pheromones.py
===============================================================================
"""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D


# =============================================================================
# PARAMETRES
# =============================================================================

# Largeur et hauteur du monde carre.
TAILLE = 80
# Nombre de fourmis simulees.
NB_FOURMIS = 70
# Coordonnees du nid et de la source de nourriture.
NID = np.array([10.0, 10.0])
NOURRITURE = np.array([68.0, 65.0])

# Distances auxquelles le nid et la nourriture sont consideres atteints.
RAYON_NID = 4.0
RAYON_NOURRITURE = 5.0

# Distance parcourue par une fourmi en une etape.
VITESSE = 1.0
# Intensite du mouvement aleatoire hors d'une piste de pheromones.
BRUIT_DIRECTION = 0.65
# Intensite du mouvement aleatoire lorsqu'une piste est suivie.
BRUIT_SUR_PISTE = 0.15
# Poids de l'attraction exercee par les pheromones.
FORCE_PHEROMONE = 0.8
# Force qui eloigne du nid une fourmi venant de livrer sa nourriture.
FORCE_ELOIGNEMENT_NID = 1.2
# Distance autour du nid dans laquelle cet eloignement est actif.
RAYON_ELOIGNEMENT_NID = 10.0
# Duree pendant laquelle la fourmi se souvient de son trajet retour.
NB_PAS_MEMOIRE_RETOUR = 80
# Quantite de pheromones disponible au debut du trajet retour.
DEPOT_PHEROMONE = 8.0
# Facteur de diminution du depot a chaque etape.
DECROISSANCE_DEPOT = 0.97
# Fraction de pheromones conservee entre deux etapes.
EVAPORATION = 0.995
# Part des pheromones diffusee vers les cases voisines.
DIFFUSION = 0.08
# Duree entre deux images de l'animation, en millisecondes.
INTERVALLE_ANIMATION = 45
# Rayon, en cases, dans lequel une fourmi detecte les pheromones.
RAYON_DETECTION = 3


# =============================================================================
# CREATION DES FOURMIS
# =============================================================================

def creer_fourmis():
    """
    Cree les fourmis au niveau du nid.

    Retour
    ------
    dict
        Positions, directions et etat de transport de nourriture.
    """

    # Toutes les fourmis commencent pres du nid.
    positions = np.tile(NID, (NB_FOURMIS, 1))
    positions += np.random.normal(0, 1.0, size=(NB_FOURMIS, 2))

    # Directions initiales aleatoires.
    # TODO 1 — Creer NB_FOURMIS directions initiales aleatoires.
    # Tirer les angles entre 0 et 2*pi, puis former les vecteurs (cos, sin).
    # Sortie : directions, tableau de forme (NB_FOURMIS, 2).
    angles = np.zeros(NB_FOURMIS)
    directions = np.zeros((NB_FOURMIS, 2))

    # False : la fourmi cherche de la nourriture.
    # True  : la fourmi ramene de la nourriture au nid.
    transporte = np.zeros(NB_FOURMIS, dtype=bool)

    # Quantite encore disponible pour marquer le chemin du retour. Elle sera
    # maximale a la nourriture puis diminuera en direction du nid.
    reserve_pheromone = np.zeros(NB_FOURMIS, dtype=float)

    # Apres une livraison, la fourmi conserve temporairement le cap oppose a
    # son trajet retour. Les pheromones continuent a corriger ce cap.
    pas_memoire_retour = np.zeros(NB_FOURMIS, dtype=int)

    return {
        "positions": positions,
        "directions": directions,
        "transporte": transporte,
        "reserve_pheromone": reserve_pheromone,
        "pas_memoire_retour": pas_memoire_retour,
        "livraisons": 0,
    }


# =============================================================================
# CHAMP DE PHEROMONES
# =============================================================================

def creer_champ_pheromones():
    """
    Cree un champ de pheromones vide.

    Retour
    ------
    numpy.ndarray
        Tableau 2D initialement nul.
    """

    return np.zeros((TAILLE, TAILLE), dtype=float)


def diffuser_et_evaporer(champ):
    """
    Diffuse legerement les pheromones puis les fait evaporer.

    Parametres
    ----------
    champ : numpy.ndarray
        Champ de pheromones modifie sur place.
    """

    # Diffusion tres simple : moyenne avec les quatre voisins.
    # TODO 2 — Calculer la moyenne des quatre cases voisines.
    # Utiliser np.roll selon les deux axes, dans les deux sens.
    # Sortie : un tableau de meme forme que champ.
    moyenne_voisins = np.zeros_like(champ)

    # Melange entre le champ actuel et le champ diffuse.
    # TODO 3 — Diffuser puis evaporer les pheromones.
    # Diffusion : (1-DIFFUSION)*champ + DIFFUSION*moyenne_voisins.
    # Evaporation : multiplier ensuite tout le champ par EVAPORATION.
    champ[:] = champ


# =============================================================================
# DEPLACEMENT D'UNE FOURMI
# =============================================================================

def direction_vers(cible, position):
    """
    Retourne un vecteur unitaire dirige vers une cible.
    """

    # TODO 4 — Construire cible - position.
    # Sortie : vecteur de forme (2,).
    vecteur = np.zeros(2)
    norme = np.linalg.norm(vecteur)

    if norme == 0:
        return np.zeros(2)

    # TODO 5 — Renvoyer le vecteur unitaire vecteur / norme.
    return np.zeros(2)


def direction_pheromone(champ, position):
    """
    Estime la direction locale vers les pheromones les plus fortes.

    Parametres
    ----------
    champ : numpy.ndarray
        Champ de pheromones.
    position : numpy.ndarray
        Position continue de la fourmi.

    Retour
    ------
    numpy.ndarray
        Vecteur indiquant approximativement la direction la plus odorante.
    """

    x = int(np.clip(position[0], RAYON_DETECTION, TAILLE - RAYON_DETECTION - 1))
    y = int(np.clip(position[1], RAYON_DETECTION, TAILLE - RAYON_DETECTION - 1))

    # Gradient discret lisse : la fourmi compare la concentration moyenne de
    # deux petites zones opposees. Cette moyenne evite les changements de cap
    # provoques par une piste diagonale repartie sur plusieurs cellules.
    r = RAYON_DETECTION

    # TODO 6 — Approcher le gradient par differences de moyennes.
    # gx compare les zones a droite et a gauche ; gy, haut et bas.
    # Chaque zone s'etend jusqu'a r = RAYON_DETECTION cases.
    gx = 0.0
    gy = 0.0

    vecteur = np.array([gx, gy], dtype=float)
    norme = np.linalg.norm(vecteur)

    if norme == 0:
        return np.zeros(2)

    # TODO 7 — Renvoyer le gradient unitaire vecteur / norme.
    return np.zeros(2)


def deplacer_fourmis(fourmis, champ):
    """
    Met a jour la position et le comportement de toutes les fourmis.

    Parametres
    ----------
    fourmis : dict
        Etat des fourmis.
    champ : numpy.ndarray
        Champ de pheromones.
    """

    positions = fourmis["positions"]
    directions = fourmis["directions"]
    transporte = fourmis["transporte"]
    reserve_pheromone = fourmis["reserve_pheromone"]
    pas_memoire_retour = fourmis["pas_memoire_retour"]

    for i in range(NB_FOURMIS):

        position = positions[i]

        # ---------------------------------------------------------------------
        # Choix de direction selon l'etat de la fourmi.
        # ---------------------------------------------------------------------

        if transporte[i]:
            # Une fourmi chargee revient globalement vers le nid.
            # TODO 8 — Orienter une fourmi chargee vers le nid.
            # Calculer la direction du nid, puis lui ajouter un bruit gaussien
            # de forme (2,) dont le poids vaut 0.25.
            cible = np.zeros(2)
            bruit = np.zeros(2)
            nouvelle_direction = directions[i].copy()

        else:
            if pas_memoire_retour[i] > 0:
                # Apres une livraison, elle repart a l'oppose de son arrivee.
                # Le gradient odorant corrige doucement le cap memorise.
                odeur = direction_pheromone(champ, position)
                nouvelle_direction = (
                    directions[i]
                    + 0.25 * FORCE_PHEROMONE * odeur
                )
                pas_memoire_retour[i] -= 1

            else:
                # Une fourmi qui cherche de la nourriture est influencee par
                # les pheromones et par un mouvement aleatoire.
                odeur = direction_pheromone(champ, position)
                intensite_bruit = (
                    BRUIT_SUR_PISTE
                    if np.linalg.norm(odeur) > 0
                    else BRUIT_DIRECTION
                )
                bruit = np.random.normal(0, intensite_bruit, 2)

                # TODO 9 — Combiner inertie, pheromones et exploration.
                # Somme attendue : direction actuelle
                # + FORCE_PHEROMONE*odeur + bruit.
                nouvelle_direction = directions[i].copy()

            # Une fourmi qui vient de livrer sa nourriture doit quitter la
            # zone du nid. Elle repart d'abord vers l'exterieur, puis les
            # pheromones prennent progressivement le relais.
            distance_nid = np.linalg.norm(position - NID)

            if distance_nid < RAYON_ELOIGNEMENT_NID:
                eloignement = direction_vers(position, NID)
                intensite = 1 - distance_nid / RAYON_ELOIGNEMENT_NID
                # TODO 10 — Ajouter la repulsion du nid.
                # Ajouter FORCE_ELOIGNEMENT_NID*intensite*eloignement.
                nouvelle_direction += np.zeros(2)

        # Normalisation.
        norme = np.linalg.norm(nouvelle_direction)

        if norme > 0:
            nouvelle_direction /= norme

        # TODO 11 — Memoriser la nouvelle direction unitaire.
        # Remplacer la direction i par nouvelle_direction.
        directions[i] = directions[i]

        # ---------------------------------------------------------------------
        # Deplacement.
        # ---------------------------------------------------------------------

        positions[i] += VITESSE * directions[i]

        # TODO 12 — Completer les conditions des quatre rebonds.
        if False:
            positions[i, 0] = 1
            directions[i, 0] = -directions[i, 0]

        if False:
            positions[i, 0] = TAILLE - 2
            directions[i, 0] = -directions[i, 0]

        if False:
            positions[i, 1] = 1
            directions[i, 1] = -directions[i, 1]

        if False:
            positions[i, 1] = TAILLE - 2
            directions[i, 1] = -directions[i, 1]

        # ---------------------------------------------------------------------
        # Interaction avec nourriture et nid.
        # ---------------------------------------------------------------------

        if (
            not transporte[i]
            and np.linalg.norm(positions[i] - NOURRITURE)
            < RAYON_NOURRITURE
        ):
            # TODO 13 — Prendre la nourriture et initialiser le depot.
            # Passer transporte[i] a True, charger DEPOT_PHEROMONE et orienter
            # immediatement la fourmi vers le nid.
            transporte[i] = False
            reserve_pheromone[i] = 0.0

            # La fourmi repart immediatement dans le sens oppose. Sans ce
            # demi-tour, elle continue quelques instants vers la nourriture
            # et plusieurs fourmis finissent par se superposer autour de la
            # source.
            directions[i] = directions[i]

        elif (
            transporte[i]
            and np.linalg.norm(positions[i] - NID)
            < RAYON_NID
        ):
            # TODO 14 — Livrer, compter puis repartir vers l'exterieur.
            # Retirer la charge et la reserve, incrementer les livraisons,
            # inverser la direction et initialiser la memoire du retour.
            transporte[i] = transporte[i]
            reserve_pheromone[i] = reserve_pheromone[i]

            # La direction d'arrivee pointe vers le nid. On l'inverse pour
            # que la fourmi reparte le long de la piste qu'elle vient de
            # renforcer, au lieu de rester a tourner autour du nid.
            directions[i] = directions[i]
            pas_memoire_retour[i] = 0

        # ---------------------------------------------------------------------
        # Depot de pheromones.
        # ---------------------------------------------------------------------

        # On depose surtout des pheromones lors du retour vers le nid.
        if transporte[i]:
            x = int(np.clip(positions[i, 0], 0, TAILLE - 1))
            y = int(np.clip(positions[i, 1], 0, TAILLE - 1))
            # TODO 15 — Deposer la reserve puis la faire decroitre.
            # Ajouter reserve_pheromone[i] dans champ[x, y], puis multiplier
            # cette reserve par DECROISSANCE_DEPOT.
            champ[x, y] = champ[x, y]
            reserve_pheromone[i] = reserve_pheromone[i]


# =============================================================================
# VISUALISATION
# =============================================================================

def lancer_visualisation():
    """
    Lance la simulation des fourmis et des pheromones.
    """

    fourmis = creer_fourmis()
    champ = creer_champ_pheromones()

    figure, axe = plt.subplots(figsize=(8, 8))
    figure.suptitle(
        "Intelligence collective : fourmis et pheromones",
        fontsize=15
    )

    # Le champ de pheromones est affiche en fond.
    image = axe.imshow(
        champ.T,
        origin="lower",
        cmap="magma",
        vmin=0,
        vmax=6,
        extent=[0, TAILLE, 0, TAILLE],
        interpolation="bilinear"
    )

    # Fourmis.
    nuage = axe.scatter(
        fourmis["positions"][:, 0],
        fourmis["positions"][:, 1],
        c=fourmis["transporte"].astype(int),
        cmap="cool",
        vmin=0,
        vmax=1,
        s=18
    )

    # Nid et nourriture.
    symbole_nid = axe.scatter(
        [NID[0]],
        [NID[1]],
        s=350,
        marker="s",
        label="Nid"
    )

    symbole_nourriture = axe.scatter(
        [NOURRITURE[0]],
        [NOURRITURE[1]],
        s=350,
        marker="*",
        label="Nourriture"
    )

    axe.set_xlim(0, TAILLE)
    axe.set_ylim(0, TAILLE)
    axe.set_aspect("equal")
    axe.set_xlabel("x")
    axe.set_ylabel("y")

    # Entrees explicites pour expliquer la couleur des fourmis.
    palette_fourmis = plt.get_cmap("cool")
    symbole_recherche = Line2D(
        [],
        [],
        marker="o",
        linestyle="none",
        markerfacecolor=palette_fourmis(0.0),
        markeredgecolor="none",
        markersize=7,
        label="Fourmi en recherche"
    )
    symbole_chargee = Line2D(
        [],
        [],
        marker="o",
        linestyle="none",
        markerfacecolor=palette_fourmis(1.0),
        markeredgecolor="none",
        markersize=7,
        label="Fourmi avec nourriture"
    )

    axe.legend(
        handles=[
            symbole_nid,
            symbole_nourriture,
            symbole_recherche,
            symbole_chargee,
        ],
        loc="upper left"
    )

    texte = axe.text(
        0.02,
        0.02,
        "",
        transform=axe.transAxes,
        bbox={"facecolor": "white", "alpha": 0.8}
    )

    def mettre_a_jour(frame):
        """
        Calcule une generation puis rafraichit l'affichage.
        """

        # Evolution du champ.
        diffuser_et_evaporer(champ)

        # Evolution des fourmis.
        deplacer_fourmis(fourmis, champ)

        # Mise a jour du fond.
        image.set_data(champ.T)

        # Ajustement de l'echelle visuelle.
        maximum = max(1.0, float(np.percentile(champ, 99.5)))
        image.set_clim(0, maximum)

        # Mise a jour des fourmis.
        nuage.set_offsets(fourmis["positions"])
        nuage.set_array(fourmis["transporte"].astype(float))

        # Petit indicateur pedagogique.
        nb_chargees = int(np.sum(fourmis["transporte"]))
        texte.set_text(
            f"Generation : {frame}\n"
            f"Fourmis avec nourriture : {nb_chargees}\n"
            f"Nourritures deposees au nid : {fourmis['livraisons']}"
        )

        return image, nuage, texte

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
