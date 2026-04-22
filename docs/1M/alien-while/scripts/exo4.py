# --------- PYODIDE:env --------- #
## {{ [cwd]alien_python/.snippets:env | FIGURE -> 4 | SOLUCE -> "H08 I08 I09 I10 I11 I12 I13 J13 K13 K12 K11 K10 K09 K08 K07 K06 J06 I06 I07" }}
import re

# Security to limit infinite loops
oops = re.search(r'while\s+\.\.\.\s*:', __USER_CODE__)
assert not oops, "Le code ne sera pas exécuté car il y a un risque de boucle infinie."

# --------- PYODIDE:code --------- #
bas()
while ... :
    droite()
...

# --------- PYODIDE:corr --------- #
bas()                           # Une solution possible
while colonne() != "13":
    droite()
while ligne() != "K":
    bas()
while colonne() != "06":
    gauche()
while ligne() != "I":
    haut()
droite()

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}

complete()
lines(less=10)
wrongs = re.findall( r"\b(?:haut|bas|droite|gauche)\([^)]+\)",__USER_CODE__)
oops = ''.join(f"\n    {s}" for s in wrongs)
assert not oops, f"Les fonctions haut(), bas() ... doivent être utilisées sans paramètres. Code invalide trouvé :{ oops }"

# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}