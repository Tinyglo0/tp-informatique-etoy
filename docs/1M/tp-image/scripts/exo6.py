# --------- PYODIDE:env --------- #
from pixel_art import * 
import p5

app.nouveau("figure6") 
app.creer_image(11, 8) 
# première ligne :
colorier(2,0,(0,255,0))
colorier(8,0,(0,255,0))

# deuxième ligne :
colorier(0,1,(0,255,0))
colorier(3,1,(0,255,0))
colorier(7,1,(0,255,0))
colorier(10,1,(0,255,0))

# troisième ligne :
colorier(0,2,(0,255,0))
colorier(2,2,(0,255,0))
colorier(3,2,(0,255,0))
colorier(4,2,(0,255,0))
colorier(5,2,(0,255,0))
colorier(6,2,(0,255,0))
colorier(7,2,(0,255,0))
colorier(8,2,(0,255,0))
colorier(10,2,(0,255,0))

# quatrième ligne
for x in [0,1,2,4,5,6,8,9,10]:
    colorier(x, 3, VERT)

# cinquième ligne
for x in [1,2,3,4,5,6,7,8,9]:
    colorier(x, 4, VERT)

# sixième ligne
for x in range(2, 9):
    colorier(x, 5, VERT)



valide = len(__USER_CODE__.split("\n"))<10
assert valide is True, "le code ne doit pas dépasser les 7 lignes !"
# --------- PYODIDE:code --------- #
NB_COLONNES = 11
ligne_6 = [...]
for x in range(...):
    colorier(x, ..., ...)

ligne_7 = [...]
for x in range(...):
    colorier(x, ..., ...)

# --------- PYODIDE:post --------- #
grille_souhaitee = [[BLANC, BLANC, VERT, BLANC, BLANC, BLANC, BLANC, BLANC, VERT, BLANC, BLANC],
                    [VERT, BLANC,BLANC, VERT, BLANC, BLANC, BLANC, VERT, BLANC, BLANC, VERT],
                    [VERT, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC, VERT],
                    [VERT, VERT, VERT, BLANC, VERT, VERT, VERT, BLANC, VERT, VERT, VERT],
                    [BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC],
                    [BLANC, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC, BLANC],
                    [BLANC, BLANC, BLANC, VERT, BLANC, BLANC, BLANC, BLANC, VERT, BLANC, BLANC],
                    [BLANC, BLANC, VERT, VERT, BLANC, BLANC, BLANC, BLANC, VERT, VERT, BLANC],
                    ]
if valide is True:
    app.verifier_programme(grille_souhaitee)