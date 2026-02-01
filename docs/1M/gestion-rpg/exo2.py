# --------- PYODIDE:code --------- #

def calculer_degats(puissance, absorption):
    ...

# --------- PYODIDE:corr --------- #

def calculer_degats(puissance, absorption):
    return puissance - absorption

# --------- PYODIDE:tests --------- #

assert calculer_degats(100, 25) == 75
assert calculer_degats(50, 0) == 50

# --------- PYODIDE:secrets --------- #
assert calculer_degats(50, 50) == 0
assert calculer_degats(100, 10) == 90