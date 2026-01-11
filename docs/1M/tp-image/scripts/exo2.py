# --------- PYODIDE:env --------- #
from pixel_art import * 
import p5

app.nouveau("figure2") 


# --------- PYODIDE:code --------- #
creer_image(..., ...) 

colorier(...,...) 
colorier(...,...) 
colorier(...,...) 
colorier(...,...) 
colorier(...,...) 
colorier(...,...) 
colorier(...,...) 
colorier(...,...) 



# --------- PYODIDE:post --------- #
grille_souhaitee = [[BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,GRIS,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,GRIS,BLANC,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,GRIS,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    [BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC,BLANC],
                    ]
app.verifier_programme(grille_souhaitee)