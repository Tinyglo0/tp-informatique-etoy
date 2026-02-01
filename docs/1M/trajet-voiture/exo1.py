# --------- PYODIDE:code --------- #

def calculer_distance(vitesse, temps):
    ...

# --------- PYODIDE:corr --------- #

def calculer_distance(vitesse, temps):
    return vitesse * temps

# --------- PYODIDE:tests --------- #

assert calculer_distance(110, 2) == 220
assert calculer_distance(50, 0.5) == 25
assert calculer_distance(130, 0) == 0

# --------- PYODIDE:secrets --------- #

# Autres tests
vitesses = [50, 80, 90, 110, 130]
temps_test = [1, 1.5, 2, 3, 5]
for v in vitesses:
    for t in temps_test:
        assert calculer_distance(v, t) == v * t