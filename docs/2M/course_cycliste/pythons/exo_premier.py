

# --------- PYODIDE:code --------- #

def premier(classement):
    ...

# --------- PYODIDE:corr --------- #

def premier(classement):
    return classement[0]

# --------- PYODIDE:tests --------- #

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert premier(classement) == "Nadia"

# --------- PYODIDE:secrets --------- #


# tests secrets
classement = ["Robert", "Nadia", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]
assert premier(classement) == "Robert"

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
    assert premier(classement) == classement[0], f"Erreur avec {classement}"