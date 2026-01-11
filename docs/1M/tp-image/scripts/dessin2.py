# --------- PYODIDE:env --------- #
from pixel_art import *  # pour importer et utiliser le module pixel_art
import p5

app4 = App("dessin2")




app4.creer_image(11, 8)  # ligne obligatoire en début de chaque programme pour créer l'image

# première ligne :
app4.colorier(2,0,(0,255,0))
app4.colorier(8,0,(0,255,0))

# deuxième ligne :
app4.colorier(0,1,(0,255,0))
app4.colorier(3,1,(0,255,0))
app4.colorier(7,1,(0,255,0))
app4.colorier(10,1,(0,255,0))

# troisième ligne :
app4.colorier(0,2,(0,255,0))
app4.colorier(2,2,(0,255,0))
app4.colorier(3,2,(0,255,0))
app4.colorier(4,2,(0,255,0))
app4.colorier(5,2,(0,255,0))
app4.colorier(6,2,(0,255,0))
app4.colorier(7,2,(0,255,0))
app4.colorier(8,2,(0,255,0))
app4.colorier(10,2,(0,255,0))

for x in [0,1,2,4,5,6,8,9,10]:
    app4.colorier(x,3,(0,255,0))
    
for x in [1,2,3,4,5,6,7,8,9]:
    app4.colorier(x,4,(0,255,0))

# 6ème ligne :
for x in [2,3,4,5,6,7,8] :
    app4.colorier(x,5,(0,255,0))
# 7ème ligne :
for x in [3,8] :
    app4.colorier(x,6,(0,255,0))
# 8ème ligne :
for x in [2,3,8,9] :
    app4.colorier(x,7,(0,255,0))

app4.afficher_image()  # pour afficher l'image