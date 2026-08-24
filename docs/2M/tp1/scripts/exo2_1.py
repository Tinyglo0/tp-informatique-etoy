
# --------- PYODIDE:code --------- #
# 2. Créez une liste invites représentant les invités d'Alice.
invites = ["Hector", "Paul", "Jules", "Marie", "Pierre", "Alphonsine", "Dorothée", "Eva", "Jeannette", "Kathy", "Carole", "Zoé"]

# 3. Alice rajoute Christian et Louis à sa liste et decide de ne plus inviter Kathy.
# Traduire ces modifications par des instructions Python.
# (Le prénom Kathy doit toujours figurer dans la liste à sa création)



# 4. Affichez le nombre d'invités une fois ces remplacements effectués.


# --------- PYODIDE:corr --------- #
invites = ["Hector", "Paul", "Jules", "Marie", "Pierre", "Alphonsine", "Dorothée", "Eva", "Jeannette", "Kathy", "Carole", "Zoé"]
invites.append("Christian")
invites.append("Louis")
invites.remove("Kathy")
print(len(invites))

# --------- PYODIDE:secrets --------- #
assert 'Christian' in invites, 'Christian manque'
assert 'Louis' in invites, 'Louis manque'
assert 'Kathy' not in invites, 'Kathy n\'a pas été supprimée'
