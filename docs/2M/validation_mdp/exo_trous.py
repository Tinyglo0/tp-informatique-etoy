# --------- PYODIDE:code --------- #
SPECIAUX = ",;:!?./§%*$£&#{}()[]-_@"


def valide(mdp):
    if len(mdp) < ...:
        return ...
    minuscule = ...
    majuscule = ...
    chiffre = ...
    special = ...
    for c in mdp:
        if c.isupper():
            majuscule = ...
        elif ...:
            ...
        elif ...:
            ...
        elif ... in ...:
            ...
    return ... and ... and ... and ...


# --------- PYODIDE:corr --------- #
SPECIAUX = ",;:!?./§%*$£&#{}()[]-_@"


def valide(mdp):
    if len(mdp) < 14:
        return False
    minuscule = False
    majuscule = False
    chiffre = False
    special = False
    for c in mdp:
        if c.isupper():
            majuscule = True
        elif c.islower():
            minuscule = True
        elif c.isnumeric():
            chiffre = True
        elif c in SPECIAUX:
            special = True
    return minuscule and majuscule and chiffre and special


# --------- PYODIDE:tests --------- #
# Mot de passe valide
mdp = "X5j13$#eCM1cG@Kdce246gs%mFs#3tv6"
assert valide(mdp) is True

# Trop court
mdp = "X5j13$#eCM"
assert valide(mdp) is False

# Pas de majuscule
mdp = "5j13$#e1c@dce246gs%ms#3tv6"
assert valide(mdp) is False

# Pas de minuscule
mdp = "X513$#CM1G@K246%F#36"
assert valide(mdp) is False

# Pas de caractère spécial
mdp = "X5j13eCM1cGKdce246gsmFs3tv6"
assert valide(mdp) is False
# --------- PYODIDE:secrets --------- #
from string import ascii_lowercase, ascii_uppercase
from random import sample, shuffle

SPECIAUX_BIS = ",;:!?./§%*$£&#{}()[]-_@"

# Valide mais taille = 13
mdp = (
    sample(ascii_lowercase, 4)
    + sample(ascii_uppercase, 4)
    + sample("0123456789", 3)
    + sample(SPECIAUX_BIS, 2)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} est trop court"

# Valide et taille = 14
mdp = (
    sample(ascii_lowercase, 4)
    + sample(ascii_uppercase, 4)
    + sample("0123456789", 4)
    + sample(SPECIAUX_BIS, 3)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is True, f"{mdp} devrait être valide"

# taille = 14 mais pas de majusucule
mdp = (
    sample(ascii_lowercase, 7)
    # + sample(ascii_uppercase, 4)
    + sample("0123456789", 4)
    + sample(SPECIAUX_BIS, 3)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} ne contient pas de majuscule"

# Valide et taille > 14
mdp = (
    sample(ascii_lowercase, 5)
    + sample(ascii_uppercase, 5)
    + sample("0123456789", 5)
    + sample(SPECIAUX_BIS, 5)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is True, f"{mdp} devrait être valide"

# Trop court
mdp = (
    sample(ascii_lowercase, 4)
    + sample(ascii_uppercase, 3)
    + sample("0123456789", 2)
    + sample(SPECIAUX_BIS, 1)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} est trop court"

# Sans majuscule
mdp = (
    sample(ascii_lowercase, 5)
    # + sample(ascii_uppercase, 5)
    + sample("0123456789", 5)
    + sample(SPECIAUX_BIS, 5)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} ne contient pas de majuscule"

# Sans minuscule
mdp = (
    # sample(ascii_lowercase, 5)
    sample(ascii_uppercase, 5)
    + sample("0123456789", 5)
    + sample(SPECIAUX_BIS, 5)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} ne contient pas de minuscule"

# Sans chiffre
mdp = (
    sample(ascii_lowercase, 5)
    + sample(ascii_uppercase, 5)
    # + sample("0123456789", 5)
    + sample(SPECIAUX_BIS, 5)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} ne contient pas de chiffre"

# Sans caractère spécial
mdp = (
    sample(ascii_lowercase, 5)
    + sample(ascii_uppercase, 5)
    + sample("0123456789", 5)
    # + sample(SPECIAUX, 5)
)
shuffle(mdp)
mdp = "".join(mdp)
assert valide(mdp) is False, f"{mdp} ne contient pas de caractère spécial"
