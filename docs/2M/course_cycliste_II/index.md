---
hide:
    - navigation
    - toc
title: La course cycliste (II)

---



Une course cycliste se déroule sur un circuit permettant de nombreux dépassements.

![course](https://www.santafixie.fr/blogfr/wp-content/uploads/2025/02/courbe-distance-minimale-depassement.webp){.center title='ludovic from Guissény. (Bretagne, Finistère), France, CC BY-SA 2.0, via Wikimedia Commons'}

Chaque cycliste est identifié par un dossard sur lequel est inscrit son prénom : `#!py "Nadia"`, `#!py "Franck"`...
On garantit que tous les prénoms sont différents.

Leurs places dans le classement sont stockées de façon ordonnée dans une liste : le premier du classement se trouve à la première position de la liste, le deuxième à la deuxième position, etc... Par exemple `#!py classement_actuel = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]`. Nadia est la première et Laure la dernière.

Compléter la fonction `depasse`. Cette fonction prend en paramètres la liste `classement` qui stocke le classement provisoire de la course, et l'entier `place` qui représente la place du coureur qui va dépasser celui qui le précède. Cette fonction modifie la liste `classement` *en place* et représente la course après le dépassement.

??? warning "Modification *en place*"

    La liste `classement` est directement modifiée, **il ne faut pas construire une nouvelle liste**.

    Il est inutile de la renvoyer modifiée.

???+ example "Exemple"

    ```pycon title=""
    >>> classement_actuel = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
    >>> depasse(classement_actuel, 3)
    >>> classement_actuel
    ['Nadia', 'Thomas', 'Franck', 'Elizabeth', 'Laure']
    ```

On garantit que la liste `classement` contient au moins deux éléments et que l'entier `place`  est valide (compris entre `#!py 2` et le nombre de coureurs participants).


{{ IDE_versions('exo_a', 'exo_b', preferred=2, MAX=1000) }}
