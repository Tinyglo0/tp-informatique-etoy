# --- exo, nombre --- #
def nombre_coureurs(classement):
    ...


# --- exo, premier --- #
def premier(classement):
    ...


# --- exo, dernier --- #
def dernier(classement):
    ...


# --- exo, position --- #
def coureur_en_position(classement, position):
    ...


# --- corr, nombre --- #
def nombre_coureurs(classement):
    return len(classement)


# --- corr, premier --- #
def premier(classement):
    return classement[0]


# --- corr, dernier --- #
def dernier(classement):
    return classement[len(classement) - 1]


# --- corr, position --- #
def coureur_en_position(classement, position):
    return classement[position - 1]


# --- tests, nombre --- #
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert nombre_coureurs(classement) == 5
# --- tests, premier --- #
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert premier(classement) == "Nadia"
# --- tests, dernier --- #
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert dernier(classement) == "Laure"
# --- tests, position --- #
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
assert coureur_en_position(classement, 1) == "Nadia"
assert coureur_en_position(classement, 3) == "Thomas"
# --- secrets, nombre --- #
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
# --- secrets, premier --- #
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
# --- secrets, dernier --- #
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
# --- secrets, position --- #
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
# --- REM, dernier --- #
""" # skip
On pouvait également opter pour la solution suivante :

```python
def dernier(classement):
    taille = nombre_coureurs(classement)  # renvoie len(classement)
    return classement[taille - 1]
```

Dans ce cas, Python autorise un raccourci. Au lieu d'indiquer l'indice `#!py taille -1`, on peut simplement noter `#!py -1`.
La fonction devient alors :

```python
def dernier(classement):
    return classement[-1]
```

Dans le même esprit, l'avant-dernier élément d'un tableau a pour indice *négatif* `#!py -2`, l'antépénultième `#!py -3`, *etc*.

```python
# indices pos.      0 ------> 1 ------> 2 ---------> 3 -----> 4
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
# indices nég.     -5 <----- -4 <----- -3 <-------- -2 <---- -1
```
"""  # skip
