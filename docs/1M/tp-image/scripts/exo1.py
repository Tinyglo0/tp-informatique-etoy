# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app2 = App("figure1")


app2.creer_image(9, 9)  # ligne obligatoire en début de chaque programme pour créer l'image


app2.colorier(4, 2)
app2.colorier(4, 3)
app2.colorier(4, 5)
app2.colorier(4, 6)

app2.colorier(2, 4)
app2.colorier(3, 4)
app2.colorier(4, 4)
app2.colorier(5, 4)
app2.colorier(6, 4)

app2.demarrer_dessin_libre(correction=True)