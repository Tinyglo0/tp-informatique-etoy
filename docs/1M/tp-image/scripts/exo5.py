# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app5 = App("figure5")


app5.creer_image(11, 1)  # ligne obligatoire en début de chaque programme pour créer l'image

NB_COLONNES = 11
ligne_5 = [BLANC, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC, BLANC]
for x in range(NB_COLONNES):
    app5.colorier(x, 0, ligne_5[x])

app5.demarrer_dessin_libre(correction=True,couleur=VERT)