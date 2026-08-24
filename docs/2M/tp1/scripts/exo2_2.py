# --------- PYODIDE:code --------- #
invites = ["Hector", "Paul", "Jules", "Marie", "Pierre", "Alphonsine", "Dorothée", "Eva", "Jeannette", "Kathy", "Carole", "Zoé"]
invites.append("Christian")
invites.append("Louis")
invites.remove("Kathy")

# 1. Modifiez votre code pour prendre en compte les contraintes :
# demander à l'utilisateur s'il y a des noms à rajouter. 
# Si l'utilisateur entre "q", afficher le nombre d'invités et la liste.



# --------- PYODIDE:corr --------- #
invites = ["Hector", "Paul", "Jules", "Marie", "Pierre", "Alphonsine", "Dorothée", "Eva", "Jeannette", "Kathy", "Carole", "Zoé"]
invites.append("Christian")
invites.append("Louis")
invites.remove("Kathy")

while True:
    nom = input("Entrez un nom à rajouter (ou 'q' pour quitter) : ")
    if nom == 'q':
        break
    invites.append(nom)

print("Nombre d'invités :", len(invites))
print("Liste des invités :", invites)

# --------- PYODIDE:secrets --------- #
assert len(__USER_CODE__.strip()) > 3, 'Votre code est vide ou trop court !'
assert 'input' in __USER_CODE__, 'Vous devez utiliser input()'

