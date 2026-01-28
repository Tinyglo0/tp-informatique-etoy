# --------- PYODIDE:code --------- #

def energie_consommee(puissance, temps):
    ...

# --------- PYODIDE:corr --------- #

def energie_consommee(puissance, temps):
    return puissance * temps

# --------- PYODIDE:tests --------- #

assert energie_consommee(4600, 1.5) == 6900
assert energie_consommee(4600, 0) == 0

# --------- PYODIDE:secrets --------- #


# Autres tests
puissances = [4000 + 10 * i for i in range(5)]
durees = [2 + i for i in range(5)]
for p in puissances:
    for d in durees:
        assert energie_consommee(p, d) == p * d