## Explications détaillées de la correction

L'algorithme de Luhn permet de vérifier l'intégrité d'un numéro de carte bancaire à 16 chiffres en quatre étapes bien distinctes.

Dans le cadre du travail sur les **listes en Python**, on peut représenter les chiffres de la carte sous la forme d'une liste d'entiers :
```python
# Conversion d'une chaîne nettoyée en liste d'entiers
chiffres = [int(c) for c in numero if c != " "]
```

---

### 1. Parité des indices et chiffres à doubler

Dans une liste de 16 chiffres indexée de $0$ à $15$ :
- Les chiffres à doubler (le 1er, le 3e, le 5e...) sont situés aux **indices pairs** : `0, 2, 4, 6, 8, 10, 12, 14`.
- En Python, pour tester si un entier `i` est pair, on utilise l'opérateur modulo : `#!py i % 2 == 0`.

---

### 2. Pourquoi soustraire 9 revient à additionner les chiffres ?

Lorsqu'on double un chiffre $c \in \{0, 1, \dots, 9\}$, le résultat $2c$ est au maximum égal à $18$.

Si $2c > 9$, le résultat est un nombre à deux chiffres dont le premier chiffre (les dizaines) vaut **toujours 1** :
- $10 \implies 1 + 0 = 1$ et $10 - 9 = 1$
- $12 \implies 1 + 2 = 3$ et $12 - 9 = 3$
- $14 \implies 1 + 4 = 5$ et $14 - 9 = 5$
- $16 \implies 1 + 6 = 7$ et $16 - 9 = 7$
- $18 \implies 1 + 8 = 9$ et $18 - 9 = 9$

D'un point de vue mathématique : un nombre à deux chiffres s'écrit $10 + u$ (où $u$ est le chiffre des unités). La somme de ses chiffres est $1 + u$, ce qui vaut exactement $(10 + u) - 9$.

Les deux écritures suivantes sont donc équivalentes :
```python
# Méthode 1 : Soustraction directe de 9
total += double - 9

# Méthode 2 : Décomposition dizaines / unités
total += (double // 10) + (double % 10)
```

---

### 3. Tester si un nombre se termine par 0

Un nombre se termine par 0 si et seulement s'il est un multiple de 10. En Python, cela se traduit simplement par :
```python
total % 10 == 0
```
Cette expression booléenne s'évalue directement à `#!py True` ou `#!py False`.

---

### 4. Code complet de référence (avec liste de chiffres)

```python
def est_valide(numero):
    # Conversion en liste d'entiers
    if isinstance(numero, list):
        chiffres = [int(x) for x in numero]
    else:
        nettoye = str(numero).replace(" ", "")
        if not nettoye.isdigit():
            return False
        chiffres = [int(c) for c in nettoye]

    # Vérification de la longueur
    if len(chiffres) != 16:
        return False

    total = 0
    for i in range(16):
        chiffre = chiffres[i]
        if i % 2 == 0:
            double = chiffre * 2
            if double > 9:
                total += double - 9
            else:
                total += double
        else:
            total += chiffre

    return total % 10 == 0
```

---

### 5. Réponses aux cartes de la page 2 du document

Voici les totaux obtenus pour les 4 cartes proposées :

| Carte | Numéro | Total Luhn | Résultat |
| :--- | :--- | :---: | :---: |
| Adam Bergnaum | `5159 5674 0995 7111` | $60$ ($60 \pmod{10} = 0$) | **Valide** |
| Celia Schaden | `6499 8024 5027 3568` | $74$ ($74 \pmod{10} = 4$) | **Invalide** |
| Lester Connelly | `8504 1721 9127 3888` | $80$ ($80 \pmod{10} = 0$) | **Valide** |
| Carroll Goodwin | `0043 6687 8348 5480` | $72$ ($72 \pmod{10} = 2$) | **Invalide** |
