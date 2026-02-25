# --------- PYODIDE:env --------- #
## {{ [cwd]alien_python/.snippets:env | FIGURE -> 6 | SOLUCE -> "H08 H06 M06 M08" }}

# --------- PYODIDE:code --------- #
a = ...
b = 5
gauche(2)
... colonne() > "04":
    bas(b)
...:
    haut(b)
droite(a)


# --------- PYODIDE:corr --------- #
a = 2
b = 5
gauche(2)
if colonne() > "04":
    bas(b)
else:
    haut(b)
droite(a)

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}

complete()
conditions('if colonne')
variables("bas(b)", 'haut(b)',"droite(a)")
valeurs(a=2, b=5)

# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}