# --------- PYODIDE:env --------- #

## {{ [cwd]alien_python/.snippets:env | FIGURE -> 5 | SOLUCE -> "H08 H03 F03 F11 N11 N13" }}


# --------- PYODIDE:code --------- #
gauche(...)
if ligne()  ... :
    e = 2
else :
    e = 3
haut(e)
droite(8)
if colonne() ... :
    f = 5
else :
    f = 8
bas(f)
droite(...)

# --------- PYODIDE:corr --------- #
gauche(5)                       # Une solution possible
if ligne() > "A" :
    e = 2
else :
    e = 3
haut(e)
droite(8)
if colonne() < "10" :
    f = 5
else :
    f = 8
bas(f)
droite(2)

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}

complete()
conditions('if colonne', "else")
variables("haut(e)","bas(f)")


# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}