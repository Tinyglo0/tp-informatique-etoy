---
hide:
    - navigation
    - toc
title: Alien Python - Boucle while
---

Pour les questions suivantes, dessinez le parcours de l'alien en cliquant sur **la case d'arrivée** de chaque instruction exécutée. Vous pourrez ensuite valider votre parcours pour vérifier s'il est correct.

!!! tip "Autres fonctions !"

    Trois autres fonctions permettent de situer l'alien dans la grille :

    * `case()` renvoie la case sur laquelle se trouve l'alien, de `"A01"` à `"O15"` ;
    * `ligne()` renvoie la ligne de la case sur laquelle se trouve l'alien, de `"A"` à `"O"` ;
    * `colonne()` renvoie la colonne de la case sur laquelle se trouve l'alien, `"01"` à `"15"`.

??? info "Consignes"
    Dans cet exercice, on trouve deux types de questions :

    * **Dessinez le parcours** : dessinez le parcours de l'alien en cliquant sur **la case d'arrivée** de chaque instruction exécutée. Vous pourrez ensuite valider votre parcours pour vérifier s'il est correct.

    * **Codez le parcours** : écrire le code nécessaire pour obtenir le déplacement souhaité (les numéros correspondent aux différentes étapes).

    !!! warning "Attention"
        En fonction de la question, il y aura une limitation du nombre de lignes.

!!! abstract "Boucle conditionnelle"
    Une **boucle conditionnelle**, permet de répéter plusieurs fois une séquence d'instructions, en fonction d'une condition évaluée avant chaque répétition de cette séquence.

    À chaque étape, les instructions indentées sont répétées
    :warning: Ne pas oublier de modifier ce qui est évalué dans la condition, sous peine d'avoir une boucle infinie. Dans ce cas le programme tourne sans fin.

    ```python { .inline .w45}
    n = 0
    while n < 4:
        haut()
        n = n + 1
    ```

    ```python { .inline .end .w45}
    while colonne() > '02':
        gauche()
    ```

!!! abstract "Boucle while – boucle for"

    Ces deux boucles sont équivalentes :

    ```python { .inline .w45}
    n = 0
    while n < 4:
        haut()
        n = n + 1
    ```

    ```python { .inline .end .w45}

    for n in range(4):
        haut()

    ```

{{ alien_dessin(1) }}

{{ alien_dessin(2) }}

{{ alien_dessin(11, num_question="3") }}

{{ alien_dessin(12, num_question="4") }}

<br>

---


Pour les deux questions suivantes écrire le code nécessaire pour obtenir le déplacement souhaité (les numéros correspondent aux différentes étapes), en respectant les conditions suivantes :

1. Le nombre de lignes de code est limité (9 pour la question 5 et 10 pour la question 6).
1. Les fonctions `bas`, `haut`, `droite` et `gauche` doivent toujours être appelées sans argument, ici.
1. Les boucles `for` sont interdites.

<br>

{{ alien_IDE(3, SANS="AST: for",  num_question="5") }}

{{ alien_IDE(4, SANS="AST: for", header="Il faudra utiliser au moins deux boucles conditionnelles.", num_question="6") }}

<!-- <style>
.md-typeset .w5  , .w5  { width: 5%;  }
.md-typeset .w10 , .w10 { width: 10%; }
.md-typeset .w15 , .w15 { width: 15%; }
.md-typeset .w20 , .w20 { width: 20%; }
.md-typeset .w25 , .w25 { width: 25%; }
.md-typeset .w30 , .w30 { width: 30%; }
.md-typeset .w35 , .w35 { width: 35%; }
.md-typeset .w40 , .w40 { width: 40%; }
.md-typeset .w45 , .w45 { width: 45%; }
.md-typeset .w50 , .w50 { width: 50%; }
.md-typeset .w55 , .w55 { width: 55%; }
.md-typeset .w60 , .w60 { width: 60%; }
.md-typeset .w65 , .w65 { width: 65%; }
.md-typeset .w75 , .w75 { width: 75%; }
.md-typeset .w80 , .w80 { width: 80%; }
.md-typeset .w90 , .w90 { width: 90%; }
.md-typeset .w100, .w100{ width: 100%; } 
</style> -->