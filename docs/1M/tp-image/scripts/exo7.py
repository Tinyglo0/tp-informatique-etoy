# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app7 = App("figure7")


app7.creer_image(9, 6)  # ligne obligatoire en début de chaque programme pour créer l'image

NB_LIGNES = 6
NB_COLONNES = 9
image = [[BLANC, BLANC, BLANC, BLEU, BLANC, BLEU, BLANC, BLANC, BLANC],
        [BLEU, BLANC, BLEU, BLEU, BLEU, BLEU, BLEU, BLANC, BLEU],
        [BLEU, BLEU, BLEU, BLANC, BLEU, BLANC, BLEU, BLEU, BLEU],
        [BLANC, BLEU, BLEU, BLEU, BLEU, BLEU, BLEU, BLEU, BLANC],
        [BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC],
        [BLEU, BLEU,BLANC,BLANC,BLANC,BLANC,BLANC,BLEU, BLEU]
        ]
for y in range(NB_LIGNES):
    ligne = image[y]
    for x in range(NB_COLONNES):
        app7.colorier(x, y, ligne[x])

app7.demarrer_dessin_libre(correction=True,couleur=BLEU)