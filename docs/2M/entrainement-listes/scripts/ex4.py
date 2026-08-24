# --------- PYODIDE:code --------- #
# 1) Liste des carrés des entiers de 1 à 25
liste1 = [...]
print("liste1:", liste1)

# 2) Liste des entiers de 0 à 100 qui ne sont pas divisibles par 7
liste2 = [...]
print("liste2:", liste2)

# --------- PYODIDE:corr --------- #
liste1 = [i**2 for i in range(1, 26)]
print("liste1:", liste1)

liste2 = [i for i in range(101) if i % 7 != 0]
print("liste2:", liste2)

# --------- PYODIDE:secrets --------- #
assert liste1 == [i**2 for i in range(1, 26)]
assert liste2 == [i for i in range(101) if i % 7 != 0]
