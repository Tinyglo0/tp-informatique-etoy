# --------- PYODIDE:code --------- #

def calculer_puissance(force, bonus_arme):
    ...

# --------- PYODIDE:corr --------- #

def calculer_puissance(force, bonus_arme):
    return force + bonus_arme

# --------- PYODIDE:tests --------- #

assert calculer_puissance(80, 20) == 100
assert calculer_puissance(0, 10) == 10
assert calculer_puissance(50, 0) == 50

# --------- PYODIDE:secrets --------- #
import random
for _ in range(5):
    f = random.randint(10, 100)
    b = random.randint(0, 50)
    assert calculer_puissance(f, b) == f + b