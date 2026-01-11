# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app6 = App("grille1")

app6.creer_image(9, 9) 

app6.colorier(2, 3) 
app6.colorier(3, 2)  
app6.colorier(4, 1)  
app6.colorier(4, 2)  
app6.colorier(4, 3)  
app6.colorier(4, 4)  
app6.colorier(4, 5)  
app6.colorier(4, 6)  

app6.afficher_image()  # pour afficher l'image