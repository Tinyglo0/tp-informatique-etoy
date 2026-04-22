# Placement bancaire

On dépose une somme d'argent sur un compte rémunéré et on désire savoir combien d'années on doit attendre avant que la somme disponible sur ce compte ait atteint une valeur particulière. 

On souhaite aussi connaître la somme disponible réellement à cet instant, au centime de franc près.

??? info "Indice pour arrondir au centième de franc près"
    Pour arrondir au centième de franc, on peut utiliser la fonction `round` en python. Par exemple : 
    ```py 
    round(122.345435435,2)
    ```
    renvoie 122.35

!!! question "Exercice 1"

    Compléter la fonction `placement_bancaire_seuil(placement, taux, somme_cible)` pour qu'elle renvoie le nombre d'années et la somme finale (arrondie à 2 décimales).

    {{ IDE('exo', MAX=1000) }}
