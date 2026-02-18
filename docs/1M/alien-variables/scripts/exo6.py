# --------- PYODIDE:env --------- #
## {{ [cwd]alien_python/.snippets:env | FIGURE -> 6 | SOLUCE -> "H08 D08 D07 D02 F02 F14" }}

# --------- PYODIDE:code --------- #
haut(...)
...
x = ...
gauche(x + 1)
y = ...
bas(x - y)
z = ...
droite(x * z)


# --------- PYODIDE:corr --------- #
haut(4)
gauche()
x = 4
gauche(x + 1)
y = 2
bas(x - y)
z = 3
droite(x * z)

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}
valeurs(x=4, y=2, z=3)


# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}