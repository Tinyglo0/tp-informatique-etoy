---
hide:
    - navigation
    - toc
title: Jeu "plus ou moins"

---

Le jeu du « plus ou moins » consiste à deviner un nombre entier choisi entre 1 et 99.
Un élève décide de le coder en langage Python de la manière suivante :

- le programme génère un nombre entier aléatoire compris entre 1 et 99 ;
- si la proposition de l'utilisateur est plus petite que le nombre cherché, l'utilisateur en est averti. Il peut alors en tester un autre ;
- si la proposition de l'utilisateur est plus grande que le nombre cherché, l'utilisateur en est averti. Il peut alors en tester un autre ;
- si l'utilisateur trouve le bon nombre en 10 essais ou moins, il gagne ;
- si l'utilisateur a fait plus de 10 essais sans trouver le bon nombre, il perd.

!!! note "Note"

    La fonction `randint` est utilisée. Si `a` et `b` sont des entiers, `randint(a, b)` renvoie un nombre entier compris entre `a` et `b`, incluant les **deux bornes**.

???+ example "Exemple"

    ```pycon title=""
    >>> plus_ou_moins()
    Proposez un nombre entre 1 et 99 : 27
    Trop petit ! Testez encore : 78
    Trop grand ! Testez encore : 49
    Trop grand ! Testez encore : 31
    Trop petit ! Testez encore : 40
    Trop petit ! Testez encore : 43
    Trop grand ! Testez encore : 42
    Bravo ! Le nombre était  42
    ```

Compléter le script suivant. Cet exercice ayant une part d'aléatoire, il faut absolument cliquer sur le bouton de validation pour vérifier votre code.

{{ IDE('exo') }}

Si votre script est juste, vous pouvez le tester ci-dessous (Cliquer sur Exécuter le code)

{{ IDE('essai') }}


