# --------- PYODIDE:env --------- #
def afficher_grille(g):
    for ligne in g:
        print("".join(str(x) for x in ligne))

# --------- PYODIDE:code --------- #
# Configuration 1
grille = [[0]*15 for i in range(10)] # initialisation à 0 des 150 éléments de la grille

# Modifiez la grille ci-dessous (6 instructions) :
# grille[...][...] = 1 ...

afficher_grille(grille)

# --------- PYODIDE:corr --------- #
grille = [[0]*15 for i in range(10)] 

grille[3][6] = 1
grille[3][9] = 1
grille[5][6] = 1
grille[5][9] = 1
grille[6][7] = 1
grille[6][8] = 1

afficher_grille(grille)

# --------- PYODIDE:secrets --------- #
assert grille[3][6] == 1, "La case (3, 6) n'est pas à 1"
assert grille[3][9] == 1, "La case (3, 9) n'est pas à 1"
assert grille[5][6] == 1, "La case (5, 6) n'est pas à 1"
assert grille[5][9] == 1, "La case (5, 9) n'est pas à 1"
assert grille[6][7] == 1, "La case (6, 7) n'est pas à 1"
assert grille[6][8] == 1, "La case (6, 8) n'est pas à 1"

# Vérifier que les autres cases sont toujours à 0
total_un = sum(sum(ligne) for ligne in grille)
assert total_un == 6, "D'autres cases (en trop) ont été modifiées !"
