

# --------- PYODIDE:code --------- #

def deux_meilleurs(scores):
    ...

# --------- PYODIDE:corr --------- #

def deux_meilleurs(scores):
    max1 = None
    max2 = None
    for v in scores:
        if max1 is None or v > max1:
            max2 = max1
            max1 = v
        elif max2 is None or v > max2:
            max2 = v
    return max1, max2

# --------- PYODIDE:tests --------- #

scores_1 = [13, 15, 12, 3, 19, 7, 14]
assert deux_meilleurs(scores_1) == (19, 15)
scores_2 = [27, 35, 14, 35, 3, 26, 9]
assert deux_meilleurs(scores_2) == (35, 35)
assert deux_meilleurs([4, 5]) == (5, 4)
assert deux_meilleurs([5, 4]) == (5, 4)
assert deux_meilleurs([5, 5]) == (5, 5)
assert deux_meilleurs([9]) == (9, None)
assert deux_meilleurs([]) == (None, None)

# --------- PYODIDE:secrets --------- #


# autres tests
assert deux_meilleurs([7]) == (7, None)
assert deux_meilleurs([1, 2]) == (2, 1)
assert deux_meilleurs([2, 1]) == (2, 1)
assert deux_meilleurs([-9, -3]) == (-3, -9)
assert deux_meilleurs([8, -3]) == (8, -3)
assert deux_meilleurs([1, 1]) == (1, 1)
assert deux_meilleurs([1, 1, 1, 1]) == (1, 1)
assert deux_meilleurs([1, 0, 1, 1]) == (1, 1)
assert deux_meilleurs([9, 8, 7, 6, 5]) == (9, 8)
assert deux_meilleurs([1, 2, 3, 4, 5]) == (5, 4)
assert deux_meilleurs([4, 5, 2, 5, 1, 2]) == (5, 5)
assert deux_meilleurs([9, 3, 2, 1, 5]) == (9, 5)
assert deux_meilleurs([2, 9, 3, 4, 5]) == (9, 5)