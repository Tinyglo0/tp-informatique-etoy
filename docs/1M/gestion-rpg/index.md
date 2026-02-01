---
hide:
    - navigation
    - toc
title: Combat RPG
---

Dans ce jeu de rôle, on souhaite calculer les points de vie (PV) restants d'un personnage après avoir reçu une attaque.
Le calcul dépend de la force de l'attaquant, de son arme, et de l'armure du défenseur.

??? question "Force de frappe"

    La puissance d'une attaque dépend de la force naturelle du héros et du bonus apporté par son épée.
    
    La formule est une simple addition : 

    $$ \text{Puissance} = \text{Force} + \text{Bonus Arme} $$

    Écrire la fonction `calculer_puissance` qui prend en paramètres :
    
    * `force` (nombre entier) ;
    * `bonus_arme` (nombre entier).
    
    Elle renvoie la puissance totale de l'attaque.

    ```pycon
    >>> calculer_puissance(80, 20)
    100
    ```

    {{IDE('exo1', MAX=1000)}}

??? question "Réduction des dégâts"

    L'armure de la cible absorbe une partie du choc. Cette absorption est calculée grâce à un *coefficient de réduction*.
    
    $$ \text{Absorption} = \text{Armure} \times \text{Coeff} $$

    *Exemple : Si j'ai 50 points d'armure et un coefficient de 0.5, j'absorbe $50 \times 0.5 = 25$ points de dégâts.*

    Écrire la fonction `calculer_absorption` qui prend en paramètres :
    
    * `armure` (entier) ;
    * `coeff` (nombre flottant, ex: 0.5).
    
    Elle renvoie le nombre de points de dégâts absorbés.

    ```pycon
    >>> calculer_absorption(50, 0.5)
    25.0
    ```

    {{IDE('exo2', MAX=1000)}}

??? question "Dégâts réels"

    Les dégâts réellement subis par le personnage sont la puissance de l'attaque moins ce qui a été absorbé par l'armure.

    $$\text{Dégâts} = \text{Puissance} - \text{Absorption}$$

    Écrire la fonction `calculer_degats` qui prend en paramètres `puissance` et `absorption` et renvoie le résultat de la soustraction.
    
    *(Pour cet exercice, on considère que l'absorption n'est jamais supérieure à la puissance).*

    ```pycon
    >>> calculer_degats(100, 25)
    75
    ```

    {{IDE('exo3', MAX=1000)}}


??? question "Points de vie restants"

    C'est le moment de tout combiner !
    
    On veut savoir combien de PV il reste au personnage après l'attaque.
    La fonction finale `pv_restants` doit prendre en paramètres :
    
    1. `pv_actuels` (La vie du personnage avant le coup)
    2. `force` (La force de l'attaquant)
    3. `bonus_arme` (Le bonus de l'épée)
    4. `armure` (L'armure du défenseur)
    5. `coeff` (Le coefficient de protection)

    **Objectif :** Vous devez calculer la puissance, puis l'absorption, en déduire les dégâts et enfin soustraire ces dégâts aux PV actuels.
    
    ⚠️ **Impératif :** Vous devez réutiliser les fonctions `calculer_puissance`, `calculer_absorption` et `calculer_degats`.

    ```pycon
    >>> pv_restants(200, 80, 20, 50, 0.5)
    125.0
    ```
    *Explication : Attaque de 100, Absorption de 25. Dégâts subis = 75. Vie restante = 200 - 75 = 125.*

    {{ IDE('exo4', STD_KEY="1234", MAX=1000) }}