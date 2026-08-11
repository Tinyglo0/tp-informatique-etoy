

# --------- PYODIDE:code --------- #

def nombre_coureurs(classement):
    ...

# --------- PYODIDE:corr --------- #

def nombre_coureurs(classement):
    return len(classement)

# --------- PYODIDE:tests --------- #

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5

# --------- PYODIDE:secrets --------- #


# tests secrets
classement = ["Robert", "Nadia", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]
assert nombre_coureurs(classement) == 7

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
    assert nombre_coureurs(classement) == taille, f"Erreur avec {classement}"