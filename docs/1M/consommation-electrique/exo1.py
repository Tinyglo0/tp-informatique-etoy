# --------- PYODIDE:code --------- #

def puissance_appareil(tension, intensite):
    ...

# --------- PYODIDE:corr --------- #

def puissance_appareil(tension, intensite):
    return tension * intensite

# --------- PYODIDE:tests --------- #

assert puissance_appareil(230, 20) == 4600
assert puissance_appareil(230, 0) == 0

# --------- PYODIDE:secrets --------- #


# Autres tests
tensions = [210 + 10 * i for i in range(5)]
intensites = [20 + i for i in range(5)]
for t in tensions:
    for i in intensites:
        assert puissance_appareil(t, i) == t * i

