# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app3 = App("figure3")

# image de 3 lignes de 11 colonnes
app3.creer_image(11, 3) 

# ligne 0 :
app3.colorier(2,0,(0,255,0))
app3.colorier(8,0,(0,255,0))

# ligne 1 :
app3.colorier(0,1,(0,255,0))
app3.colorier(3,1,(0,255,0))
app3.colorier(7,1,(0,255,0))
app3.colorier(10,1,(0,255,0))

# ligne 2 :
app3.colorier(0,2,(0,255,0))
app3.colorier(2,2,(0,255,0))
app3.colorier(3,2,(0,255,0))
app3.colorier(4,2,(0,255,0))
app3.colorier(5,2,(0,255,0))
app3.colorier(6,2,(0,255,0))
app3.colorier(7,2,(0,255,0))
app3.colorier(8,2,(0,255,0))
app3.colorier(10,2,(0,255,0))

app3.demarrer_dessin_libre(correction=True, couleur=VERT)
