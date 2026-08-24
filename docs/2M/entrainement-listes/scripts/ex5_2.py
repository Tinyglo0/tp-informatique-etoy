# --------- PYODIDE:env --------- #
def afficher_grille(g):
    for ligne in g:
        print("".join(str(x) for x in ligne))

# --------- PYODIDE:code --------- #
# Configuration 2
grille = [[0]*15 for i in range(10)] # initialisation à 0 des 150 éléments de la grille

# Modifiez la grille ci-dessous à l'aide de boucles :
# ...

afficher_grille(grille)

# --------- PYODIDE:corr --------- #
grille = [[0]*15 for i in range(10)] 

for i in range(10):
    for j in range(15):
        if (i < 10 and j < 10 and j>0) and (j == 1 or j ==9 or i== 0 or i == 9):
            grille[i][j] = 1

for i in range(7):
    for j in range(7):
        if (i == j):
            grille[i+1][j+2] = 1
            
afficher_grille(grille)

# --------- PYODIDE:secrets --------- #
grille_attendue = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

assert grille == grille_attendue, "La grille générée ne correspond pas au modèle demandé (Configuration 3)"
