# --- PYODIDE:env --- #
from random import random
from copy import deepcopy
import p5, traceback

# Réglage affichage
COULEUR_BLANC = (255, 255, 255)
COULEUR_GRIS = (129, 129, 129)
COULEUR_GRILLE = (126, 86, 194)
COULEUR_FOURMI = (255, 0, 0)
COULEUR_TEXTE = (0, 0, 255)
TAILLE_CELLULE = 25
FPS = 40

# Réglages du jeu
LARGEUR = 35
HAUTEUR = 5
BLANC = True
GRIS = False
HAUT = 0
DROITE = 1
BAS = 2
GAUCHE = 3
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
fourmi = (0, 0, DROITE)
grille_depart = [[False, True, True, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, True, True, False, False, True, False, True, True, False, True, False, False, False, True], [True, True, True, False, False, False, False, True, False, True, True, False, False, True, True, False, True, False, True, False, False, True, False, False, True, True, True, False, True, True, False, False, True, False, False], [False, True, False, True, True, True, False, False, True, True, True, False, True, False, True, False, True, False, True, False, True, False, False, True, False, True, False, False, True, False, False, True, False, True, True], [True, False, True, True, False, False, False, False, False, False, True, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, False, True, False, False, True, False, False, False], [True, False, False, False, True, True, False, True, True, False, True, True, False, False, False, False, True, False, False, True, True, True, True, False, False, True, False, True, True, True, False, True, False, False, True]]
grille = deepcopy(grille_depart)
DONE_ANIM = False

def dessine_grille(grille):
    largeur = len(grille[0])
    hauteur = len(grille)
    p5.strokeWeight(1)
    p5.stroke(*COULEUR_GRILLE)
    for i in range(hauteur):
        for j in range(largeur):
            couleur = COULEUR_BLANC if grille[i][j] == BLANC else COULEUR_GRIS
            p5.fill(*couleur)
            p5.rect(
                j * TAILLE_CELLULE, i * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE
            )


def dessine_fourmi(x, y, o):
    """
    Code adapté à partir de celui de N. Weibel
    """
    p5.fill(*COULEUR_FOURMI)
    p5.stroke(*COULEUR_FOURMI)
    p5.push()
    p5.translate(
        x * TAILLE_CELLULE + TAILLE_CELLULE // 2,
        y * TAILLE_CELLULE + TAILLE_CELLULE // 2,
    )
    p5.rotate(o * p5.PI / 2 - p5.PI / 2)
    # dessin de la fourmi
    pas = TAILLE_CELLULE // 8
    # les pattes et antennes
    p5.line(0, 2 * pas, 0, -2 * pas)
    p5.line(-2 * pas, -2 * pas, -pas // 3, 0)
    p5.line(-2 * pas, 2 * pas, -pas // 3, 0)
    p5.line(2 * pas, -2 * pas, pas // 3, 0)
    p5.line(2 * pas, 2 * pas, pas // 3, 0)
    p5.line(2 * pas, 0, 3 * pas, -pas)
    p5.line(2 * pas, 0, 3 * pas, pas)
    # le corps
    p5.noStroke()
    p5.ellipse(0, 0, TAILLE_CELLULE // 3, pas)
    p5.ellipse(-2 * pas, 0, 2 * pas, TAILLE_CELLULE // 6)
    p5.ellipse(2 * pas, 0, TAILLE_CELLULE // 6, TAILLE_CELLULE // 6)
    p5.pop()


def affiche_etape():
    p5.textSize(36)
    p5.fill(*COULEUR_TEXTE)
    p5.noStroke()
    p5.text(p5.frameCount, 0, HAUTEUR * TAILLE_CELLULE)


def initialisation():
    p5.createCanvas(LARGEUR * TAILLE_CELLULE, HAUTEUR * TAILLE_CELLULE)
    p5.frameRate(FPS)
    dessine_grille(grille)
    dessine_fourmi(x, y, o)
    affiche_etape()


def dessine():
    global fourmi, DONE_ANIM
    try:
        fourmi = etape(*fourmi)
        dessine_grille(grille)
        dessine_fourmi(*fourmi)
        affiche_etape()
        if p5.frameCount >= nb_etapes:
            p5.noLoop()
            DONE_ANIM = True
    except:
        DONE_ANIM = True
        terminal_message('oopsy', traceback.format_exc(), format='error')
        raise


def lance_simulation():
    global fourmi
    fourmi = (x, y, o)
    p5.run(initialisation, dessine, target="langton")


def avance(x, y, o):
    di, dj = DIRS[o]
    x = (x + dj) % LARGEUR
    y = (y + di) % HAUTEUR
    return x, y


def gauche(o):
    o = (o - 1) % 4
    return o


def droite(o):
    o = (o + 1) % 4
    return o


def retourne_tuile(x, y):
    grille[y][x] = GRIS if grille[y][x] == BLANC else BLANC


def couleur_tuile(x, y):
    return grille[y][x]


# --- PYODIDE:code --- #
# Réglages initiaux
x = ...
y = ...
o = ...
nb_etapes = ...

# Simulation d'une étape
def etape(x, y, o):
    c = couleur_tuile(...)
    if ... == ...:  # BLANC ou GRIS
        ... = ...
    else:
        ...
    ...(...)
    ... = avance(...)
    return ...

FPS = 60  # images par seconde, diminuer pour ralentir l'animation
lance_simulation()  # NE PAS MODIFIER
# --- PYODIDE:corr --- #
# Réglages initiaux
x = 28
y = 0
o = GAUCHE
nb_etapes = 500


# Simulation d'une étape
def etape(x, y, o):
    if couleur_tuile(x, y) == BLANC:
        o = droite(o)
    else:
        o = gauche(o)
    retourne_tuile(x, y)
    x, y = avance(x, y, o)
    return x, y, o


# Lance la simulation
lance_simulation()


# --- PYODIDE:secrets --- #
@auto_run
async def _():
    import js, p5

    while not DONE_ANIM and p5.isLooping():
        await js.sleep(100)

    attendu = [
        [True, False, False, False, False, False, True, False, False, False, True, False, False, False, True, False, False, True, True, True, False, False, True, True, True, False, False, True, False, False, True, False, False, False, True],
        [True, False, False, False, False, True, False, True, False, False, True, True, False, False, True, False, True, False, False, False, False, False, False, True, False, False, True, False, True, False, True, True, False, False, True],
        [True, False, False, False, False, True, True, True, False, False, True, False, True, False, True, False, True, False, True, True, True, False, False, True, False, False, True, False, True, False, True, False, True, False, True],
        [True, False, False, False, True, False, False, False, True,False, True, False, False, True, True, False, True, False, False, True, False, False, False, True, False, False, True, False, True, False, True, False,False, True, True],
        [True, True, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, True, True, True, False, False, False, True, False, False, False, True, False, False, True, False, False, False, True],
    ]
    assert grille == attendu, "La grille finale n'est pas égale à celle attendue"
