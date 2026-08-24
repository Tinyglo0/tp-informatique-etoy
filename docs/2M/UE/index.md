# Les pays de l'Union Européenne

On donne la liste des pays de l'Union européenne (UE), ainsi que la liste des capitales correspondantes et la liste des nombres d'habitants (en millions d'habitants).
    
```python
pays = ['Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande','France','Grèce', 'Hongrie', 'Irlande', 'Italie', 'Lettonie', 'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas','Pologne', 'Portugal', 'République tchèque', 'Roumanie', 'Slovaquie', 'Slovénie', 'Suède']
capitale = ['Berlin', 'Vienne', 'Bruxelles', 'Sofia', 'Nicosie', 'Zagreb', 'Copenhague', 'Madrid', 'Tallinn', 'Helsinki','Paris', 'Athènes', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'La Valette', 'Amsterdam','Varsovie', 'Lisbonne', 'Prague','Bucarest', 'Bratislava', 'Ljubljana', 'Stockholm']
population = [83.16, 8.98, 11.75, 6.45, 0.90, 3.85, 5.93, 47.43, 1.37, 5.56,68.4, 10.71, 9.60, 5.27, 58.98, 1.88, 2.9, 0.66, 0.54, 17.81, 36.7, 10.5, 10.7, 19.06, 5.43, 2.11, 10.45]
```
    
Répondez aux questions suivantes en écrivant les instructions en Python (les listes sont déjà chargées dans l'environnement de la console, vous n'avez pas besoin de les redéfinir).

1. Combien y a-t-il de pays dans l'UE ?
{{ IDE('ex1_1', MAX=1000) }}

2. Quel est le nombre total d'habitants de l'UE ? (l'utilisation de la fonction `sum` n'est pas autorisée)
{{ IDE('ex1_2', MAX=1000,SANS="sorted, max, sum, min") }}

3. Quel est le pays le plus peuplé de l'UE ? (l'utilisation de la fonction `max` n'est pas autorisée)
{{ IDE('ex1_3', MAX=1000,SANS="sorted, max, sum,min") }}

4. Quel est le pays le moins peuplé de l'UE ? (l'utilisation de la fonction `min` n'est pas autorisée)
{{ IDE('ex1_4', MAX=1000,SANS="sorted, max, sum,min") }}

5. Ecrire un programme qui affiche un pays de l'UE au hasard, ainsi que sa capitale et son nombre d'habitants.
{{ IDE('ex1_5', MAX=1000,SANS="sorted, max, sum,min") }}

6. Ecrire un programme qui demande à l'utilisateur de saisir le nom d'un pays de l'UE et qui affiche la capitale de ce pays.
{{ IDE('ex1_6', MAX=1000,SANS="sorted, max, sum,min") }}
