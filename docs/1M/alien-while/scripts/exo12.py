# --------- PYODIDE:env --------- #
## {{ [cwd]alien_python/.snippets:dessin | FIGURE -> 12 }}

# --------- PYODIDE:dessin --------- #
pas = 1
while colonne() > "03" :
    bas(pas)
    droite(pas)
    haut(pas + 1)
    gauche(pas + 1)
    pas = pas + 2
