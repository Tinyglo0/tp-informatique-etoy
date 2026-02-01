# --------- PYODIDE:env --------- #
flag_puissance = False
flag_absorb = False
flag_degats = False

def calculer_puissance(f, b):
    global flag_puissance
    flag_puissance = True
    return f + b

def calculer_absorption(a, c):
    global flag_absorb
    flag_absorb = True
    return a * c

def calculer_degats(p, a):
    global flag_degats
    flag_degats = True
    return p - a

# --------- PYODIDE:code --------- #

def pv_restants(pv_actuels, force, bonus_arme, armure, coeff):
    ...

# --------- PYODIDE:corr --------- #

def pv_restants(pv_actuels, force, bonus_arme, armure, coeff):
    puis = calculer_puissance(force, bonus_arme)
    abs_val = calculer_absorption(armure, coeff)
    degats = calculer_degats(puis, abs_val)
    return pv_actuels - degats

# --------- PYODIDE:tests --------- #

# PV: 200, Force: 80, Epée: 20 (Total 100), Armure: 50, Coeff: 0.5 (Absorb 25) -> Dégats 75
assert pv_restants(200, 80, 20, 50, 0.5) == 125.0

# --------- PYODIDE:secrets --------- #

# Vérification des appels de fonctions
if not flag_puissance:
    terminal_message("1234", "Utilisez la fonction calculer_puissance !", "warning")
if not flag_absorb:
    terminal_message("1234", "Utilisez la fonction calculer_absorption !", "warning")
if not flag_degats:
    terminal_message("1234", "Utilisez la fonction calculer_degats !", "warning")

# Autres tests
# PV: 100, Atk: 10+0=10, Abs: 20*0.1=2 -> Dmg: 8 -> Reste: 92
assert pv_restants(100, 10, 0, 20, 0.1) == 92.0