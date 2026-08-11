

# --------- PYODIDE:code --------- #

def dernier(classement):
    ...

# --------- PYODIDE:corr --------- #

def dernier(classement):
    return classement[len(classement) - 1]

# --------- PYODIDE:tests --------- #

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert dernier(classement) == "Laure"

# --------- PYODIDE:secrets --------- #


# tests secrets
classement = ["Robert", "Nadia", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]
assert dernier(classement) == "Steeve"

from random import randrange, sample

prenoms = [
    "Grégoire",
    "Matthieu",
    "Cécile",
    "Clémence",
    "Pierre",
    "Benjamin",
    "Gabriel",
    "Chantal",
    "Dorothée",
    "Cécile",
    "Agathe",
    "Thibault",
    "Amélie",
    "Richard",
    "Georges",
    "Marc",
    "Catherine",
    "Anaïs",
    "Anastasie",
    "Xavier",
    "Michèle",
    "Sylvie",
    "Henri",
    "René",
    "Luc",
    "Rémy",
    "Noël",
    "Nicolas",
    "Gérard",
    "Nathalie",
]
for test in range(10):
    taille = randrange(1, 31)
    classement = sample(prenoms, taille)
    assert dernier(classement) == classement[-1], f"Erreur avec {classement}"