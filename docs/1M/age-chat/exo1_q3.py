# --------- PYODIDE:code --------- #

def humain_vers_chat(ageHumain):
    # à vous de jouer !
    ...

# --------- PYODIDE:corr --------- #

def humain_vers_chat(ageHumain):
    if ageHumain <= 10:
        return 0.5  # Représente arbitrairement les chatons
    elif ageHumain <= 15:
        return 1
    elif ageHumain <= 24:
        return 2
    else:
        # Formule inversée : (ageHumain - 24) / 4 + 2
        return int(((ageHumain - 24) / 4) + 2)

# --------- PYODIDE:tests --------- #

assert humain_vers_chat(15) == 1
assert humain_vers_chat(24) == 2

# --------- PYODIDE:secrets --------- #

assert humain_vers_chat(28) == 3
assert humain_vers_chat(32) == 4
assert humain_vers_chat(36) == 5
assert humain_vers_chat(56) == 10
assert humain_vers_chat(76) == 15
assert humain_vers_chat(96) == 20