# --------- PYODIDE:code --------- #

def calculer_cout(litres, prix_litre):
    ...

# --------- PYODIDE:corr --------- #

def calculer_cout(litres, prix_litre):
    return round(litres * prix_litre, 2)

# --------- PYODIDE:tests --------- #

assert calculer_cout(13.2, 1.85) == 24.42
assert calculer_cout(10, 1.5) == 15.0
assert calculer_cout(0, 2.0) == 0

# --------- PYODIDE:secrets --------- #

vols = [10, 20.5, 30.123, 50]
prix = [1.5, 1.85, 2.0, 1.66]
for v in vols:
    for p in prix:
        assert calculer_cout(v, p) == round(v * p, 2)