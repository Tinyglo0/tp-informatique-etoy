# --------- PYODIDE:code --------- #

def est_valide(numero):
    # Étape 0 : Obtenir une liste d'entiers représentant les 16 chiffres
    if isinstance(numero, list):
        chiffres = [int(x) for x in numero]
    else:
        nettoye = str(numero).replace(" ", "")
        if not nettoye.isdigit():
            return False
        chiffres = [int(c) for c in nettoye]

    # On vérifie que la liste comporte bien 16 chiffres
    if len(chiffres) != 16:
        return False

    total = 0
    for i in range(16):
        chiffre = chiffres[...]

        # Étape 1 : On double un chiffre sur deux (indices pairs : 0, 2, 4...)
        if i % 2 == ...:
            double = chiffre * ...

            # Étape 2 : Si le résultat est supérieur à 9, on additionne ses chiffres
            if double > ...:
                total = total + (double - ...)  # ou (double // 10) + (double % 10)
            else:
                total = total + ...
        else:
            # Chiffre non doublé (indices impairs)
            total = total + ...

    # Étape 4 : Le numéro est valide si le total se termine par 0
    return total % ... == ...


# --- Programme interactif ---
numero_carte = input("Entrez votre numéro de carte bancaire : ")
if est_valide(numero_carte):
    print("Numéro de carte valide !")
else:
    print("Numéro de carte invalide !")


# --------- PYODIDE:corr --------- #

def est_valide(numero):
    # Conversion en liste d'entiers
    if isinstance(numero, list):
        chiffres = [int(x) for x in numero]
    else:
        nettoye = str(numero).replace(" ", "")
        if not nettoye.isdigit():
            return False
        chiffres = [int(c) for c in nettoye]

    if len(chiffres) != 16:
        return False

    total = 0
    for i in range(16):
        chiffre = chiffres[i]
        if i % 2 == 0:
            double = chiffre * 2
            if double > 9:
                total += double - 9
            else:
                total += double
        else:
            total += chiffre

    return total % 10 == 0


# --------- PYODIDE:tests --------- #

# Exemple du cours (chaîne avec ou sans espaces)
assert est_valide("4137 8947 1175 5904") is True
assert est_valide("4137894711755904") is True

# Test sous forme de liste de chiffres
assert est_valide([4, 1, 3, 7, 8, 9, 4, 7, 1, 1, 7, 5, 5, 9, 0, 4]) is True

# Cartes du document
assert est_valide("5159 5674 0995 7111") is True
assert est_valide("6499 8024 5027 3568") is False


# --------- PYODIDE:secrets --------- #

# Autres cartes du document
assert est_valide("8504 1721 9127 3888") is True, "La carte 8504 1721 9127 3888 doit être valide"
assert est_valide("0043 6687 8348 5480") is False, "La carte 0043 6687 8348 5480 doit être invalide"

# Tests sous forme de listes de chiffres
assert est_valide([5, 1, 5, 9, 5, 6, 7, 4, 0, 9, 9, 5, 7, 1, 1, 1]) is True
assert est_valide([6, 4, 9, 9, 8, 0, 2, 4, 5, 0, 2, 7, 3, 5, 6, 8]) is False
assert est_valide([8, 5, 0, 4, 1, 7, 2, 1, 9, 1, 2, 7, 3, 8, 8, 8]) is True
assert est_valide([0, 0, 4, 3, 6, 6, 8, 7, 8, 3, 4, 8, 5, 4, 8, 0]) is False

# Cartes modifiées (altération d'un chiffre)
assert est_valide("5159 5674 0995 7112") is False, "Cette carte comporte une faute de frappe et doit être invalide"
assert est_valide("4137 8947 1175 5905") is False, "Cette carte comporte une faute de frappe et doit être invalide"
assert est_valide("4137 8947 1175 5900") is False, "Cette carte comporte une faute de frappe et doit être invalide"
assert est_valide("8504 1721 9127 3889") is False, "Cette carte comporte une faute de frappe et doit être invalide"

# Support du format entier et vérification de la longueur
assert est_valide(4137894711755904) is True, "La fonction doit supporter un entier"
assert est_valide("1234") is False, "Un numéro de moins de 16 chiffres doit être refusé"
assert est_valide([1, 2, 3, 4]) is False, "Une liste de moins de 16 chiffres doit être refusée"
assert est_valide("41378947117559040") is False, "Un numéro de plus de 16 chiffres doit être refusé"
