---
name: creer-exercice
description: >-
  Guide complet pour créer un exercice interactif sur la plateforme TP Informatique Etoy.
  Couvre la structure des fichiers, les sections Pyodide, les macros IDE, les admonitions,
  l'intégration d'images, et l'ajout de la page dans la navigation du site.
  Activer ce skill dès qu'il faut créer, modifier ou transformer un exercice.
---

# Créer un exercice interactif — Guide complet

Ce skill décrit **pas à pas** comment créer un exercice interactif pour le site
TP Informatique du Gymnase d'Etoy. Le site est généré avec MkDocs et le thème
`pyodide-mkdocs-theme` (PMT), qui permet aux élèves d'exécuter du Python
directement dans leur navigateur.

---

## 1. Structure des fichiers

### 1.1 Arborescence type

```text
docs/<niveau>/<nom-exercice>/
├── index.md                # Page Markdown de l'exercice
├── scripts/                # (ou pythons/) Dossier des scripts Python
│   ├── exo1.py
│   ├── exo2.py
│   └── exo2_REM.md         # (Optionnel) Remarque affichée après validation réussie
└── images/                 # (Optionnel) Illustrations
    └── schema.png
```

- `<niveau>` = `1M` ou `2M`
- `<nom-exercice>` = nom en minuscules avec tirets (ex : `entrainement-listes`)
- Les scripts Python peuvent être à la racine du dossier ou dans un sous-dossier
  `scripts/` ou `pythons/`.

### 1.2 Convention de nommage

| Fichier | Rôle |
|:--------|:-----|
| `exo.py` | Script unique pour un exercice simple |
| `exo1.py`, `exo2.py`, ... | Scripts numérotés quand l'exercice a plusieurs questions |
| `exo1_1.py`, `exo1_2.py`, ... | Sous-questions (ex : question 1.1, 1.2, ...) |
| `exo_REM.md` | Remarque post-validation (même nom que le `.py`, suffixé `_REM`) |
| `exo_a.py`, `exo_b.py` | Versions alternatives (vide / à trous) pour `IDE_versions` |

---

## 2. Fichier Python : les sections Pyodide

Chaque fichier `.py` est découpé en sections grâce à des commentaires spéciaux.
L'ordre des sections doit être respecté.

### 2.1 Toutes les sections disponibles

```python
# --------- PYODIDE:ignore --------- #
# Code ignoré par Pyodide (imports locaux pour tests hors navigateur)

# --------- PYODIDE:env --------- #
# Code d'initialisation exécuté silencieusement AVANT le code de l'élève.
# Sert à définir des variables, fonctions utilitaires, imports.
# L'élève ne voit PAS ce code.

# --------- PYODIDE:code --------- #
# Code pré-rempli dans l'éditeur de l'élève.
# C'est le point de départ que l'élève doit compléter.

# --------- PYODIDE:corr --------- #
# Solution / correction complète.
# Accessible via le bouton "Correction" après MAX tentatives.
# OBLIGATOIRE si une section `secrets` existe.

# --------- PYODIDE:tests --------- #
# Tests PUBLICS visibles par l'élève (onglet "Tests").
# Exécutés quand l'élève clique sur "Exécuter".

# --------- PYODIDE:secrets --------- #
# Tests CACHÉS, invisibles pour l'élève.
# Exécutés uniquement lors de la validation (bouton "Valider").
# Ne JAMAIS y mettre la logique de la solution (boucles, algorithmes).
# Préférer des valeurs en dur ou des assertions simples.

# --------- PYODIDE:checks --------- #
# Analyse statique du code de l'élève via __USER_CODE__.
# Ex : vérifier qu'une fonction interdite n'est pas utilisée.

# --------- PYODIDE:post --------- #
# Code de nettoyage exécuté après l'exécution et les tests.

# --------- PYODIDE:dessin --------- #
# Logique de dessin pour les exercices alien_python / pixel_art.

# --------- PYODIDE:grille --------- #
# Grille de référence pour les exercices alien_python.
```

### 2.2 Sections les plus courantes

Pour un exercice standard, on utilise généralement :

```python
# --------- PYODIDE:env --------- #
# Variables / fonctions prédéfinies (optionnel)

# --------- PYODIDE:code --------- #
# Code de départ pour l'élève

# --------- PYODIDE:corr --------- #
# Solution complète

# --------- PYODIDE:secrets --------- #
# Tests cachés de validation
```

### 2.3 Règles importantes

1. **`secrets` requiert `corr`** : Si un fichier contient une section `secrets`,
   il DOIT aussi contenir une section `corr` (ou un fichier `_REM.md`).
   Sinon MkDocs lèvera une erreur au build.

2. **Ne pas mettre la solution dans `secrets`** : Les tests cachés ne doivent
   PAS contenir l'algorithme attendu. Si l'élève provoque une erreur, le
   traceback pourrait révéler le contenu. Préférer :
   - Des valeurs en dur (tableaux pré-calculés)
   - Des assertions simples (`assert f(5) == 25`)

3. **`env` est invisible** : Le code dans `env` est exécuté mais jamais montré
   à l'élève. Idéal pour prédéfinir des listes, des données, etc.

### 2.4 Exemple complet

```python
# --------- PYODIDE:env --------- #
notes = [12, 15, 8, 19, 14, 7, 16]

# --------- PYODIDE:code --------- #
# La liste `notes` est déjà définie.
# Calculer la moyenne des notes (sans utiliser sum).
moyenne = ...
print("Moyenne:", moyenne)

# --------- PYODIDE:corr --------- #
total = 0
for n in notes:
    total += n
moyenne = total / len(notes)
print("Moyenne:", moyenne)

# --------- PYODIDE:secrets --------- #
assert abs(moyenne - 13.0) < 0.01, "La moyenne n'est pas correcte"
```

---

## 3. Page Markdown (`index.md`)

### 3.1 Frontmatter obligatoire

```yaml
---
hide: toc, navigation
title: Titre de l'exercice
---
```

### 3.2 Titre de la page

```markdown
# Exercices d'entraînement sur les listes
```

### 3.3 Admonitions pour les exercices

Chaque exercice doit être dans une admonition **pliable** `??? question` :

```markdown
??? question "Exercice 1 : Titre de l'exercice"
    Énoncé de l'exercice...
    
    {{ IDE('scripts/exo1') }}
```

**Attention à l'indentation** : tout le contenu à l'intérieur de l'admonition
doit être indenté de **4 espaces**.

Pour un exercice déplié par défaut mais pliable :
```markdown
???+ question "Exercice 1 : Titre de l'exercice"
```

### 3.4 Sous-questions numérotées

Quand un exercice a plusieurs sous-questions, utiliser des listes ordonnées
Markdown (`1.`, `2.`, ...) avec un IDE après chaque question :

```markdown
??? question "Exercice 1 : Les pays de l'UE"
    Énoncé général de l'exercice...
    
    1. Première question ?
    {{ IDE('scripts/ex1_1') }}

    2. Deuxième question ?
    {{ IDE('scripts/ex1_2') }}

    3. Troisième question ?
    {{ IDE('scripts/ex1_3') }}
```

### 3.5 Blocs de code dans l'énoncé

Pour montrer des données (listes, exemples) dans l'énoncé sans qu'elles soient
exécutables :

```markdown
    ```python
    ma_liste = [1, 2, 3, 4, 5]
    ```
```

---

## 4. Macros IDE disponibles

### 4.1 `{{ IDE(...) }}` — Macro principale

```markdown
{{ IDE('scripts/exo1') }}
```

Le chemin est relatif au dossier de la page `index.md`, **sans l'extension `.py`**.

**Paramètres courants :**

| Paramètre | Type | Description |
|:-----------|:-----|:------------|
| `MAX` | int | Nombre max de tentatives avant de révéler la correction. `1000` = quasi-infini. Par défaut : `5`. |
| `SANS` | str | Fonctions/modules interdits, séparés par des virgules. Ex : `SANS="sum, max, min"`. Pour interdire une syntaxe AST : `SANS="AST: for"`. |
| `STD_KEY` | str | Clé de chiffrement pour les sections `corr`/`secrets`. |
| `ID` | str | Identifiant unique si plusieurs IDE partagent le même nom sur une page. |
| `TERM_H` | int | Hauteur du terminal (en lignes). Par défaut : `10`. |
| `MIN_SIZE` | int | Hauteur minimum de l'éditeur (en lignes). Par défaut : `3`. |
| `MAX_SIZE` | int | Hauteur maximum de l'éditeur (en lignes). Par défaut : `30`. |

**Exemples :**

```markdown
{{ IDE('exo', MAX=1000) }}
{{ IDE('scripts/exo2', SANS="sorted, max, sum, min") }}
{{ IDE('exo4', STD_KEY="1234", MAX=1000) }}
```

### 4.2 `{{ IDE_versions(...) }}` — Versions multiples

Crée des onglets avec plusieurs versions d'un même exercice (version vide /
version à trous) :

```markdown
{{ IDE_versions('exo_a', 'exo_b', preferred=2, MAX=1000) }}
```

- `preferred` : numéro (1-indexé) de la version recommandée.
- Alias : `{{ double_IDE(...) }}` et `{{ IDE_double(...) }}`.

### 4.3 `{{ alien_IDE(...) }}` — Exercices Alien Python

```markdown
{{ alien_IDE(5, MAX=1000) }}
```

- `num` : numéro de l'exercice (pointe vers `scripts/exo{num}.py`).
- `grille` : `True`/`False` pour afficher ou non la grille attendue.

### 4.4 `{{ alien_dessin(...) }}` — Dessin Alien (lecture seule)

```markdown
{{ alien_dessin(1) }}
```

Affiche un dessin alien sans éditeur interactif.

---

## 5. Intégration d'images

### 5.1 Images statiques

Placer les images dans un dossier `images/` (ou à la racine du dossier exercice)
et les référencer en Markdown :

```markdown
![Description](images/schema.png){: width=75% .center }
```

Pour centrer une image avec `attr_list` :

```markdown
![Description](image.png){: style="display: block; margin: 0 auto" }
```

La classe CSS `.center` est aussi disponible dans le projet :

```markdown
![Description](images/schema.png){ .center }
```

### 5.2 Images issues d'un notebook Jupyter

Pour extraire les images embarquées dans un notebook `.ipynb` :

```python
import json, base64, os

with open("notebook.ipynb", 'r', encoding='utf-8') as f:
    notebook = json.load(f)

for cell in notebook['cells']:
    if 'attachments' in cell:
        for filename, attachment in cell['attachments'].items():
            if 'image/png' in attachment:
                data = base64.b64decode(attachment['image/png'])
                with open(os.path.join("output_dir", filename), 'wb') as img_f:
                    img_f.write(data)
```

### 5.3 Images côte à côte

```html
<div style="display: flex; justify-content: space-around; margin: auto;">
    ![Image 1](images/img1.svg){width=100%}
    ![Image 2](images/img2.gif){width=65%}
</div>
```

---

## 6. Ajouter la page dans la navigation

### 6.1 Lien dans la page de catégorie

Ajouter un lien dans la page thématique correspondante (ex : `docs/2M/listes-python.md`) :

```markdown
- [ ] [Titre de l'exercice](nom-exercice/index.md)
```

### 6.2 Carte dans la page d'accueil du niveau (optionnel)

Si l'exercice mérite d'apparaître directement sur la page d'accueil du niveau
(`docs/2M/index.md`), ajouter une carte dans le `<div class="grid cards">` :

```markdown
-   :material-icon: **Titre**

    ---

    Description courte.

    [:octicons-arrow-right-24: Commencer](nom-exercice/index.md)
```

### 6.3 Structure de navigation

La navigation globale est gérée par `mkdocs.yml` avec seulement les onglets
principaux. La navigation interne est gérée automatiquement par le plugin
`awesome-pages` et les liens manuels dans les pages hub.

---

## 7. Checklist de création d'un exercice

Voici la checklist complète à suivre pour créer un exercice :

- [ ] **Créer le dossier** : `docs/<niveau>/<nom-exercice>/`
- [ ] **Créer le sous-dossier scripts** : `scripts/` (ou `pythons/`)
- [ ] **Créer les fichiers Python** pour chaque question :
    - Section `env` si des données doivent être prédéfinies
    - Section `code` avec le squelette pour l'élève
    - Section `corr` avec la solution complète
    - Section `secrets` avec les tests cachés (valeurs en dur, pas d'algorithme)
- [ ] **Créer `index.md`** :
    - Frontmatter : `hide: toc, navigation` + `title:`
    - Titre `#`
    - Admonitions pliables `??? question "Exercice N : Titre"`
    - Questions numérotées `1.`, `2.`, ... si plusieurs sous-questions
    - Appels `{{ IDE('scripts/exoN') }}` correctement indentés (4 espaces)
- [ ] **Ajouter les images** si nécessaire (dossier `images/` ou racine)
- [ ] **Ajouter le lien** dans la page de catégorie (ex : `listes-python.md`)
- [ ] **Tester** avec `mkdocs serve` :
    - La page compile sans erreur
    - Les IDE s'affichent correctement
    - Les corrections s'affichent (bouton ampoule)
    - Les tests de validation fonctionnent
    - Les images sont visibles et centrées

---

## 8. Erreurs fréquentes à éviter

| Erreur | Cause | Solution |
|:-------|:------|:---------|
| `secrets without corr section` | Section `secrets` sans section `corr` | Ajouter une section `corr` (même minimale avec `pass`) |
| IDE non affiché | Mauvaise indentation dans l'admonition | Vérifier que `{{ IDE(...) }}` est indenté de 4 espaces |
| Solution visible dans les tests | Algorithme dans `secrets` | Remplacer par des valeurs en dur ou des assertions simples |
| Image non trouvée | Chemin relatif incorrect | Le chemin est relatif à `index.md` |
| Extension `.py` dans le chemin IDE | `{{ IDE('scripts/exo.py') }}` | Retirer l'extension : `{{ IDE('scripts/exo') }}` |

---

## 9. Transformer un notebook Jupyter en exercices

Pour convertir un fichier `.ipynb` en exercices interactifs :

1. **Lire le notebook** et identifier les cellules Markdown (énoncés) et Code
   (squelettes + assertions).
2. **Extraire les images** embarquées (voir section 5.2).
3. **Pour chaque exercice** :
    - Créer un fichier `.py` avec les sections Pyodide appropriées.
    - Le code de la cellule d'initialisation → section `env`.
    - Le squelette vide → section `code`.
    - La solution → section `corr`.
    - Les `assert` → section `secrets` (reformulés avec des valeurs en dur).
4. **Créer la page `index.md`** avec les admonitions et les appels IDE.
5. **Intégrer** dans la navigation du site.
