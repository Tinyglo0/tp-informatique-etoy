# --------- PYODIDE:code --------- #

def conversion_age(ageDuChat):
    ageConverti = 0

    # Calculer l'équivalent en années humaines en fonction de l'âge du chat :
    if ageDuChat == 1:
        ageConverti = 15
    elif ... :
        ageConverti = 15 + 9
    else:
    # Vous devrez utiliser une formule mathématique !
        ...

    # Afficher le résultat (âge converti) à l'utilisateur
    print("En années humaines, votre chat a l'équivalent de " + str(ageConverti) + " ans.")
    return ageConverti

ageDuChat = int(input("Quel âge a votre chat (en années) ? "))
conversion_age(ageDuChat)

# --------- PYODIDE:corr --------- #

def conversion_age(ageDuChat):
    if ageDuChat == 1:
        return 15
    elif ageDuChat == 2:
        return 24
    else:
        return 24 + (ageDuChat - 2) * 4

# --------- PYODIDE:tests --------- #

assert conversion_age(1) == 15
assert conversion_age(2) == 24

# --------- PYODIDE:secrets --------- #

assert conversion_age(3) == 28
assert conversion_age(4) == 32
assert conversion_age(5) == 36
assert conversion_age(10) == 56
assert conversion_age(20) == 96