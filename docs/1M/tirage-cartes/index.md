# Tirage de cartes

On considère le jeu suivant :

- On choisit au hasard une carte dans un jeu classique de 32 cartes.
- Si la carte tirée est un as, on s'arrête ; sinon, on la remet dans le paquet et on recommence.

On s'intéresse au nombre de tirages que l'on doit effectuer pour obtenir un as pour la première fois. 

??? info "Générer des nombres aléatoires"

    Pour générer des nombres entiers de manière aléatoire en Python, on utilise généralement la fonction `randint` du module `random`.
    Il faut d'abord importer cette fonction au début de son script :
    
    ```python
    from random import randint
    ```

    Puis, pour obtenir un entier aléatoire entre 1 et 10 (inclus), on écrit :
    
    ```python
    nb_mystere = randint(1, 10)
    ```

!!! question "Exercice"

    Complétez la fonction ci-dessous (on considère que les 4 as sont les nombres de 1 à 4 dans un tirage entre 1 et 32).

    {{ IDE('exo', MAX=1000) }}
