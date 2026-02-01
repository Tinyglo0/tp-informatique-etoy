# Soldes

???+ question "Exercice 1 : promotions"

    🎁 Dans une parfumerie, on propose deux actions différentes pour l'achat de deux articles :  

    * Formule A : une réduction de 50% sur le prix du 2ème article (le moins cher)  
    * Formule B : une réduction de 20% sur le montant total à payer.  

    Muni d'un billet de 50 francs, Pierre souhaite offrir deux parfums à sa mère . 

    **1.**	Ecrire une fonction `promo_A` qui prend en paramètres `prix1` et `prix2` et qui renvoie le prix total à payer pour l’achat de deux parfums aux prix `prix1` et `prix2`.  

    Par exemple : 	
    
    * `promo_A(10, 20)` doit renvoyer `25`, et
    * `promo_A(20, 10)` doit également renvoyer `25`.

    {{IDE('scripts/promo_a')}}   

    **2.** Ecrire de même,  une fonction `promo_B`.   

    Par exemple : 	
    
    * `promoB(10, 20)` doit renvoyer 24
    * `promoB(20, 10)` doit également renvoyer 24.

    Compléter ci-dessous.

    {{ IDE('scripts/promo_b', MAX=1000) }}

    **3.** Ajouter le programme principal :  

    Il doit demander la saisie du prix des deux parfums, afficher le prix avec la formule A et la formule B, Afficher quelle est la formule la plus avantageuse, et si Pierre pourra offrir les deux parfums à sa mère (il ne dispose que de 50 euros).  
    Vous testerez votre code pour :  

    * Un parfum à 10 francs et un autre à 20 francs  
    * Un parfum à 12 francs et un autre à 45 francs  
    * Un parfum à 35 francs et un autre à 20 francs  

    Les fonctions `promo_A` et `promo_B` sont dans du code caché. Il est inutile de les écrire.

    {{IDE('scripts/promos')}} 
