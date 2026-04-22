# --------- PYODIDE:code --------- #
def placement_bancaire_seuil(placement, taux, somme_cible):
    # à compléter sur plusieurs lignes
    ...

# --------- PYODIDE:corr --------- #
def placement_bancaire_seuil(placement, taux, somme_cible):
    somme = placement
    nb_annees = 0
    while somme < somme_cible:
        somme = somme * (1 + taux/100)
        nb_annees += 1
    return (nb_annees, round(somme, 2))

# --------- PYODIDE:tests --------- #
assert placement_bancaire_seuil(2000, 2, 3000) == (21, 3031.33)
assert placement_bancaire_seuil(5000, 1.5, 8000) == (32, 8051.62)
assert placement_bancaire_seuil(2000, 5.25, 5000) == (18, 5023.75)
