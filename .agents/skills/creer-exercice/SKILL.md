---
name: creer-exercice
description: >-
  Guide complet pour créer un exercice interactif en Python avec sa correction associée
  sur la plateforme TP Informatique Etoy (basée sur CodEx et pyodide-mkdocs-theme).
  Couvre la structure des fichiers, les sections Pyodide (env, code, corr, tests, secrets, post),
  les fichiers de correction détaillée (_REM.md), les macros IDE (avec MAX=1000 obligatoire),
  les versions vides/à trous, les admonitions et l'ajout dans la navigation.
  Activer ce skill dès qu'il faut créer, modifier ou transformer un exercice Python.
---

# Créer un exercice Python interactif avec correction — Guide complet

Ce skill décrit **pas à pas** comment créer un exercice interactif en Python avec sa correction associée pour le site TP Informatique du Gymnase d'Etoy, basé sur [CodEx](https://forge.apps.education.fr/codex/codex.forge.apps.education.fr) et le thème [`pyodide-mkdocs-theme` (PMT)](https://frederic-zinelli.gitlab.io/pyodide-mkdocs-theme/#creer-des-ides).

> **Règle d'or pour les IDE** : Tous les appels `IDE(...)`, `IDE_versions(...)` et `alien_IDE(...)` pour un exercice doivent **systématiquement** inclure `MAX=1000` (nombre d'essais quasi-infini).

---

## 1. Structure des fichiers

### 1.1 Arborescence type

Deux organisations sont utilisées dans `docs/<niveau>/<nom-exercice>/` (`<niveau>` = `1M` ou `2M`) :

**Option A — Fichiers à la racine de l'exercice (style CodEx classique, 1 à 4 scripts) :**
```text
docs/<niveau>/<nom-exercice>/
├── index.md                # Énoncé Markdown de l'exercice
├── exo.py                  # Script Python (code élève + correction + tests)
├── exo_REM.md              # (Optionnel) Explications et solutions alternatives post-validation
├── exo_trous.py            # (Optionnel) Version à trous si exercice bi-version
└── images/                 # (Optionnel) Illustrations
    └── schema.png
```

**Option B — Sous-dossier `scripts/` ou `pythons/` (recommandé si nombreux scripts) :**
```text
docs/<niveau>/<nom-exercice>/
├── index.md                # Page Markdown de l'exercice
├── pythons/                # (ou scripts/) Dossier des scripts Python
│   ├── exo1.py
│   ├── exo1_REM.md         # (Optionnel) Remarque de correction associée à exo1.py
│   ├── exo2.py
│   └── exo2_REM.md
└── images/                 # (Optionnel) Illustrations
```

### 1.2 Convention de nommage des fichiers

| Fichier | Rôle |
|:--------|:-----|
| `exo.py` | Script unique pour un exercice simple |
| `exo1.py`, `exo2.py`, ... | Scripts numérotés pour un exercice à plusieurs étapes/questions |
| `exo1_q1.py`, `ex1_1.py` | Sous-questions d'un même exercice |
| `exo_vide.py`, `exo_trous.py` (ou `exo_a.py`, `exo_b.py`) | Versions « vide » et « à trous » pour `IDE_versions` |
| `<nom>_REM.md` | Correction commentée / remarques pédagogiques (même dossier et même préfixe que `<nom>.py`) |
| `<nom>_VIS_REM.md` | Remarques visibles sous la correction |

> **Note `mkdocs.yml`** : Les motifs `**/*.py` et `**/*_REM.md` sont déclarés dans `exclude_docs` afin d'être chargés par Pyodide sans générer de pages HTML parasites.

---

## 2. Fichier Python (`.py`) : Sections Pyodide et Correction

Chaque fichier `.py` regroupe l'environnement, le code de départ, la **correction** et les **tests de validation** grâce aux séparateurs `# --------- PYODIDE:<section> --------- #` (ou `# --- PYODIDE:<section> --- #`).

### 2.1 Cycle d'exécution dans `pyodide-mkdocs-theme`

| Action de l'élève | Sections exécutées (dans l'ordre) |
|:------------------|:----------------------------------|
| **Exécuter** (bouton Play ▶) | `env` ➔ `code` (élève) ➔ `tests` (publics) ➔ `post` |
| **Valider** (bouton Check ✔️) | `env` ➔ `code` (élève) ➔ `tests` (publics) ➔ `secrets` (cachés) ➔ `post` |

Lorsque la validation réussit, le thème révèle automatiquement la **correction** contenue dans la section `corr` ainsi que le contenu éventuel du fichier `<nom>_REM.md`.

### 2.2 Structure complète d'un fichier `exo.py`

```python
# --------- PYODIDE:ignore --------- #
# (Optionnel) Code ignoré par PMT, utile pour tester le fichier en local

# --------- PYODIDE:env --------- #
# (Optionnel) Exécuté silencieusement AVANT le code de l'élève.
# Invisible pour l'élève. Sert à définir des variables, constantes,
# fonctions utilitaires, imports cachés ou drapeaux de vérification.

# --------- PYODIDE:code --------- #
# Code pré-rempli dans l'éditeur de l'élève.
# Utiliser `...` ou `pass` pour les zones à compléter.
def ma_fonction(param):
    ...

# --------- PYODIDE:corr --------- #
# OBLIGATOIRE dès qu'il y a une section `secrets` ou un fichier `_REM.md`.
# Contient la solution de référence propre et lisible.
def ma_fonction(param):
    return param * 2

# --------- PYODIDE:tests --------- #
# Tests PUBLICS visibles par l'élève et exécutés avec le bouton "Exécuter".
# Doivent correspondre exactement aux exemples donnés dans l'énoncé Markdown.
assert ma_fonction(3) == 6
assert ma_fonction(0) == 0

# --------- PYODIDE:secrets --------- #
# Tests CACHÉS exécutés uniquement lors du clic sur "Valider".
# Tester les cas limites (0, négatifs, listes vides, doublons...) et des cas aléatoires.
assert ma_fonction(-5) == -10
for x in range(10, 50):
    attendu = x * 2
    assert ma_fonction(x) == attendu, f"Erreur avec {x = }"

# --------- PYODIDE:post --------- #
# (Optionnel) Exécuté à la toute fin (dans un bloc finally) pour nettoyer
# l'environnement (ex: restaurer `input` ou `randint`, fermer une figure).
```

### 2.3 Bonnes pratiques pour la correction (`corr`, `_REM.md`, `tests`, `secrets`)

1. **`corr` est obligatoire avec `secrets`** : Si un fichier contient `PYODIDE:secrets`, il **doit** contenir `PYODIDE:corr` (ou un fichier `_REM.md`), sinon `mkdocs` échoue à la compilation.
2. **Clarté de `PYODIDE:corr`** : Mettre dans `corr` la solution la plus pédagogique et lisible pour le niveau visé (`1M` ou `2M`). Les variantes plus compactes (compréhension de liste, opérateur ternaire, indices négatifs, etc.) vont dans `exo_REM.md`.
3. **Fichier `exo_REM.md` (Correction commentée)** :
   - Placé à côté de `exo.py` (ex: `docs/1M/bissextiles/exo_REM.md`).
   - Rédigé en Markdown standard (blocs de code ` ```python `, admonitions `!!! abstract`, tableaux, formules LaTeX).
   - Explique la démarche, les erreurs classiques (ex: décalage d'indice `rang - 1`) et présente d'autres implémentations valides (`elif`, une seule ligne, etc.).
4. **Messages d'erreur dans `secrets`** :
   - Toujours ajouter un message d'erreur clair dans les assertions secrètes pour aider l'élève à débugger sans dévoiler la formule :
     ```python
     assert est_bissextile(annee) is attendu, f"Erreur avec {annee = }"
     ```
   - Si l'exercice interdit une fonction via `SANS="sum, max"`, **ne pas utiliser non plus** cette fonction dans `env`, `tests` ou `secrets` (la restriction AST/runtime s'applique aussi pendant les tests !). Calculer le résultat attendu avec une boucle basique ou des valeurs en dur.
5. **Vérifier qu'une fonction précédente est bien réutilisée** (ex: exercices multi-questions type `gestion-rpg` ou `trajet-voiture`) :
   - Dans `PYODIDE:env`, définir les fonctions des questions précédentes en levant un drapeau (`flag`) lorsqu'elles sont appelées :
     ```python
     # --------- PYODIDE:env --------- #
     flag_distance = False

     def calculer_distance(v, t):
         global flag_distance
         flag_distance = True
         return v * t
     ```
   - Dans `PYODIDE:secrets`, vérifier le drapeau et afficher un avertissement avec `terminal_message` (associé à `STD_KEY="1234"` dans la macro `IDE`) :
     ```python
     # --------- PYODIDE:secrets --------- #
     if not flag_distance:
         terminal_message("1234", "Utilisez la fonction calculer_distance !", "warning")
     assert cout_trajet(110, 2, 6, 1.85) == 24.42
     ```

### 2.4 Version vide vs Version à trous (`exo_vide.py` / `exo_trous.py`)

Inspiré de CodEx, on peut proposer deux niveaux d'accompagnement :
- **Version vide (`exo.py` ou `exo_vide.py`)** : seule la signature de la fonction est donnée :
  ```python
  def deux_meilleurs(scores):
      ...
  ```
- **Version à trous (`exo_trous.py`)** : la structure algorithmique est guidée avec des `...` :
  ```python
  def deux_meilleurs(scores):
      max1 = None
      max2 = ...
      for v in scores:
          if max1 is None or v > max1:
              max2 = ...
              max1 = ...
      return ..., ...
  ```

---

## 3. Page Markdown (`index.md`)

### 3.1 Frontmatter obligatoire

```yaml
---
hide:
    - navigation
    - toc
title: Titre de l'exercice
---
```
*(Des métadonnées CodEx optionnelles comme `author`, `tags`, `difficulty` peuvent aussi être présentes).*

### 3.2 Deux modèles de mise en page

#### Modèle 1 : Exercice unique type CodEx (ex: `bissextiles`, `deux-meilleurs`, `costumes`)

L'énoncé est écrit directement dans la page, suivi des aides éventuelles, d'un bloc d'exemples déplié `???+ example "Exemples"` au format console Python (`pycon`), puis de l'IDE :

```markdown
---
hide:
    - navigation
    - toc
title: Années bissextiles
---

Énoncé de l'exercice...

!!! warning "Contraintes"

    On n'utilisera ni `max`, ni `min`, ni `sorted`.

??? tip "Aide"

    Indice ou rappel de cours replié par défaut...

???+ example "Exemples"

    ```pycon title=""
    >>> ma_fonction(2020)
    True
    >>> ma_fonction(2022)
    False
    ```

{{ IDE('exo', MAX=1000) }}
```

#### Modèle 2 : Exercice progressif à plusieurs questions / fiche d'entraînement (ex: `gestion-rpg`, `course_cycliste`, `entrainement-listes`)

Un contexte général en haut de page, puis chaque question dans une admonition pliable `??? question "..."` (tout le contenu interne doit être **indenté de 4 espaces**) :

```markdown
---
hide:
    - navigation
    - toc
title: Combat RPG
---

Contexte général de l'exercice...

??? question "1. Force de frappe"

    Énoncé de la question 1...

    ```pycon
    >>> calculer_puissance(80, 20)
    100
    ```

    {{ IDE('exo1', MAX=1000) }}

??? question "2. Réduction des dégâts"

    Énoncé de la question 2...

    {{ IDE('exo2', MAX=1000) }}
```

### 3.3 Admonitions et encadrés : Syntaxe Material for MkDocs obligatoire

> ⚠️ **IMPORTANT : Ne JAMAIS utiliser la syntaxe GitHub Alerts (`> [!TIP]`, `> [!NOTE]`, `> [!WARNING]`, `> [!IMPORTANT]`, etc.)**.
> Cette syntaxe n'est pas reconnue par le moteur de rendu MkDocs Material et s'affiche sous forme de simple citation brute cassée.

Toujours utiliser la syntaxe standard des **admonitions MkDocs** :
- `!!! <type> "Titre"` : encadré **ouvert en permanence** (ex: `!!! warning "Contraintes"`).
- `??? <type> "Titre"` : encadré **replié par défaut**, dépliable au clic (ex: `??? info "Astuce"`, `??? tip "Indice"`, `??? question "Question 1"`).
- `???+ <type> "Titre"` : encadré **déplié par défaut**, repliable au clic (ex: `???+ example "Exemples"`).

**Types fréquents** :
- `info` : astuces de calcul, compléments d'information.
- `tip` : indices ou aides méthodologiques.
- `warning` : contraintes strictes, interdictions ou pièges à éviter.
- `example` : exemples de code, doctests `pycon`.
- `question` : questions progressives numérotées.

**Règle stricte d'indentation** :
Tout le contenu à l'intérieur d'une admonition (paragraphes, code `pycon`, listes, blocs mathématiques ou IDE) **doit obligatoirement être indenté de 4 espaces** :

```markdown
??? info "Astuce pour l'étape 2"

    Lorsqu'on double un chiffre entre 0 et 9, le résultat vaut au maximum 18.
    Additionner ses chiffres revient à lui **soustraire 9**.

    *Exemple :* $16 \implies 1 + 6 = 7$ et $16 - 9 = 7$.
```

### 3.4 Diagrammes, formules et coloration inline

- **Code Python inline coloré** : utiliser `#!py True`, `#!py None`, `#!py x % 2 == 0`.
- **Formules mathématiques LaTeX** : `$d = v \times t$` (inline) ou `$$ \text{Puissance} = \text{Force} + \text{Bonus} $$` (bloc).
- **Organigrammes Mermaid** : utiliser un bloc ```` ```mermaid ```` (`flowchart LR` ou `graph LR`) pour illustrer un algorithme conditionnel ou une boucle.
  - *Bonnes pratiques Mermaid pour éviter les erreurs de parsing* :
    - Éviter d'imbriquer des parenthèses dans un nœud stadium : préférer `Start("Début")` à `Start(["Début (texte)"])`.
    - Pour les losanges de décision `{...}`, éviter les symboles bruts `>` ou `%` non protégés.
    - Utiliser des nœuds de convergence circulaires `Next(("Passer au suivant"))` pour reboucler proprement.


---

## 4. Macros disponibles dans le projet

### 4.1 `{{ IDE(...) }}` — Macro principale

> **Toujours préciser `MAX=1000`** pour laisser un nombre d'essais infini aux élèves.

```markdown
{{ IDE('exo', MAX=1000) }}
{{ IDE('scripts/exo2', MAX=1000, SANS="sorted, max, sum, min") }}
{{ IDE('exo4', STD_KEY="1234", MAX=1000) }}
```

- **1er argument** : chemin relatif vers le script Python depuis le dossier contenant `index.md`, **sans l'extension `.py`**.
- **Paramètres utiles** :
  - `MAX=1000` : **(Obligatoire)** Nombre d'essais quasi-infini avant de pouvoir révéler la solution sans réussir.
  - `SANS="..."` : Fonctions, méthodes (`.sort`), modules ou constructions AST (`AST: for`) interdits, séparés par des virgules.
  - `STD_KEY="..."` : Clé autorisant l'utilisation de `terminal_message(STD_KEY, ...)` dans les sections cachées.
  - `MODE="no_reveal"` / `"no_valid"` / `"delayed_reveal"` / `"revealed"` : Contrôle le mode de validation/révélation (par défaut : validation standard avec tests et révélation à la réussite).
  - `TERM_H=10` : Hauteur du terminal en nombre de lignes.
  - `MIN_SIZE=3`, `MAX_SIZE=30` : Bornes de hauteur de l'éditeur en lignes.
  - `TEST="..."` : Contrôle l'exécution lors des tests globaux du site (`include: site`).

### 4.2 `{{ IDE_versions(...) }}` (ou `double_IDE` / `IDE_double`) — Onglets multi-versions

Permet de proposer côte à côte une version vide et une version à trous :

```markdown
{{ IDE_versions('exo_vide', 'exo_trous', preferred=2, MAX=1000) }}
```
- Par défaut, l'onglet 1 s'intitule `"Version vide"` et l'onglet 2 `"Version à trous"`.
- `preferred=1` ou `preferred=2` ajoute une icône cible sur la version recommandée.
- On peut personnaliser les titres avec `title1="..."`, `title2="..."`.

### 4.3 Macros CodEx de remarques et d'interdictions

- `{{ interdiction("sum, max, min") }}` : Génère automatiquement une admonition `???+ warning` listant proprement les fonctions interdites.
- `{{ remarque('assertion') }}` : Insère le fichier `remarques/assertion.md` expliquant le fonctionnement du mot-clé `assert`.

### 4.4 Macros graphiques (`figure`, `alien_IDE`, `alien_dessin`, `run`)

- **P5 / Matplotlib / Pixel Art** :
  - `{{ run('scripts/dessin1') }}` exécute un script automatiquement au chargement.
  - `{{ figure("id_cible", admo_title="Titre") }}` crée la zone d'affichage graphique associée.
- **Alien Python** :
  - `{{ alien_dessin(1) }}` : question où l'élève clique sur les cases de la grille (section `PYODIDE:dessin`).
  - `{{ alien_IDE(5, MAX=1000) }}` : question où l'élève code le déplacement de l'alien.

---

## 5. Intégration d'images

Placer les images dans `images/` (ou dans le dossier de l'exercice) et utiliser `attr_list` avec la classe `.center` :

```markdown
![Texte alternatif](images/schema.png){ width=50% .center }
```

Pour mettre deux images côte à côte :
```markdown
<div style="display: flex; justify-content: space-around; margin: auto;">
    ![Image 1](images/img1.svg){width=100%}
    ![Image 2](images/img2.gif){width=65%}
</div>
```

---

## 6. Ajouter l'exercice dans la navigation

1. **Page thématique du niveau** (ex: `docs/1M/conditions.md`, `docs/1M/fonctions.md`, `docs/1M/boucle-while.md`, `docs/1M/variables.md`, `docs/2M/listes-python.md`) :
   Ajouter une entrée dans la liste de tâches :
   ```markdown
   - [ ] [Titre de l'exercice](nom-exercice/index.md)
   ```
2. **Page d'accueil du niveau** (`docs/1M/index.md` ou `docs/2M/index.md`) : uniquement s'il s'agit d'une nouvelle catégorie ou d'un grand TP autonome, ajouter une carte dans `<div class="grid cards" markdown>`.

---

## 7. Checklist de création et de vérification

- [ ] **Dossier créé** : `docs/<niveau>/<nom-exercice>/`
- [ ] **Scripts `.py` complets** :
  - `# --------- PYODIDE:env --------- #` (si données ou fonctions prédéfinies)
  - `# --------- PYODIDE:code --------- #` (squelette élève avec `...`)
  - `# --------- PYODIDE:corr --------- #` (solution complète et propre)
  - `# --------- PYODIDE:tests --------- #` (assertions publiques correspondant aux exemples de l'énoncé)
  - `# --------- PYODIDE:secrets --------- #` (assertions cachées avec cas limites, tests aléatoires et messages d'erreur `f"Erreur avec ..."` ; **aucun appel aux fonctions interdites par `SANS`**)
- [ ] **Correction détaillée (optionnel mais recommandé)** : fichier `<nom>_REM.md` pour expliquer les subtilités ou montrer les solutions alternatives.
- [ ] **Page `index.md` créée** :
  - Frontmatter avec `hide: [navigation, toc]` et `title:`
  - Énoncé clair + exemples dans `???+ example "Exemples"` avec bloc `pycon`
  - **Syntaxe d'admonition MkDocs respectée** : `??? info`, `!!! warning`, `??? tip`... et **jamais** de syntaxe GitHub Alerts (`> [!TIP]`)
  - Tous les appels `{{ IDE(..., MAX=1000) }}` contiennent bien **`MAX=1000`** et sont **sans extension `.py`**
  - Indentation de **4 espaces** respectée à l'intérieur de toutes les admonitions (`??? question`, `??? info`, etc.)
- [ ] **Lien ajouté** dans la page thématique (`docs/1M/...` ou `docs/2M/...`)
- [ ] **Vérification locale** (`mkdocs build` ou `mkdocs serve`) : aucune erreur de build, les tests publics et secrets passent avec le code de `corr`.

---

## 8. Dépannage & compatibilité technique

### Conflit Ace Editor / Mermaid.js (`Wae.default.extend is not a function`)
- **Problème** : Ace Editor (l'éditeur de code des IDE Pyodide) a impérativement besoin de `window.define` pour charger dynamiquement le module de coloration syntaxique Python (`mode-python.js`). À l'inverse, le bundle UMD de Mermaid 11 contient un sous-module (`fastdom`) qui crashe si `window.define` existe au moment de son exécution (`Uncaught TypeError: Wae.default.extend is not a function`). De plus, le rendu natif de `mkdocs-material` (dans un Shadow DOM) vérifie de manière synchrone `typeof mermaid !== "undefined"` au démarrage de `bundle.js`.
- **Solution propre adoptée (le « sandwich synchrone »)** :
  - Dans `overrides/hooks/libsAfter.html` (et en secours dans `overrides/partials/header.html`), juste après le chargement d'Ace Editor dans `<head>` :
    1. On sauvegarde et masque temporairement `window.define` (`window._ace_define = window.define; window.define = undefined;`).
    2. On charge de manière **synchrone** `https://cdn.jsdelivr.net/npm/mermaid@11.16.1/dist/mermaid.min.js` (qui crée `window.mermaid` sans erreur).
    3. On restaure **immédiatement** `window.define = window._ace_define;` dans la balise `<script>` suivante.
  - Ainsi, quand `mkdocs-material` initialise la page, `window.mermaid` est déjà prêt pour le rendu natif des diagrammes, et quand les IDE Pyodide s'initialisent dans le `<body>`, `window.define` est de nouveau présent pour charger la coloration syntaxique Python (`mode-python.js`).


