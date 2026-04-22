# --------- PYODIDE:code --------- #
def attente_seuil_bacteries(pop_initiale, pop_finale):
    ...



# --------- PYODIDE:corr --------- #
def attente_seuil_bacteries(pop_initiale, pop_finale):
    pop = pop_initiale
    heures = 0
    while pop < pop_finale:
        pop = pop * 1.105 # Augmentation de 10.5%
        heures += 1
    return heures

# --------- PYODIDE:tests --------- #
assert attente_seuil_bacteries(100000, 200000) == 7
assert attente_seuil_bacteries(100000, 500000) == 17
assert attente_seuil_bacteries(100000, 1000000) == 24
