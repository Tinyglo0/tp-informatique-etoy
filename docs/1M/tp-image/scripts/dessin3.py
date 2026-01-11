# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app8 = App("dessin3")
app8.creer_image(9, 7)  # ligne obligatoire en début de chaque programme pour créer l'image
NB_LIGNES = 7
NB_COLONNES = 9
image = [[BLANC, BLANC, BLANC, ROSE, ROSE, ROSE, BLANC, BLANC, BLANC],
        [BLANC, BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC, BLANC],
        [BLANC, ROSE, BLANC, BLANC, ROSE, BLANC, BLANC, ROSE, BLANC],
        [BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC],
        [BLANC, BLANC, ROSE, ROSE, ROSE, ROSE, ROSE, BLANC, BLANC],
        [BLANC, ROSE, BLANC, ROSE, BLANC, ROSE, BLANC, ROSE, BLANC],
        [ROSE, BLANC, BLANC, BLANC, BLANC, BLANC, BLANC, BLANC, ROSE]
        ]


for y in range(NB_LIGNES):
    ligne = image[y]
    for x in range(NB_COLONNES):
        app8.colorier(x, y, ligne[x])



app8.afficher_image()  # pour afficher l'image