

# --------- PYODIDE:code --------- #

def est_bissextile(annee):
    ...

# --------- PYODIDE:corr --------- #

def est_bissextile(annee):
    if annee % 4 != 0:
        return False
    if annee % 100 != 0:
        return True
    if annee % 400 != 0:
        return False
    return True

# --------- PYODIDE:tests --------- #

assert est_bissextile(2022) is False
assert est_bissextile(2020) is True
assert est_bissextile(2100) is False
assert est_bissextile(2400) is True

# --------- PYODIDE:secrets --------- #


# Tests supplémentaires
for annee in range(500, 1001):
    attendu = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
    assert est_bissextile(annee) is attendu, f"Erreur avec {annee = }"