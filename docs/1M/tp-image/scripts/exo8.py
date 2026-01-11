# --------- PYODIDE:env --------- #
from pixel_art import * 
import p5

app.nouveau("figure8") 
 

valide = len(__USER_CODE__.split("\n"))<21
assert valide is True, "le code ne doit pas dépasser les 20 lignes !"
# --------- PYODIDE:code --------- #
creer_image(..., ...)

NB_LIGNES = ...
NB_COLONNES = ...
image = [[BLANC, BLANC, BLANC, ROSE, ROSE, ROSE, BLANC, BLANC, BLANC],
        [BLANC, BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC, BLANC],
        [BLANC, ROSE, BLANC, BLANC, ROSE, BLANC, BLANC, ROSE, BLANC],
        [...],
        [...],
        [...],
        [...]
        ]
for y in range(...):
    ligne = image[...]
    for x in range(...):
        colorier(x, y, ligne[...])

# --------- PYODIDE:post --------- #
grille_souhaitee = [[BLANC, BLANC, BLANC, ROSE, ROSE, ROSE, BLANC, BLANC, BLANC],
        [BLANC, BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC, BLANC],
        [BLANC, ROSE, BLANC, BLANC, ROSE, BLANC, BLANC, ROSE, BLANC],
        [BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC],
        [BLANC, BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC, BLANC],
        [BLANC, ROSE, BLANC, ROSE, BLANC, ROSE, BLANC, ROSE, BLANC],
        [ROSE, BLANC, BLANC, BLANC, BLANC, BLANC, BLANC, BLANC, ROSE]
        ]


if valide is True:
    app.verifier_programme(grille_souhaitee)