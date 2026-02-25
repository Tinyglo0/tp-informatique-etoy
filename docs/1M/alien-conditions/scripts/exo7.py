# --------- PYODIDE:env --------- #

valide = "if colonne" in __USER_CODE__ and "if ligne" in __USER_CODE__
assert valide is True, "On doit utiliser les structures conditionnelles"

## {{ [cwd]alien_python/.snippets:env | FIGURE -> 7 | SOLUCE -> "H08 H04 M04 M06 K06 K08" }}

# --------- PYODIDE:code --------- #
gauche(...)
x = "..."
if ligne() < x:
    bas(5)
elif ligne() > x:
    bas(6)
else:
    bas(7)

y = "..."
if colonne() < y:
    haut(2)
elif colonne() > y:
    haut(2)
    droite(2)
else:
    droite(2)
    haut(2)

droite(...)


# --------- PYODIDE:corr --------- #
gauche(4)
x = "J"
if ligne() < x:
    bas(5)
elif ligne() > x:
    bas(6)
else:
    bas(7)

y = "04"
if colonne() < y:
    haut(2)
elif colonne() > y:
    haut(2)
    droite(2)
else:
    droite(2)
    haut(2)

droite(2)

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}

complete()
conditions('if colonne', 'if ligne', 'elif', 'else')
valeurs(y="04")


# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}