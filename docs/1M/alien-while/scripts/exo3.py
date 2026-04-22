# --------- PYODIDE:env --------- #
## {{ [cwd]alien_python/.snippets:env | FIGURE -> 3 | SOLUCE -> "H08 I08 J08 K08 K09 L09 M09 M10 N10 O10 O11 N11" }}
import re

# Security to limit infinite loops
oops = re.search(r'n\s*=\s*\.\.\.', __USER_CODE__)
assert not oops, "Le code ne sera pas exécuté car il y a un risque de boucle infinie."

# --------- PYODIDE:code --------- #
bas()
n = 0
while n < ... :
    bas()
    ...
    ...
    n = ...
...



# --------- PYODIDE:corr --------- #
bas()                           # Une solution possible
n = 0
while n < 3:
    bas()
    bas()
    droite()
    n = n + 1
haut()

# --------- PYODIDE:tests --------- #
## {{ [cwd]alien_python/.snippets:tests }}

# --------- PYODIDE:secrets --------- #
## {{ [cwd]alien_python/.snippets:checks }}

complete()
lines(less=9)
wrongs = re.findall( r"\b(?:haut|bas|droite|gauche)\([^)]+\)",__USER_CODE__)
oops = ''.join(f"\n    {s}" for s in wrongs)
assert not oops, f"Les fonctions haut(), bas() ... doivent être utilisées sans paramètres. Code invalide trouvé :{ oops }"

# --------- PYODIDE:post --------- #
## {{ [cwd]alien_python/.snippets:tests }}