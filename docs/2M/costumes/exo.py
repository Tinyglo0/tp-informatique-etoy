

# --------- PYODIDE:code --------- #

def costume(rang, couleurs):
    ...

# --------- PYODIDE:corr --------- #

def costume(rang, couleurs):
    n = len(couleurs)
    indice = (rang - 1) % n
    return couleurs[indice]

# --------- PYODIDE:tests --------- #

assert costume(2, ["bleu", "blanc", "rouge"]) == "blanc"
assert costume(8, ["rose", "vert", "orange", "bleu"]) == "bleu"

# --------- PYODIDE:secrets --------- #

from random import randrange


def costume_corr(rang, couleurs):
    n = len(couleurs)
    indice = (rang - 1) % n
    return couleurs[indice]



assert costume(1, ["bleu", "blanc", "rouge"]) == "bleu"
assert costume(3, ["bleu", "blanc", "rouge"]) == "rouge"
assert costume(8, ["bleu", "blanc", "rouge"]) == "blanc"
assert costume(1000, ["bleu", "blanc", "rouge"]) == "bleu"
assert costume(300, ["bleu", "blanc", "rouge"]) == "rouge"
# Tests supplémentaires
for _ in range(10):
    nb_couleurs = randrange(5, 20)
    couleurs = [tuple(randrange(0, 256) for _ in range(3)) for _ in range(nb_couleurs)]
    rang = randrange(1, 3 * nb_couleurs)
    attendu = costume_corr(rang, couleurs)
    assert (
        costume(rang, couleurs) == attendu
    ), f"Erreur avec une liste de {nb_couleurs} couleurs et le rang {rang}"