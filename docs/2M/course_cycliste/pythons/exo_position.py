

# --------- PYODIDE:code --------- #

def coureur_en_position(classement, position):
    ...

# --------- PYODIDE:corr --------- #

def coureur_en_position(classement, position):
    return classement[position - 1]

# --------- PYODIDE:tests --------- #

classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert coureur_en_position(classement, 1) == "Nadia"
assert coureur_en_position(classement, 3) == "Thomas"

# --------- PYODIDE:secrets --------- #


# tests secrets
classement = ["Robert", "Nadia", "Eric", "Thomas", "Elizabeth", "Laure", "Steeve"]
assert coureur_en_position(classement, 4) == "Thomas"


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
    position = randrange(1, taille + 1)
    assert (
        coureur_en_position(classement, position) == classement[position - 1]
    ), f"Erreur avec {classement = } et {position = }"