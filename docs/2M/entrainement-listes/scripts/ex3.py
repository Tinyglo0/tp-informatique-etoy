# --------- PYODIDE:code --------- #
def entrelace(liste1, liste2):
    ...

# --------- PYODIDE:corr --------- #
def entrelace(liste1, liste2):
    res = []
    for i in range(len(liste1)):
        res.append(liste1[i])
        res.append(liste2[i])
    return res

# --------- PYODIDE:secrets --------- #
liste1 = [4,8,6,0,6,4]
liste2 = [5,1,9,3,7,3]
assert entrelace(liste1, liste2) == [4,5,8,1,6,9,0,3,6,7,4,3]
assert entrelace([1, 2], [3, 4]) == [1, 3, 2, 4]
