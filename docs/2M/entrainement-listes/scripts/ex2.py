# --------- PYODIDE:code --------- #
def produit(liste):
    ...

# --------- PYODIDE:corr --------- #
def produit(liste):
    res = 1
    for nb in liste:
        res *= nb
    return res

# --------- PYODIDE:secrets --------- #
assert produit([2,1,3,4]) == 24
assert produit([5, 5]) == 25
assert produit([-1, 10, 2]) == -20
assert produit([]) == 1
