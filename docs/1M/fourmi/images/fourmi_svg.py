# --- PYODIDE:env --- #
import drawsvg as draw
from random import random

# Affichage
TAILLE_CELLULE = 25
BLANC = True
GRIS = False
COULEURS = {
    BLANC: "#fff",
    GRIS: "#777",
}
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3

# Réglages du jeu
LARGEUR = 35
HAUTEUR = 5
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
orientation = HAUT  # à l'envers
orientation = BAS  # à l'endroit

grille_01 = [
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1, 0,0,1,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0, 0,1,0,1,0,1,1,0,0,1],
    [1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0, 0,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0, 0,1,0,1,0,1,0,0,1,1],
    [1,1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0, 0,0,1,0,0,1,0,0,0,1],
]
grille_attendue = [[bool(b) for b in ligne] for ligne in grille_01]
grille_depart = [[True, True, False, True, False, True, False, False, False, False, False, True, True, True, False, False, False, False, True, True, False, True, 
True, False, False, False, True, False, False, False, True, False, False, True, True], [False, False, True, True, False, True, False, False, True, True, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, True, True, True, False, True, 
True, False, True, True], [True, False, False, True, False, False, False, False, True, True, True, False, False, False, True, False, True, True, True, False, False, True, False, False, False, True, False, False, False, True, True, False, False, True, False], [False, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, True, True, True, True, True, False, True, True, True, False, False, False, False, True, False, False, False, True, False], [True, False, False, True, True, False, False, False, True, True, True, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, True, True, True]] 

def dessine_svg(grille, couleurs, nom):
    figure = draw.Drawing(LARGEUR * TAILLE_CELLULE, HAUTEUR * TAILLE_CELLULE)
    for i in range(HAUTEUR):
        for j in range(LARGEUR):
            c = couleurs[grille[i][j]]
            figure.append(
                draw.Rectangle(
                    j * TAILLE_CELLULE,
                    i * TAILLE_CELLULE,
                    TAILLE_CELLULE,
                    TAILLE_CELLULE,
                    fill=c,
                )
            )

    for i in range(HAUTEUR + 1):
        figure.append(
            draw.Line(
                0,
                i * TAILLE_CELLULE,
                LARGEUR * TAILLE_CELLULE,
                i * TAILLE_CELLULE,
                stroke_width=1,
                stroke="#7e56c2",
            )
        )
    for j in range(LARGEUR + 1):
        figure.append(
            draw.Line(
                j * TAILLE_CELLULE,
                0,
                j * TAILLE_CELLULE,
                HAUTEUR * TAILLE_CELLULE,
                stroke_width=1,
                stroke="#7e56c2",
            )
        )
    figure.save_svg(f"{nom}.svg")


def grille_aleatoire(largeur, hauteur, proba_vie):
    return [
        [BLANC if random() < proba_vie else GRIS for _ in range(largeur)]
        for _ in range(hauteur)
    ]


def avance(x, y, orientation):
    di, dj = DIRS[orientation]
    x = (x + dj) % LARGEUR
    y = (y + di) % HAUTEUR
    return x, y


def gauche(orientation):
    return (orientation - 1) % 4


def droite(orientation):
    return (orientation + 1) % 4


def retourne_tuile(x, y):
    grille[y][x] = not grille[y][x]


def couleur_case(x, y):
    return grille[y][x]


def une_etape(x, y, orientation):
    if couleur_case(x, y) == BLANC:
        orientation = droite(orientation)
    else:
        orientation = gauche(orientation)
    retourne_tuile(x, y)
    x, y = avance(x, y, orientation)
    return x, y, orientation


def une_etape_envers(x, y, orientation):
    x, y = avance(x, y, orientation)
    retourne_tuile(x, y)
    if couleur_case(x, y) == BLANC:
        orientation = gauche(orientation)
    else:
        orientation = droite(orientation)
    return x, y, orientation


def n_etapes(x, y, orientation, nb_etapes):
    for _ in range(nb_etapes):
        x, y, orientation = f_mode[mode](x, y, orientation)
    return x, y, orientation


# La position initiale
nb_etapes = 500
grille = grille_attendue
x = LARGEUR // 2
y = HAUTEUR // 2
# x = 23
# y = 0
orientation = DROITE
mode = "envers"
f_mode = {
    "endroit": une_etape,
    "envers": une_etape_envers,
}

dessine_svg(grille, COULEURS, "langton")
x, y, orientation = n_etapes(x, y, orientation, nb_etapes)
dessine_svg(grille, COULEURS, "depart")
print(x, y, orientation)
print(grille)
# l'orientation de départ vaut (orientation + 2) % 4
mode = "endroit"
x, y, orientation = n_etapes(x, y, (orientation + 2) % 4, nb_etapes)
dessine_svg(grille, COULEURS, "langton_bis")

