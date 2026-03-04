# --------- PYODIDE:code --------- #

def stade_de_vie(ageDuChat):
    # à vous de jouer !
    ...

# --------- PYODIDE:corr --------- #

def stade_de_vie(ageDuChat):
    if ageDuChat < 1:  # Moins d'un an, on englobe Chaton et le début Junior
        return "Chaton"
    elif ageDuChat <= 2:
        return "Junior"
    elif ageDuChat <= 6:
        return "Adulte"
    elif ageDuChat <= 10:
        return "Mûr"
    elif ageDuChat <= 14:
        return "Senior"
    else:
        return "Gériatrique"

# --------- PYODIDE:tests --------- #

assert stade_de_vie(2) == "Junior"
assert stade_de_vie(5) == "Adulte"

# --------- PYODIDE:secrets --------- #

assert stade_de_vie(0.5) == "Chaton"
assert stade_de_vie(8) == "Mûr"
assert stade_de_vie(12) == "Senior"
assert stade_de_vie(15) == "Gériatrique"
assert stade_de_vie(20) == "Gériatrique"