
# --------- PYODIDE:code --------- #
# 2. Créez la liste des sept jours de la semaine, en commençant par le lundi.
semaine = ...

# 3. Affichez cette liste en la parcourant à l'aide des indices.


# 4. Même consigne mais en utilisant un parcours par élément.


# --------- PYODIDE:corr --------- #
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for i in range(len(semaine)):
    print(semaine[i])
for jour in semaine:
    print(jour)

# --------- PYODIDE:secrets --------- #
assert semaine == ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'], 'La liste n\'est pas correcte'
