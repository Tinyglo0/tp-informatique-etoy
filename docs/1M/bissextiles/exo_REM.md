Si l'on applique la règle telle qu'elle est formulée dans l'énoncé on obtient :

```python
def est_bissextile(annee):
    if annee % 4 != 0:      # année non div. par 4
        return False            
    else:                   # année div. par 4
        if annee % 100 != 0:    # année non div. par 100 
            return True
        else:                   # année div. par 100
            if annee % 400 != 0:    # année non div. par 400
                return False
            else:                   # année div. par 400 
                return True
```

Il est aussi possible de structurer le code avec des `elif` :

```python
def est_bissextile(annee):
    if annee % 4 != 0:      # année non div. par 4
        return False            
    elif annee % 100 != 0: # année div. par 4
                           # et pas par 100 
        return True
    elif annee % 400 != 0: # année div. par 4
                           # et par 100
                           # mais pas par 400
        return False
    else: # année div. par 4
          # et par 100
          # mais pas par 400
        return True
```

En utilisant plusieurs `return`, on peut obtenir un code plus lisible :


On peut aussi répondre en une ligne :

```python
def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0
```
