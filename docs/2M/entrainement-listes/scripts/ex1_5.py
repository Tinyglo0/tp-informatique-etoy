# --------- PYODIDE:env --------- #
pays = ['Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande',
        'France', 'Grèce', 'Hongrie', 'Irlande', 'Italie', 'Lettonie', 'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas', 
        'Pologne', 'Portugal', 'République tchèque', 'Roumanie', 'Slovaquie', 'Slovénie', 'Suède']
capitale = ['Berlin', 'Vienne', 'Bruxelles', 'Sofia', 'Nicosie', 'Zagreb', 'Copenhague', 'Madrid', 'Tallinn', 'Helsinki',
           'Paris', 'Athènes', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'La Valette', 'Amsterdam',
           'Varsovie', 'Lisbonne', 'Prague', 'Bucarest', 'Bratislava', 'Ljubljana', 'Stockholm']
population = [83.16, 8.98, 11.75, 6.45, 0.90, 3.85, 5.93, 47.43, 1.37, 5.56,
             68.4, 10.71, 9.60, 5.27, 58.98, 1.88, 2.9, 0.66, 0.54, 17.81,
             36.7, 10.5, 10.7, 19.06, 5.43, 2.11, 10.45]
# --------- PYODIDE:code --------- #
# 5) Pays au hasard, avec sa capitale et sa population
import random
...

# --------- PYODIDE:corr --------- #
import random
indice_hasard = random.randint(0, len(pays) - 1)
print("Pays au hasard:", pays[indice_hasard])
print("Capitale:", capitale[indice_hasard])
print("Population:", population[indice_hasard])

# --------- PYODIDE:secrets --------- #
pass
