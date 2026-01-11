# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app1 = App("dessin")




app1.creer_image(9, 9)  # ligne obligatoire en début de chaque programme pour créer l'image

app1.colorier(3, 7)  # on colorie un pixel

app1.afficher_image()  # pour afficher l'image