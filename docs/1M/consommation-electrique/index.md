---
hide:
    - navigation
    - toc
title: Consommation d'énergie
---

On souhaite calculer l'énergie consommée par un appareil électrique à l'aide de la *tension* (exprimée en volt) et de l'*intensité* (exprimée en ampère) du courant qui le traverse.


??? question "Puissance d'un appareil"

    La *puissance électrique* (exprimée en watt) consommée à chaque instant par un appareil est définie par : tension $\times$ intensité (la tension est en volt et l'intensité en ampère).

    La puissance d'un four électrique traversé par un courant de $230~\text{V}$ et d'intensité $20~\text{A}$ est donc de $230 \times 20 = 4600~\text{W}$ 

    Écrire la fonction `puissance_appareil` qui prend en paramètres les nombres `tension`, et `intensite` représentant respectivement la tension et l'intensité utilisées fournies respectivement en volt et ampère. Cette fonction renvoie la puissance d'un appareil électrique en watt.

 
    ```pycon
    >>> puissance_appareil(230, 20)
    4600
    ```

    {{ remarque('assertion') }}

    {{IDE('exo1', MAX=1000)}}

??? question "Energie consommée"

    L'*énergie consommée* (exprimée en watt-heure) par l'appareil pendant une durée donnée (exprimée en heure) est calculée par : puissance $\times$ durée (la puissance est ici en watt).

    Ainsi, l'utilisation du four de puissance $4\,600$ W pendant $1$ h $30$ min consommera $4\,600 \times 1,5 =  6\,900~\text{Wh}$


    Écrire la fonction `energie_consommee` qui prend en paramètres les nombres `puissance` et `temps` représentant respectivement la puissance de l'appareil (en watt), et sa durée d'utilisation (en heure). Cette fonction renvoie l'énergie consommée (en watt-heure).

    ```pycon
    >>> energie_consommee(4600, 1.5)
    6900.0
    ```

    {{IDE('exo2', MAX=1000)}}

??? question "Coût d'utilisation"

    Le prix moyen de l'électricité est de $0,158\,2~\text{CHF/kWh}$.

    Ainsi, l'utilisation du four pendant $0$ h $30$ min coûtera environ $1,09~\text{CHF}$, arrondi au centime près.

    Ecrire la fonction `cout_utilisation` qui prend en paramètres les nombres `energie`, et `prix_base` qui représentent respectivement l'énergie consommée (en kWh) et le prix moyen de l'électricité (en CHF/kWh). Cette fonction renvoie le prix d'utilisation arrondi au centime près d'un appareil électrique.
    
    ```pycon
    >>> cout_utilisation(6.9, 0.1582)
    1.09
    ```

    On pourra utiliser la fonction `#!py round` qui permet d'arrondir un nombre à une précision donnée.

    ```pycon
    >>> round(4.52463, 3)  # arrondi à 3 décimales
    4.524
    ```

    {{IDE('exo3', MAX=1000)}}


??? question "Coût de la consommation"

    Écrire la fonction `cout_consommation` qui renvoie le prix de la consommation (arrondi au centime) d'un appareil électrique.
    Cette fonction prend en paramètres :

    * un nombre `tension` qui est la tension d'utilisation de l'appareil (en V) ;
    * un nombre `prix` qui est le prix du kWh (en CHF/kWh) ;
    * un nombre `intensite` qui est l'intensité du courant traversant l'appareil (en A) ;
    * un nombre `duree` qui est la durée d'utilisation de l'appareil (en heure).
    
    On réutilisera **impérativement** toutes les fonctions déjà créées.

    ```pycon
    >>> cout_consommation(230, 0.1582, 20, 1.5)
    1.09
    ```

    ??? tip "Astuce"

        Attentions aux unités utilisées : $1 \text{kWh} = 1\,000 {Wh}$


    {{ IDE('exo4',STD_KEY="1234", MAX=1000) }}

