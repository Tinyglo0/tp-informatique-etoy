

# --------- PYODIDE:code --------- #

def depasse(classement, place):
    ...

# --------- PYODIDE:corr --------- #

def depasse(classement, place):
    indice_coureur = place - 1
    indice_precedent = indice_coureur - 1
    coureur_precedent = classement[indice_precedent]
    classement[indice_precedent] = classement[indice_coureur]
    classement[indice_coureur] = coureur_precedent

# --------- PYODIDE:tests --------- #

classement_actuel = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
depasse(classement_actuel, 3)
assert classement_actuel == ["Nadia", "Thomas", "Franck", "Elizabeth", "Laure"]
depasse(classement_actuel, 2)
assert classement_actuel == ["Thomas", "Nadia", "Franck", "Elizabeth", "Laure"]

# --------- PYODIDE:secrets --------- #

from random import randint

# Tests
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
depasse(classement, 3)
assert classement == ["Nadia", "Thomas", "Franck", "Elizabeth", "Laure"]
depasse(classement, 2)
assert classement == ["Thomas", "Nadia", "Franck", "Elizabeth", "Laure"]

# Autres tests
classement = ["Robert", "Nadia", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]
depasse(classement, 2)
assert classement == ["Nadia", "Robert", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]

taille = randint(10, 20)
tableau_1 = [str(i) for i in range(taille)]
tableau_2 = [str(i) for i in range(taille)]
n = randint(2, taille)
depasse(tableau_1, n)
tableau_2[n - 1], tableau_2[n - 2] = tableau_2[n - 2], tableau_2[n - 1]
assert tableau_1 == tableau_2
