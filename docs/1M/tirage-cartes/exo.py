# --------- PYODIDE:code --------- #
from ...
    
def nb_tirages_as():
    nb_tirages = ...
    carte = ...
    while carte > 4: # les cartes du jeu sont assimilées à des nombres entiers...
        nb_tirages = ...
        carte = randint(...,...)
    return ...

# --------- PYODIDE:env --------- #
from random import randint

# --------- PYODIDE:corr --------- #
from random import randint

def nb_tirages_as():
    nb_tirages = 1
    # On assimile les cartes à des nombres de 1 à 32. Les As sont 1, 2, 3, 4.
    carte = randint(1, 32)
    while carte > 4:
        nb_tirages += 1
        carte = randint(1, 32)
    return nb_tirages

# --------- PYODIDE:tests --------- #
resultat = nb_tirages_as()
assert isinstance(resultat, int) and resultat > 0
