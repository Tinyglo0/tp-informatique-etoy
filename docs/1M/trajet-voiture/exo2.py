# --------- PYODIDE:code --------- #

def calculer_carburant(distance, conso_100):
    ...

# --------- PYODIDE:corr --------- #

def calculer_carburant(distance, conso_100):
    return (distance * conso_100) / 100

# --------- PYODIDE:tests --------- #

assert calculer_carburant(220, 6) == 13.2
assert calculer_carburant(100, 5) == 5
assert calculer_carburant(0, 5) == 0

# --------- PYODIDE:secrets --------- #

dists = [100, 200, 350, 500]
consos = [4, 5.5, 6, 7.2]
for d in dists:
    for c in consos:
        attendu = (d * c) / 100
        # On utilise une petite marge d'erreur pour les flottants si besoin, 
        # mais ici l'égalité stricte devrait passer pour des calculs simples
        assert abs(calculer_carburant(d, c) - attendu) < 1e-9