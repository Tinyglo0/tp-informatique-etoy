Une des difficultés de cet exercice est le décalage de 1 entre le place d'un coureur et son indice dans la liste.

Autre solution possible : 

```python
def depasse(classement, place):
    classement[place - 1], classement[place - 2] = classement[place - 2], classement[place - 1]
```
