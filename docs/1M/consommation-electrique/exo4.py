# --------- PYODIDE:env --------- #
fonction1 = False
fonction2 = False
fonction3 = False

def puissance_appareil(tension, intensite):
    global fonction1
    fonction1 = True
    return tension * intensite


def cout_utilisation(energie, prix_base):
    global fonction2
    fonction2 = True
    return round(energie * prix_base, 2)


def energie_consommee(puissance, temps):
    global fonction3
    fonction3 = True
    return puissance * temps

# --------- PYODIDE:code --------- #

def ...(..., ..., ..., ...):
    ...

# --------- PYODIDE:corr --------- #

def cout_consommation(tension, prix, intensite, duree):
    puissance = puissance_appareil(tension, intensite)
    energie_en_Wh = energie_consommee(puissance, duree)
    energie_en_kWh = energie_en_Wh / 1000
    cout = cout_utilisation(energie_en_kWh, prix)
    return cout

# --------- PYODIDE:tests --------- #

assert cout_consommation(230, 0.1582, 20, 1.5) == 1.09
assert cout_consommation(230, 0.1582, 0, 1.5) == 0

# --------- PYODIDE:secrets --------- #
if fonction1 is not True:
    terminal_message("1234","il faut utiliser la fonction puissance_appareil","warning") 
if fonction2 is not True:
    terminal_message("1234","il faut utiliser la fonction cout_utilisation","warning")
if fonction3 is not True:
    terminal_message("1234","il faut utiliser la fonction energie_consommee","warning") 


# Autres tests
assert cout_consommation(200, 0.125, 25, 2) == 1.25
assert cout_consommation(220, 0.5, 15, 5) == 8.25