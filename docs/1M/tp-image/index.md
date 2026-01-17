---
hide:
    - navigation
    - toc
title: Créer une image
---

# Comprendre les coordonnées

Une image numérique est constituée de pixels, chaque pixel ayant des coordonnées : une abscisse et une ordonnée, notées respectivement `x` et `y` dans la suite.

!!! warning "Attention"

    - On commence la numérotation à partir de 0, ainsi le pixel en haut à gauche de l’image a pour coordonnées $(0 ; 0)$.

    - L’axe des ordonnées est dirigé vers le bas !

## Exemple
On suppose ici que l’on dispose d’une fonction `colorier(x, y)` qui permet de colorier le pixel de coordonnées `(x, y)` (en gris).

Voici un exemple d'utilisation pour comprendre le rôle de la fonction `colorier` :
```python
creer_image(9, 9)  # ligne obligatoire en début de chaque programme pour créer l'image

colorier(3, 7)  # on colorie un pixel
```
On obtient une image de dimension 9*9 pixels, avec le pixel aux coordonnées (3, 7) colorié :
{{ run('scripts/dessin1') }}
{{ figure("dessin") }}


??? question "Question 1"
    ```python { .inline .end .w45 }
    creer_image(9,9)

    colorier(4, 2)
    colorier(4, 3)
    colorier(4, 5)
    colorier(4, 6)

    colorier(2, 4)
    colorier(3, 4)
    colorier(4, 4)
    colorier(5, 4)
    colorier(6, 4)
    ```
    {{ run('scripts/exo1') }}
    {{ figure("figure1") }}




??? question "Question 2"
    Vous devez écrire le code nécessaire pour obtenir l'image souhaitée.
    {{ run('scripts/grille1') }}
    {{ figure("grille1") }}

    {{ IDE('scripts/exo2') }}
    {{ figure("figure2") }}

!!! abstract "Couleurs"

    Il est possible de passer un troisième **argument** à la fonction `colorier` afin de spécifier la couleur du pixel.

    On dispose des couleurs suivantes : `BLANC`, `NOIR`, `VERT`, `ROUGE`, `BLEU`, `ROSE`, `BLEU`, `JAUNE`.

Dans la suite de l'exercice, on souhaite créer le dessin suivant :
{{ run('scripts/dessin2') }}
{{ figure("dessin2") }}
Nous allons pour ceci procéder par étape en répondant aux questions suivantes.


??? question "Question 3"
    ```python { .inlinee .end .w45 }
    # image de 3 lignes de 11 colonnes
    creer_image(11, 3)

    # ligne 0 :
    colorier(2, 0, VERT)
    colorier(8, 0, VERT)

    # ligne 1 :
    colorier(0, 1, VERT)
    colorier(3, 1, VERT)
    colorier(7, 1, VERT)
    colorier(10, 1, VERT)

    # ligne 2 :
    colorier(0, 2, VERT)
    colorier(2, 2, VERT)
    colorier(3, 2, VERT)
    colorier(4, 2, VERT)
    colorier(5, 2, VERT)
    colorier(6, 2, VERT)
    colorier(7, 2, VERT)
    colorier(8, 2, VERT)
    colorier(10, 2, VERT)
    ```
    {{ run('scripts/exo3') }}
    {{ figure("figure3") }}

!!! abstract "Répétitions"
    On peut constater que le coloriage de la troisième ligne (d'odonnée $2$) est très répétitif, alors que seule la cordonnées en x change d'une ligne à l'autre.
    Ainsi, on aurait pu écrire cette même ligne avec le code suivant :
    ```python title=""
    for x in [0, 2, 3, 4, 5, 6, 7, 8, 10]:
        colorier(x, 2, VERT)
    ```

??? question "Question 4"
    Vous devez écrire le code nécessaire pour obtenir les lignes aux ordonnées $3$ et $4$ de l'image souhaitée.

    {{ IDE('scripts/exo4') }}
    {{ figure("figure4") }}


!!! abstract "Répétitions"
    Le code précédent se concentre sur les pixels à colorier.

    En pratique, une ligne de l'image est stockée par une liste de couleurs.
    ```python title=""
    ligne_2 = [VERT, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC, VERT]
    ```
    Ainsi l'expression `ligne_2[0]` donne la couleur du pixel situé à l'abscisse $0$. De manière plus générale, l'expression `ligne_2[x]` donne la couleur du pixel situé à l'abscisse `x`.

    On peut parcourir l'ensemble des valeurs du tableau pour colorier la ligne entière :
    ```python title=""
    for x in range(NB_COLONNES):
        colorier(x, 2, ligne_2[x])
    ```

??? question "Question 5"
    cliquer sur les pixels à colorier en vert :
    ```python { .inlinee .end .w45 }
    NB_COLONNES = 11
    ligne_5 = [BLANC, BLANC, VERT, VERT, VERT, VERT, VERT, VERT, VERT, BLANC, BLANC]
    for x in range(NB_COLONNES):
        colorier(x, 0, ligne_5[x])
    ```
    {{ run('scripts/exo5') }}
    {{ figure("figure5") }}


??? question "Question 6"
    Vous devez écrire le code nécessaire pour obtenir les lignes aux ordonnées $6$ et $7$ de l'image souhaitée.

    {{ IDE('scripts/exo6') }}
    {{ figure("figure6") }}

!!! abstract "Répétitions de boucle"
    On constate qu'il y a toujours des répétitions, puisque la construction de chaque ligne de l'image nécessite une boucle, alors que seuls l'ordonnée et le tableau de couleurs changent.

    On peut alors regrouper l'ensemble des lignes dans un tableau :
    ```python title=""
    image = [ligne_0, ligne_1, ligne_2, ligne_3, ligne_4, ligne_5, ligne_6, ligne_7]
    ```
    Ainsi l'expression `image[3]` donne la ligne située à l'ordonnée $3$. De manière plus générale, l'expression `image[y]` donne la ligne située à l'ordonnée `y`.

    On peut alors parcourir l'ensemble des lignes de l'images :
    ```python title=""
    for y in range(NB_LIGNES):
        ligne = image[y]
        for x in range(NB_COLONNES):
            colorier(x, y, ligne[x])
    ```

??? question "Question 7"
    Cliquer sur les pixels à colorier en bleu :
    ```python { .inlinee .end}
    NB_LIGNES = 6
    NB_COLONNES = 9
    image = [[BLANC, BLANC, BLANC, BLEU, BLANC, BLEU, BLANC, BLANC, BLANC],
            [BLEU, BLANC, BLEU, BLEU, BLEU, BLEU, BLEU, BLANC, BLEU],
            [BLEU, BLEU, BLEU, BLANC, BLEU, BLANC, BLEU, BLEU, BLEU],
            [BLANC, BLEU, BLEU, BLEU, BLEU, BLEU, BLEU, BLEU, BLANC],
            [BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC],
            [BLEU, BLEU, BLANC, BLANC, BLANC, BLANC, BLANC, BLEU, BLEU]
            ]
    for y in range(NB_LIGNES):
        ligne = image[y]
        for x in range(NB_COLONNES):
            colorier(x, y, ligne[x])
    ```
    {{ run('scripts/exo7') }}
    {{ figure("figure7") }}

??? question "Question 8"
    Vous devez écrire le code nécessaire pour obtenir l'image souhaitée.
    {{ run('scripts/dessin3') }}
    {{ figure("dessin3") }}

    {{ IDE('scripts/exo8') }}
    {{ figure("figure8") }}