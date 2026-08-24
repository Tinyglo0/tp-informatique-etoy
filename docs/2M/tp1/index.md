---
hide: toc, navigation
title: TP1 - Listes
---

# TP1 : Exercices sur les listes

## Rappels

Supposons qu'on veuille écrire un programme gérant une liste de courses à faire, on ne sait pas combien d'éléments sont présents dans cette liste de courses. Bien sûr, on pourrait écrire quelque chose comme :

```python
# Une liste de courses ...
item1 = "oignons"
item2 = "huile"
item3 = "sel"
item4 = "chips"
item5 = "orange"
```

Cette solution n'est pas satisfaisante, en effet, si la liste contient plus de 5 items, il faudrait éditer le programme et y créer une variable `item6`.

De façon générale, on aimerait :

- ajouter facilement un élément à cette liste ?
- en enlever un ?
- savoir rapidement si un élément est présent ou non dans la liste ?
- avoir le nombre d'éléments présents dans la liste, ... ?

Une solution bien plus intéressante est d'utiliser une **liste** en Python.

### Ajout d'éléments dans une liste

Il est possible d'ajouter un élément à la fin d'une liste à l'aide de `append()`.

Exemple :
```python
liste = [1, 2, 3]
liste.append(4)
nombre = 5
liste.append(nombre)
print(liste) # Sortie : [1, 2, 3, 4, 5]
```

### Suppression d'éléments dans une liste

La fonction `remove()` permet de supprimer un élément présent dans une liste. Toutefois, seule la première occurrence sera supprimée s'elle apparaît plusieurs fois.

Exemple :
```python
pays = ["France", "Suisse", "Allemagne", "Italie", "Espagne"]
pays.remove("Allemagne")
print(pays) # Sortie ['France', 'Suisse', 'Italie', 'Espagne']
```

---

<!-- ??? question "Exercice 1 : Jours de la semaine"
    Pour le point 3) et 4) de cette exercice, vous mettrez un commentaire indiquant le type de parcours que vous utilisez.
    
    1) Créez la liste des sept jours de la semaine, en commençant par le lundi. Cette liste sera nommée `semaine`.
    2) Affichez cette liste en la parcourant à l'aide des indices.
    3) Même consigne mais en utilisant un parcours par élément.
    
    *Indication: Vous indiquerez à l'aide d'un commentaire quel code correspond à quelle boucle.*

    {{ IDE('scripts/exo1', MAX=1000) }}


??? question "Exercice 2 : Liste d'invités"
    Pour son anniversaire, Alice a invité ses amis : Hector, Paul, Jules, Marie, Pierre, Alphonsine, Dorothée, Eva, Jeannette, Kathy, Carole, et Zoé.
    
    **Tâche 1**

    1) Créez une liste `invites` représentant les invités d'Alice.
    2) Finalement, Alice rajoute Christian et Louis à sa liste et decide de ne plus inviter Kathy.
       Traduire ces modifications par des instructions Python. *(Le prénom Kathy doit toujours figurer dans la liste à sa création)*
    3) Affichez le nombre d'invités une fois ces remplacements effectués.

    {{ IDE('scripts/exo2_1', MAX=1000) }}
    
    **Tâche 2**

    On souhaite améliorer ce code afin qu'il demande à l'utilisateur s'il y a des noms à rajouter. S'il y en a, le programme devra les enregistrer dans la liste. À tout moment si l'utilisateur entre la lettre « q », le programme doit indiquer le nombre d'invités et leur noms avant de s'arrêter.

    4) Modifiez votre code pour prendre en compte ces contraintes.

    {{ IDE('scripts/exo2_2', MAX=1000) }}
-->


??? question "Exercice 1 : Listes de restaurants"
    Dans cet exercice, nous utiliserons un fichier contenant des informations sur des restaurants à New York.
    Les listes sont déjà chargées en mémoire pour vous. Voici un aperçu des premières valeurs de ces listes pour que vous sachiez à quoi elles ressemblent :

    ```python
    nom_restaurant = ['410', '1919', '2898', 'Abacrombie Fine Food', 'Abbey Pub'] # et d'autres...
    NPA = ['21206', '21231', '21214', '21202', '21230']
    district = ['Frankford', 'Fells Point', 'Hamilton', 'Downtown', 'Federal Hill']
    numero_district = [2, 1, 3, 11, 10]
    zone = ['NORTHEASTERN', 'SOUTHEASTERN', 'NORTHEASTERN', 'CENTRAL', 'SOUTHERN']
    adresse = ['4509 BELAIR ROAD Baltimore, MD', '1919 FLEET ST Baltimore, MD', '2898 HARFORD RD Baltimore, MD', '9 W CENTER ST Baltimore, MD', '1205 LIGHT ST Baltimore, MD']
    ```

    - La liste `nom_restaurant` contient la liste des noms des restaurants.
    - La liste `NPA` contient le NPA des différentes zones à New York.
    - La liste `district` contient la liste des quartiers dans lesquels se situent les restaurants (Il existe 14 quartiers).
    - La liste `numero_district` contient le numéro administratif du quartier (de 1 à 14).
    - La liste `zone` contient la zone géographique du restaurant.
    - La liste `adresse` contient l'adresse de chaque restaurant.

    **Tâche 1**

    1) Indiquez le nom du 220ème restaurant en l'affectant à la variable `reponse` :
    {{ IDE('scripts/exo3_1_1', MIN_SIZE=3, MAX=1000) }}

    2) Quels sont les noms des derniers et avant-derniers restaurants de la liste ? Affectez-les aux variables `avant_dernier` et `dernier` :
    {{ IDE('scripts/exo3_1_2', MIN_SIZE=3, MAX=1000) }}

    3) Quel est le numéro d'indice du restaurant nommé « PICCADELIS » ? Affectez-le à la variable `index_piccadelis` (Il faut utiliser une boucle pour trouver cette information)
    {{ IDE('scripts/exo3_1_3', SANS=".index", MIN_SIZE=3, MAX=1000) }}

    4) Ajoutez le nom d'un restaurant à la fin de la liste et vérifiez par une instruction en python qu'il a bien été ajouté.
    {{ IDE('scripts/exo3_1_4', MIN_SIZE=3, MAX=1000) }}

    5) Entrez une instruction permettant de changer le nom de « HUCKAS » en « HUCKAS BURGER » et vérifiez par une instruction en python qu'il a bien été modifié.
    {{ IDE('scripts/exo3_1_5', MIN_SIZE=3, MAX=1000) }}

    6) Entrez une instruction permettant de supprimer le nom « LOUISIANA » de la liste des restaurants et vérifiez par une instruction en python qu'il a bien été supprimé.
    {{ IDE('scripts/exo3_1_6', MIN_SIZE=3, MAX=1000) }}

    7) Comptez le nombre de restaurants situés dans le district de « Brooklyn » et affectez le résultat à `nombre_brooklyn` :
    {{ IDE('scripts/exo3_1_7', MIN_SIZE=3, MAX=1000) }}


    **Tâche 2**
    
    La partie suivante nécessite de revoir le concept de fonction en python.

    1) Créez une fonction `nombre_zone_geographique` qui prends en paramètres une zone géographique et une liste et qui renvoie le nombre de restaurants de cette zone.
    
    *Exemple* : `print(nombre_zone_geographique("CENTRAL", zone))` renvoie **288**.

    {{ IDE('scripts/exo3_2', MAX=1000) }}


??? question "Exercice 2 : Jeux Olympiques"
    Pour cet exercice, nous allons travailler avec une liste de villes hôtes des Jeux olympiques depuis le début des Jeux olympiques modernes en 1896) Notre liste comprendra les Jeux d'été et d'hiver. 
    Les listes sont déjà chargées en mémoire pour vous. Voici un aperçu :

    ```python
    year = ['1896', '1900', '1904', '1908', '1912'] # et d'autres...
    city = ['Athens', 'Paris', 'St. Louis', 'London', 'Stockholm']
    country = ['Greece', 'France', 'United States', 'United Kingdom', 'Sweden']
    season = ['Summer', 'Summer', 'Summer', 'Summer', 'Summer']
    ```

    - La liste `year` contient l'année ou ont eu lieu les JO.
    - La liste `city` contient la ville qui a accueillie les jeux.
    - La liste `country` contient le pays où se sont tenus les JO.
    - La liste `season` pour savoir si les jeux se sont déroulés en hiver (winter) ou en été (summer).

    **Travail à faire**

    Modifier le code pour obtenir les informations suivantes :

    1) Créez une liste `villes_hiver` contenant toutes les villes qui ont organisé les jeux en hiver (Winter).
    {{ IDE('scripts/exo4_1', MIN_SIZE=5, MAX=1000) }}

    2) Créez une liste `villes_uk` contenant les villes des jeux qui ont été organisés par le Royaume Uni (United Kingdom).
    {{ IDE('scripts/exo4_2', MIN_SIZE=5, MAX=1000) }}

    3) Comptez le nombre de fois que Londres a organisé les JO et affectez ce nombre à la variable `nombre_londres`.
    {{ IDE('scripts/exo4_3', MIN_SIZE=5, MAX=1000) }}

    4) Affectez à la variable `ville_2016` le nom de la ville qui a organisé les JO en '2016' en parcourant les listes de données.
    {{ IDE('scripts/exo4_4', MIN_SIZE=5, MAX=1000) }}

