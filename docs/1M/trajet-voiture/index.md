---
hide:
    - navigation
    - toc
title: Planification de trajet
---

On souhaite estimer le coût en carburant d'un trajet en voiture en fonction de la vitesse, de la durée du voyage et des caractéristiques du véhicule.

??? question "Distance parcourue"

    La distance parcourue (en km) est définie par la formule : $d = v \times t$.
    
    * $v$ est la vitesse moyenne en km/h.
    * $t$ est la durée du trajet en heures.

    Par exemple, si je roule à $110~\text{km/h}$ pendant $2$ heures, je parcours $110 \times 2 = 220~\text{km}$.

    Écrire la fonction `calculer_distance` qui prend en paramètres les nombres `vitesse` et `temps`. Cette fonction renvoie la distance parcourue en km.

    ```pycon
    >>> calculer_distance(110, 2)
    220
    ```

    {{IDE('exo1', MAX=1000)}}

??? question "Carburant nécessaire"

    La consommation d'une voiture est souvent indiquée en "litres aux 100 km" (L/100km).
    Pour calculer le nombre de litres nécessaires, on utilise la formule : 
    
    $$ \text{Litres} = \frac{\text{Distance} \times \text{Consommation aux 100}}{100} $$

    Par exemple, pour faire $220~\text{km}$ avec une voiture qui consomme $6~\text{L/100km}$, il faut : $(220 \times 6) / 100 = 13,2~\text{L}$.

    Écrire la fonction `calculer_carburant` qui prend en paramètres :
    
    * `distance` (en km) ;
    * `conso_100` (la consommation du véhicule en L/100km).
    
    Cette fonction renvoie le nombre de litres de carburant nécessaires.

    ```pycon
    >>> calculer_carburant(220, 6)
    13.2
    ```

    {{IDE('exo2', MAX=1000)}}

??? question "Coût du plein"

    Si l'essence coûte $1,85~\text{€/L}$, alors $13,2$ litres coûteront : $13,2 \times 1,85 = 24,42~\text{€}$.

    Écrire la fonction `calculer_cout` qui prend en paramètres :
    
    * `litres` (le volume de carburant) ;
    * `prix_litre` (le prix d'un litre d'essence).
    
    Cette fonction renvoie le coût total arrondi à 2 décimales (centimes).
    
    On rappelle que la fonction `round(x, 2)` permet d'arrondir `x` à 2 chiffres après la virgule.

    ```pycon
    >>> calculer_cout(13.2, 1.85)
    24.42
    ```

    {{IDE('exo3', MAX=1000)}}


??? question "Coût total du trajet"

    Écrire la fonction `cout_trajet` qui renvoie le prix total du voyage (arrondi au centime).
    Cette fonction prend en paramètres 4 nombres :

    1. `vitesse` (km/h)
    2. `temps` (heures)
    3. `conso_100` (L/100km)
    4. `prix_litre` (€/L)
    
    ⚠️ **Contrainte importante :** Vous devez **impérativement** réutiliser les trois fonctions créées précédemment (`calculer_distance`, `calculer_carburant` et `calculer_cout`) à l'intérieur de cette nouvelle fonction pour effectuer les calculs.

    ```pycon
    >>> cout_trajet(110, 2, 6, 1.85)
    24.42
    ```

    {{ IDE('exo4', STD_KEY="1234", MAX=1000) }}