Il est possible de faire une façon plus proche d'une recherche de maximum classique, sans tester `None` :

```python
def deux_meilleurs(scores):
    if len(scores) == 0:
        return None, None
    elif len(scores) == 1:
        return scores[0], None
    if scores[0] > scores[1]:
        max1, max2 = scores[0], scores[1]
    else:
        max1, max2 = scores[1], scores[0]
    for i in range(2, len(scores)):
        if scores[i] > max1:
            max2 = max1
            max1 = scores[i]
        elif scores[i] > max2:
            max2 = scores[i]
    return max1, max2
```
