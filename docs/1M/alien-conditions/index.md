---
hide:
    - navigation
    - toc
title: Alien - Instructions conditionnelles
build:
    extra_pyodide_sections: ['dessin']
---


Les règles sont simples : l'alien 👽 se situe au départ au centre de la grille et peut être déplacé avec les fonctions `haut`, `bas`, `gauche` et `droite`.

L'objectif est de trouver la case finale de l'alien (et donc son parcours) après exécution du programme donné.

!!! tip "Nouvelles fonctions !"

    Trois autres fonctions permettent de situer l'alien dans la grille :

    * `case()` renvoie la case sur laquelle se trouve l'alien, de `"A01"` à `"O15"` ;
    * `ligne()` renvoie la ligne de la case sur laquelle se trouve l'alien, de `"A"` à `"O"` ;
    * `colonne()` renvoie la colonne de la case sur laquelle se trouve l'alien, `"01"` à `"15"`.

Pour les questions suivantes, dessinez le parcours de l'alien en cliquant sur **la case d'arrivée** de chaque instruction exécutée. Vous pourrez ensuite valider votre parcours pour vérifier s'il est correct.

!!! abstract "Instruction conditionnelle"

    Une **instruction conditionnelle**, ou instruction de test, permet de *faire des choix* en fonction de la valeur d'une *condition*. On parle souvent d'une instruction « *si ... alors* », ou « *if ... else* » en anglais.

    ```python
    if condition_1:
        bloc_instructions_1
    elif condition_2:
        bloc_instructions_2
    else:
        bloc_instructions_3
    ```

    Le code ci-dessus indique que si la `condition_1` est vraie, on n'exécute que `bloc_instruction_1`, sinon on regarde si `condition_2` est vraie, on n'exécute que `bloc_instruction_2`, et si les deux conditions sont fausses, on n'exécute que `bloc_instruction_3`

    Les mots-clés « `#!py if` », « `#!py elif` » (contraction de *else if*) et « `#!py else` » sont les traductions respectives de « si », « sinon si » et « sinon ».

???+ abstract "Comparaison"

    Une **condition** est une instruction qui est soit vraie, soit fausse. On dit qu'il s'agit d'une **expression booléenne**.

    Pour tester des inégalité larges (comme $a \leqslant b$ et $a \geqslant b$) ou la différence (comme $a\neq b$) on utilise les syntaxes suivantes :

    - le signe `<=` pour *inférieur ou égal* ;

    - le signe `>=` pour *supérieur ou égal* ;

    - le signe `!=` pour *n'est pas égal à*.

    On peut résumer les tests possibles dans le tableau ci-dessous :
    
    | Test                       | Syntaxe Python |
    | -------------------------- | -------------- |
    | $a=b$                      | `a == b`       |
    | $a\neq b$                  | `a != b`       |
    | $a<b$                      | `a < b`        |
    | $a\leqslant b$             | `a <= b`       |
    | $a>b$                      | `a > b`        |
    | $a\geqslant b$             | `a >= b`       |
    | $a<b<c$                    | `a < b < c`    |
    | $a\leqslant b \leqslant c$ | `a <= b <= c`  |
    | $a<b\leqslant c$           | `a < b <= c`   |

    ??? example "Examples"
        ```pycon title=""
        >>> 15 >= 10
        False
        >>> 5 < 10
        True
        >>> 32 < 32
        False
        ```

???+ warning "Comparaison de chaines de caractères"
    Lorsque l'on compare deux chaines de caractères entre elles, on les compare selon l'ordre alphabétique, caractère par caractère.

    !!! example "Examples"
    ```pycon title=""
    >>> "A" >= "B"
    False
    >>> "01" < "15"
    True
    >>> "code" < "mode"
    True
    >>> "2" < "15"
    True
    ```

???+ warning "Source d'erreur classique"
    Le test d'égalité entre deux variables se fait avec un double égal `==` (car le simple `=` a un rôle différent : celui d'affecter une valeur à une variable).



{{ alien_dessin(1) }}

{{ alien_dessin(2) }}

{{ alien_dessin(3) }}

{{ alien_dessin(4) }}



Pour les questions suivantes écrire le code nécessaire pour obtenir le déplacement souhaité (les numéros correspondent aux différentes étapes).



{{ alien_IDE(5) }}

{{ alien_IDE(6) }}

{{ alien_IDE(7) }}