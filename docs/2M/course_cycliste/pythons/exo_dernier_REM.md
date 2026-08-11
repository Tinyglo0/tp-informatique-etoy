On pouvait également opter pour la solution suivante :

```python
def dernier(classement):
    taille = nombre_coureurs(classement)  # renvoie len(classement)
    return classement[taille - 1]
```

Dans ce cas, Python autorise un raccourci. Au lieu d'indiquer l'indice `#!py taille -1`, on peut simplement noter `#!py -1`.
La fonction devient alors :

```python
def dernier(classement):
    return classement[-1]
```

Dans le même esprit, l'avant-dernier élément d'un tableau a pour indice *négatif* `#!py -2`, l'antépénultième `#!py -3`, *etc*.

```python
# indices pos.      0 ------> 1 ------> 2 ---------> 3 -----> 4
classement = ["Nadia", "Franck", "Thomas", "Elizabeth", "Laure"]
# indices nég.     -5 <----- -4 <----- -3 <-------- -2 <---- -1
```
