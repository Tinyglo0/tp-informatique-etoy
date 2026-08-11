La première chose à noter dans cet exercice est la différence entre le rang d’un figurant et l’indice d’un élément dans une liste : le premier commence à 1, le second à 0.

Ainsi, avec la liste de couleurs `["bleu", "blanc", "rouge"]`, s’il n’y avait que 3 figurants avec les rangs 1, 2 et 3 les indices correspondants seraient 0, 1 et 2 soit la valeur du rang moins 1. On pourrait donc penser que la réponse à la question est simplement :

```python 
def costume(rang, couleurs):
    return couleurs[rang - 1]
```

😢 Mais bien sûr cela ne fonctionne pas dès que le nombre de figurants est plus grand que le nombre de couleurs. Ainsi, si on reprend nos trois couleurs ['bleu', 'blanc', 'rouge'] mais que le rang du figurant est 8, alors l’indice serait 7 mais couleurs[7] provoquera une erreur `Index out of range`. On sent bien qu’il faut recommencer au début lorsqu’on dépasse le rang 3 (l’indice 2) pour cet exemple à 3 couleurs. Il y a deux façons de voir cela :


!!! abstract "I. Une première approche"

    🤔 On fait comme si la liste des couleurs étaient suffisamment longue, avec les couleurs qui se répètent : 

    <table>
          <tr>
            <th>Longue liste :</th>
            <th>["bleu",</th>
            <th>"blanc",</th>
            <th>"rouge",</th>
            <th>"bleu",</th>
            <th>"blanc",</th>
            <th>"rouge",</th>
            <th>"bleu",</th>
            <th>"blanc",</th>
            <th>"rouge"]</th>
          </tr>
          <tr>
            <td>Indices</td>
            <td ALIGN="CENTER">0</td>
            <td ALIGN="CENTER">1</td>
            <td ALIGN="CENTER">2</td>
            <td ALIGN="CENTER">3</td>
            <td ALIGN="CENTER">4</td>
            <td ALIGN="CENTER">5</td>
            <td ALIGN="CENTER">6</td>
            <td ALIGN="CENTER">7</td>
            <td ALIGN="CENTER">8</td>
          </tr>
    </table>

    Ainsi pour notre exemple de 3 couleurs et le rang 8 (indice 7), on constate qu’il faudrait 3 fois la liste des couleurs mise bout à bout pour former une liste suffisamment longue pour avoir un élément à l’indice 7.

    😢 **Cette méthode est inefficace** : on est amené à créer une liste potentiellement très grande (imaginez si vous avez plusieurs milliers de figurants)


!!! abstract "II. Méthode plus efficace"

    Dans l'exemple précédent, il suffit de trouver que  l'indice 7 correspond à la même couleur que l'indice 1. Pour comprendre ce qui se passe, nous allons construire le tableau suivant : 

    |Liste normale de couleurs :| [`'bleu'`,| `'blanc'`,| `'rouge'`]|
    |--:|:--:|:--:|:--:|
    |Les indices :|     0  |     1  |      2 |       
    |2e tour :|     3    |   4    |    5   |     
    |3e tour :|     6  |     7    |    8|

    Cela revient à boucler sur les indices 0, 1, 2 autant de fois que nécessaire, c’est-à-dire jusqu’à atteindre la valeur de notre indice (ici 7). Ce qui donne ce code dans un premier temps :

    ```python
    def costume(rang, couleurs):
        indice = rang - 1
        indice_couleur = 0
        for _ in range(indice):
            indice_couleur += 1
            if indice_couleur >= len(couleurs):
                indice_couleur = 0
        return couleurs[indice_couleur]
    ```

!!! abstract "III. 💡 Une approche beaucoup plus efficace, en utilisant **modulo**"

    Mais en réalité, on n’a pas besoin de réaliser explicitement cette boucle pour trouver le bon indice. On remarque, toujours avec l’exemple des 3 couleurs que tous les indices 0, 3, 6, 9, etc. seront associés à l’indice 0, tous les indices 1, 4, 7, 10 ce sera 1 et enfin tous les indices 2, 5, 8 etc. seront associés à 2. C’est l’opération modulo (% en Python) qui permet d’obtenir le résultat et donne le code proposé dans la solution.

    On peut encore optimiser la solution, car si on utilise le "modulo" on évite la boucle. C'est la solution qui est proposée.  

    $7=2 \times 3 + 1$. La réponse sera donc l'élément d'indice 1 : `"blanc"`.  
    Le reste de la division euclidienne de 7 par 3 est 1. Il s'écrit $7 \% 3$. On dit que "7 modulo 3" renvoie $1$.


!!! abstract "Bilan"

    👉 D'une manière générale, lorsqu'on est amené à lire une liste de façon circulaire, c'est-à-dire en reprenant la lecture au début de la liste après l'avoir terminée, il faut penser à utiliser un "modulo longueur de la liste".



