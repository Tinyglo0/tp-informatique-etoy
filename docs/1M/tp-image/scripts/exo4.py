# --------- PYODIDE:env --------- #
from pixel_art import * 
import p5

app.nouveau("figure4") 
app.creer_image(11, 9) 
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

valide = len(__USER_CODE__.split("\n"))<7
assert valide is True, "le code ne doit pas dépasser les 6 lignes !"
# --------- PYODIDE:code --------- #
for x in [...]:
    colorier(x, ..., VERT)

for x in [...]:
    colorier(x, ..., VERT)

# --------- PYODIDE:post --------- #
grille_souhaitee = [[BLANC,BLANC,VERT,BLANC,BLANC,BLANC,BLANC,BLANC,VERT,BLANC,BLANC],
                    [VERT, BLANC,BLANC, VERT,BLANC,BLANC,BLANC, VERT,BLANC,BLANC, VERT],
                    [VERT, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT,BLANC, VERT],
                    [VERT, VERT, VERT,BLANC, VERT, VERT, VERT,BLANC, VERT, VERT, VERT],
                    [BLANC, VERT,VERT, VERT, VERT, VERT, VERT, VERT, VERT, VERT,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    ]
if valide is True:
    app.verifier_programme(grille_souhaitee)