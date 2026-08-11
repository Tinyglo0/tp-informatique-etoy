---
author: Pierre Marquestaut
hide:
    - navigation
    - toc
title: La course cycliste (I)
---

Une course cycliste se dispute. 

![Les coureurs - source : Wikimedia ](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/V%C3%A9locourse.jpg/330px-V%C3%A9locourse.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=thumbnail){ .center }

Chaque participant est identifié par son prénom : `#!py "Nadia"`, `#!py "Franck"`. On garantit que tous les prénoms sont différents.

Durant la course, les cyclistes se doublent les uns les autres, le classement évolue. À chaque instant, les positions des coureurs dans le classement sont stockées de façon ordonnée dans un tableau : le premier du classement se trouve à la première position du tableau, le deuxième à la deuxième position, *etc*.

Par exemple avec `#!py classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]`, Nadia est la première du classement et Laure la dernière.

On demande d'écrire plusieurs fonctions autour cette situation.

??? question "Fonction `nombre_coureurs`"

    La fonction `nombre_coureurs` prend en paramètre le tableau `classement` et renvoie le nombre de participants à la course.
    
     ```pycon
     >>> classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
     >>> nombre_coureurs(classement)
     5
     ```
    
    {{ IDE('./pythons/exo_nombre', MAX=1000)}}

??? question "Fonction `premier`"

    La fonction `premier` prend en paramètre le tableau `classement` et renvoie le nom du coureur en première position.
    
     ```pycon
     >>> classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
     >>> premier(classement)
     'Nadia'
     ```
    
    {{ IDE('./pythons/exo_premier', MAX=1000)}}

??? question "Fonction `dernier`"

    La fonction `dernier` prend en paramètre le tableau `classement` et renvoie le nom du coureur en dernière position.
    
     ```pycon
     >>> classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
     >>> dernier(classement)
     'Laure'
     ```
    
    {{ IDE('./pythons/exo_dernier', MAX=1000)}}


??? question "Fonction `coureur_en_position`"

    La fonction `coureur_en_position` prend en paramètre le tableau `classement` et un entier `position` et renvoie le nom du coureur à cette position.
    

    On garantit que la position passée en argument à cette fonction est valide (comprise entre 1 et le nombre de coureurs participants).
    
     ```pycon
     >>> classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
     >>> coureur_en_position(classement, 1)
     'Nadia'
     >>> coureur_en_position(classement, 3)
     'Thomas'
     ```
    
    {{ IDE('./pythons/exo_position', MAX=1000)}}
