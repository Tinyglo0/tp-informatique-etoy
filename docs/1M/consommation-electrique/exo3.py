# --------- PYODIDE:code --------- #

def cout_utilisation(energie, prix_base):
    ...

# --------- PYODIDE:corr --------- #

def cout_utilisation(energie, prix_base):
    return round(energie * prix_base, 2)

# --------- PYODIDE:tests --------- #

assert cout_utilisation(6.9, 0.1582) == 1.09
assert cout_utilisation(0, 0.1582) == 0

# --------- PYODIDE:secrets --------- #


# Autres tests
energies = [2 + i for i in range(5)]
prix = [0.25, 0.5, 0.125]
for e in energies:
    for pr in prix:
        assert cout_utilisation(e, pr) == round(e * pr, 2)