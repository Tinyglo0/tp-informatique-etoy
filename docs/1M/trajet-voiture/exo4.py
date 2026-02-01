# --------- PYODIDE:env --------- #
flag_dist = False
flag_carb = False
flag_cout = False

# On redéfinit les fonctions "correctes" dans l'environnement caché, 
# mais on y ajoute un "mouchard" (global flag) pour savoir si l'élève les appelle.

def calculer_distance(v, t):
    global flag_dist
    flag_dist = True
    return v * t

def calculer_carburant(d, c):
    global flag_carb
    flag_carb = True
    return (d * c) / 100

def calculer_cout(l, p):
    global flag_cout
    flag_cout = True
    return round(l * p, 2)

# --------- PYODIDE:code --------- #

def cout_trajet(vitesse, temps, conso_100, prix_litre):
    ...

# --------- PYODIDE:corr --------- #

def cout_trajet(vitesse, temps, conso_100, prix_litre):
    dist = calculer_distance(vitesse, temps)
    litres = calculer_carburant(dist, conso_100)
    prix_final = calculer_cout(litres, prix_litre)
    return prix_final

# --------- PYODIDE:tests --------- #

# Test public
assert cout_trajet(110, 2, 6, 1.85) == 24.42

# --------- PYODIDE:secrets --------- #

# Vérification que les fonctions intermédiaires ont bien été appelées
if not flag_dist:
    terminal_message("1234", "Il faut utiliser la fonction calculer_distance !", "warning")
if not flag_carb:
    terminal_message("1234", "Il faut utiliser la fonction calculer_carburant !", "warning")
if not flag_cout:
    terminal_message("1234", "Il faut utiliser la fonction calculer_cout !", "warning")

# Autres tests de valeurs
assert cout_trajet(130, 3, 7, 1.90) == 51.87
assert cout_trajet(90, 1, 5, 2.0) == 9.0