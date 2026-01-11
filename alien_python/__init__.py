"""
Module permettant d'écrire des programmes déplaçant un alien dans une grille.
Adaptation du travail de Mathieu Degrange (https://github.com/DegrangeM/alien-python)

Auteur : Germain BECKER
Licence : CC BY-NC-SA

//!\\ ATTENTION
Ce module ne fonctionne qu'avec Basthon et donc aussi sur Capytale.
En effet, il est basé sur le module p5 porté dans Basthon par Romain Casati, module
lui-même basé sur la bibliothèque JavaScript self.p5.js (qui diffère du module p5 que l'on
peut obtenir avec la commande pip install p5).
"""
from pyodide.ffi import create_proxy
from calendar import c
import re, js, p5, sys
from inspect import currentframe

# Variables partagées
TAILLE_CASE = 30
MARGE_HAUT = 5
MARGE_BAS = 70
LETTRES = "ABCDEFGHIJKLMNO"
NOMBRES = range(1, 16)



def move_factory(name, dx, dy):

    def move(self:'App', n=1):
        """
        Déplace l'alien de n cases vers le haut.
        Si n est négatif, le déplacement se fait de -n cases vers le bas.
        """
        if not isinstance(n, int):
            raise TypeError(f"Le paramètre de la fonction {name} doit être un nombre entier.")
        if n!=1:
            self.puce = False
        # numéro de ligne appelant la fonction
        ligne = currentframe().f_back.f_lineno
        # mise à jour de la position actuelle
        self.alien['pos'] = {
            'x': self.alien['pos']['x'] + dx * n,
            'y': self.alien['pos']['y'] + dy * n,
            'ligne': ligne,
            'etape': self.alien['pos']['etape'] + 1
        }
        # ajout de cette nouvelle position à la liste de toutes les positions
        self.alien['positions'].append(self.alien['pos'])

    move.__name__ = name
    return move








class App(p5.Sketch):
    def __init__(self, cible):
        self.cible = cible

        # on récupère le numéro de ligne appelant cette fonction
        ligne = currentframe().f_back.f_lineno
        self.alien = {
            'taille_case': TAILLE_CASE,
            'largeur': TAILLE_CASE * 15,
            'hauteur': TAILLE_CASE * 15 + MARGE_HAUT,
            'pos': {'x': 0, 'y': 0, 'ligne': ligne, 'etape': 0},
            'positions': [{'x': 0, 'y': 0, 'ligne': ligne, 'etape': 0}],
            'num_lignes': True,
            'etapes': False,
            'comparaison': False,
            'bonnes_positions': [],
            'coord_repere_animation': [(0, 0)],
            'coord_fenetre_animation': [],
            'etape': 0,
            'animation': False,
            'animation_en_cours': False,
            'deux_grilles': False,
            'canvas_id': None,
            'parcours_libre': False,
            'parcours_propose': [{'x': 0, 'y': 0, 'etape': 0}],
            'selectionner_case': False,
            'case_selectionnee': None,
            'indication_parcours': False
        }
        self.puce = True
        self.ran_program = False
        self.drawingFlag = create_proxy([None])     # dynamic flag, mutated from the JS layer on the fly


    def centrer(self, *_, globals=None):
        """
        Si `globals` est utilisé, ce doit être le dict issue de `globals()`, et à loa fin de
        l'appel, les méthode de cette instance seront mise en place en tant que fonctions
        dans l'espace de noms de l'utilisateur.
        """
        # on récupère le numéro de ligne appelant cette fonction
        ligne = currentframe().f_back.f_lineno
        self.alien = {
            'taille_case': TAILLE_CASE,
            'largeur': TAILLE_CASE * 15,
            'hauteur': TAILLE_CASE * 15 + MARGE_HAUT,
            'pos': {'x': 0, 'y': 0, 'ligne': ligne, 'etape': 0},
            'positions': [{'x': 0, 'y': 0, 'ligne': ligne, 'etape': 0}],
            'num_lignes': True,
            'etapes': False,
            'comparaison': False,
            'bonnes_positions': [],
            'coord_repere_animation': [(0, 0)],
            'coord_fenetre_animation': [],
            'etape': 0,
            'animation': False,
            'animation_en_cours': False,
            'deux_grilles': False,
            'canvas_id': None,
            'parcours_libre': False,
            'parcours_propose': [{'x': 0, 'y': 0, 'etape': 0}],
            'selectionner_case': False,
            'case_selectionnee': None,
            'indication_parcours': False
        }
        self.ran_program = False

        # Affecte automatiquement les fonctions/méthodes de l'instance en cours dans l'espace global:
        if globals is not None:
            for func in self.get_functions():
                globals[func.__name__] = func


    def get_functions(self):
        return [
            getattr(self, name) for name in 'haut,bas,gauche,droite,case,ligne,colonne'.split(',')
        ]



    def dessiner_grille(self,x=0, y=0):
        """
        Dessine la grille complète.

        Paramètres
        ------
        x : abscisse du coin supérieur gauche
        y : ordonnée du coin supérieur gauche
        (utile pour dessiner deux grilles)
        """
        self.p5.textFont("Arial")
        self.p5.strokeWeight(1)
        self.p5.textSize(TAILLE_CASE // 3)
        for i in range(len(LETTRES)):
            c = LETTRES[i]
            for j,n in enumerate(NOMBRES):

                # couleur de la case
                is_border_or_center = c in ("A", "H", "O") or n in (1, 8, 15)
                bgd = (255, 166, 166) if is_border_or_center else (255, 215, 215)
                self.p5.fill(*bgd)

                # dessin de la case
                self.p5.square(x + j * TAILLE_CASE , MARGE_HAUT + y + i * TAILLE_CASE, TAILLE_CASE)

                # écriture du numéro de la case
                self.p5.fill(50)
                nom_case = f"{ c }{ n :0>2}"
                """
                if n >= 10:
                    self.p5.text(nom_case, x + j * TAILLE_CASE + TAILLE_CASE//4 , \
                    MARGE_HAUT + y + i * TAILLE_CASE + 2*TAILLE_CASE//3)
                else:
                    self.p5.text(nom_case, x + j * TAILLE_CASE + TAILLE_CASE//3 , \
                    MARGE_HAUT + y + i * TAILLE_CASE + 2*TAILLE_CASE//3)
                """
                self.p5.text(
                    nom_case,
                    x + j * TAILLE_CASE + TAILLE_CASE//4,
                    MARGE_HAUT + y + i * TAILLE_CASE + 2 * TAILLE_CASE//3
                )

    def dessiner_deplacement(self,positions, img, etape_fin=None, num_grille=1):
        """
        Dessine le déplacement de l'alien.

        Paramètres
        ----------
        positions
            une liste de dictionnaires contenant les différentes positions de l'alien
        img
            l'image de l'alien
        etape_fin
            un entier correspondant à l'étape finale souhaitée du déplacement
            Par exemple, si etape_fin = 3, le déplacement est dessiné des positions 0 à 3.
            Vaut None par défaut : tout le déplacement est dessiné
        num_grille
            un entier (1 ou 2) correspondant à la grille dans laquelle l'alien est dessiné
            Par défaut, il est dessiné dans la grille 1
        """
        # Dessin de la première position
        self.dessiner_alien(0, positions, img, num_grille)

        # Écriture du numéro de ligne du script ou de l'étape du déplacement
        if not self.alien['etapes']:
            if self.alien['num_lignes']:
                self.ecrire_numero_ligne(0, positions, img, num_grille)
        else:
            self.ecrire_numero_etape(0, positions, img, num_grille)

        # Position finale souhaitée
        if etape_fin is not None and etape_fin <= len(positions) - 2:
            position_finale = etape_fin
        else:
            position_finale = len(positions) - 1

        # Dessin des positions suivantes
        for i in range(position_finale):
            self.dessiner_segment(i, positions, img, num_grille)
            self.dessiner_alien(i+1, positions, img, num_grille)
            if not self.alien['etapes']:
                if self.alien['num_lignes']:
                    self.ecrire_numero_ligne(i+1, positions, img, num_grille)
            else:
                self.ecrire_numero_etape(i+1, positions, img, num_grille)

    def dessiner_case_finale(self, num_grille=1):
        """Marque la case finale"""
        if num_grille == 1:
            abs_centre = 7 * TAILLE_CASE
        elif num_grille == 2:
            abs_centre = 7 * TAILLE_CASE + 16 * TAILLE_CASE
        ord_centre = MARGE_HAUT + 7 * TAILLE_CASE
        abscisse = abs_centre + self.alien['positions'][-1]['x'] * TAILLE_CASE
        ordonnee = ord_centre - self.alien['positions'][-1]['y'] * TAILLE_CASE
        self.p5.stroke(255)
        self.p5.strokeWeight(5)
        self.p5.noFill()
        self.p5.rect(abscisse, ordonnee, TAILLE_CASE)

    def dessiner_alien(self,i, positions, img, num_grille):
        """
        Dessine l'alien à l'étape i.

        Paramètres
        ----------
        i
            un entier égal à l'étape à dessiner
        positions
            une liste de dictionnaires contenant les différentes positions de l'alien
        img
            l'image de l'alien
        num_grille
            un entier (1 ou 2) correspondant à la grille dans laquelle l'alien est dessiné
        """
        if num_grille == 1:
            abs_centre = 7 * TAILLE_CASE
        elif num_grille == 2:
            abs_centre = 7 * TAILLE_CASE + 16 * TAILLE_CASE
        ord_centre = MARGE_HAUT + 7 * TAILLE_CASE
        abscisse = abs_centre + positions[i]['x'] * TAILLE_CASE
        ordonnee = ord_centre - positions[i]['y'] * TAILLE_CASE
        self.p5.image(img, abscisse, ordonnee, TAILLE_CASE, TAILLE_CASE)


    def dessiner_segment(self,i, positions, img, num_grille):
        """ Dessine le segment reliant les étapes i et i+1. """
        if num_grille == 1:
            abs_centre = 7 * TAILLE_CASE
        elif num_grille == 2:
            abs_centre = 7 * TAILLE_CASE + 16 * TAILLE_CASE
        ord_centre = MARGE_HAUT + 7 * TAILLE_CASE
        abs1 = abs_centre + positions[i]['x'] * TAILLE_CASE
        ord1 = ord_centre - positions[i]['y'] * TAILLE_CASE
        abs2 = abs_centre + positions[i+1]['x'] * TAILLE_CASE
        ord2 = ord_centre - positions[i+1]['y'] * TAILLE_CASE
        if img == self.image_alien:
            self.p5.stroke(255)
        elif img == self.image_alien2:
            self.p5.stroke(129, 185, 221)
        self.p5.strokeWeight(3)
        self.p5.line(abs1 + TAILLE_CASE // 2, ord1 + TAILLE_CASE // 2, abs2 + TAILLE_CASE // 2, ord2 + TAILLE_CASE // 2)


    def _ecrire_numero(self, i, positions, num_grille, axe):
        if num_grille == 1:
            abs_centre = 7 * TAILLE_CASE
        elif num_grille == 2:
            abs_centre = 7 * TAILLE_CASE + 16 * TAILLE_CASE
        ord_centre = MARGE_HAUT + 7 * TAILLE_CASE
        abscisse = abs_centre + positions[i]['x'] * TAILLE_CASE
        ordonnee = ord_centre - positions[i]['y'] * TAILLE_CASE
        self.p5.stroke(255)
        self.p5.strokeWeight(3)
        self.p5.fill(0)
        self.p5.textSize(TAILLE_CASE // 3 + 2)
        self.p5.text(positions[i][axe], abscisse + 3*TAILLE_CASE//4, ordonnee + TAILLE_CASE)

    def ecrire_numero_ligne(self, i, positions, img, num_grille):
        """ Écrit à côté de l'alien le numéro de la ligne du script qui amène
        l'alien à l'étape i. """
        self._ecrire_numero(i, positions, num_grille, 'ligne')

    def ecrire_numero_etape(self, i, positions, img, num_grille):
        """ Écrit à côté de l'alien le numéro de l'étape i.
        On numérote les étapes à partir de 1. """
        self._ecrire_numero(i, positions, num_grille, 'etape')


    haut   = move_factory('haut',    0,  1)
    bas    = move_factory('bas',     0, -1)
    gauche = move_factory('gauche', -1,  0)
    droite = move_factory('droite',  1,  0)

    def case(self):
        coord = self.conversion_coordonnees_en_case(self.alien['pos']['x'],self.alien['pos']['y'])
        return coord

    def ligne(self):
        return self.case()[0]

    def colonne(self):
        return self.case()[1:]


    def afficher_deplacement(self, etapes=False, num_lignes=True, animation=False):
        """
        Affiche tout le déplacement à l'écran en appelant la fonction run().

        Paramètres
        ----------
        etapes
            booléen dont la valeur détermine si on affiche le numéro des étapes
            à côté de chaque position. Par défaut, ce n'est pas affiché.
        num_lignes
            booléen dont la valeur détermine si on affiche le numéro de la ligne
            du script à côté de chaque position. Par défaut, c'est affiché.
        animation
            booléen dont la valeur détermine si l'animation est lancée.
            L'animation consiste à pouvoir animer le déplacement de l'alien, avec
            un mode pas à pas possible.
            Par défaut, l'animation n'est pas lancée : on obtient le déplacement
            complet directement.
        """
        if not etapes:
            self.alien['etapes'] = False
            self.alien['num_lignes'] = True
        else:
            self.alien['etapes'] = True
            self.alien['num_lignes'] = False

        if not num_lignes:
            self.alien['num_lignes'] = False
        else:
            self.alien['num_lignes'] = True

        if animation:
            self.alien['animation'] = True

        if self.alien['etapes']:
            print("Les nombres correspondent aux différentes étapes.")
        elif self.alien['num_lignes']:
            print("Les nombres correspondent aux numéros de lignes du programme.")

        self.run(target=self.cible, stop_others=False)


    def est_case_valide(self,case):
        """ Renvoie True si et seulement si case est valide (de "A1" à "O15"). """
        valide = isinstance(case, str) and re.fullmatch(r'[A-O]\d\d?', case) and int(case[1:]) in NOMBRES
        assert valide, f"case invalide: {case!r}"
        return valide       # backward compatibility (kinda)


    def conversion_case_en_coordonnees(self, case):
        """
        Convertit une case en coordonnées.

        Paramètres
        ----------
        case
            chaine de caractères entre 'A1' et 'O15'

        Renvoie
        -------
        Une liste de deux éléments

        Exemples
        --------
        >>> conversion_case_en_coordonnees('H8')
        [0, 0]
        >>> conversion_case_en_coordonnees('F11')
        [3, 2]
        >>> conversion_case_en_coordonnees('A1')
        [-7, 7]
        """
        self.est_case_valide(case)
        lettre_choisie = case[0].upper()
        nb_choisi = int(case[1:])
        pos_lettre = ord(lettre_choisie)-65
        coord = [nb_choisi - 8, 7 - pos_lettre]  # 7 est la position de la lettre H
        return coord

    def conversion_coordonnees_en_case(self,x, y):
        """
        Convertit les coordonnées x, y en la bonne case.

        Exemples
        --------
        >>> conversion_coordonnees_en_case(0, 0)
        'H8'
        >>> conversion_coordonnees_en_case(-7, 7)
        'A1'
        """
        assert -7 <= x <= 7, "case inatteignable (en dehors de la grille)"
        assert -7 <= y <= 7, "case inatteignable (en dehors de la grille)"
        pos_lettre = 7 - y
        lettre = LETTRES[pos_lettre]
        nb = x + 8
        if nb < 10:
            nombre = "0" + str(nb)
        else:
            nombre = str(nb)
        return lettre + nombre

    def cases_du_parcours(self,positions=None):
        """
        Renvoie la liste des cases correspondant aux différentes positions
        du parcours de l'alien.

        Paramètres
        ---------
        positions
            une liste de dictionnaires contenant les coordonnées de chaque position
        c
        Renvoie
        ------
        Une liste de cases (str) du parcours.

        Exemple
        -------
        >>> pos = [{'x': 0, 'y': 0}, {'x': 2, 'y': 0}, {'x': 2, 'y': -3}]
        >>> cases_du_parcours(pos)
        ['H8', 'H10', 'K10']
        """
        if positions == None:
            positions = self.alien['positions']
        liste_cases = []
        try:
            for p in positions:
                liste_cases.append(self.conversion_coordonnees_en_case(p['x'], p['y']))
        except AssertionError:
                print("\u274C La prochaine case n'est pas atteignable")
                etape_erreur = p['etape']
                nouvelles_positions = []
                etape = positions[0]['etape']
                i = 0
                while etape != etape_erreur:
                    nouvelles_positions.append(positions[i])
                    i += 1
                    etape = positions[i]['etape']
                    self.alien['positions'] = nouvelles_positions
        return liste_cases

    def compter_chaines_non_vides(self,liste_de_chaines):
        """
        Renvoie le nombre de chaînes de liste qui sont différentes de la chaîne vide
        ou d'une chaîne constituée uniquement d'espaces.

        Paramètres
        ----------
        liste_de_chaines
            une liste de chaînes de caractères

        Sortie
        ------
        Un entier positif ou nul
        """
        n = len(liste_de_chaines)
        n_vides = sum( not chaine.strip(' ') for chaine in liste_de_chaines )
        return n - n_vides

    def creer_liste_sans_chaine_vide_ou_d_espaces_en_debut_et_fin(self,liste_de_chaines):
        """
        Crée une nouvelle liste mais sans les éléments
        """
        return [chaine for chaine in liste_de_chaines if chaine.strip(' ')]

    def nb_lignes_python_derniere_cellule_executee(self):
        """
        Analyse le programme écrit dans la dernière cellule exécutée par l'utilisateur.
        Renvoie un tuple dont le premier élément est la liste des lignes de la dernière
        cellule exécutée et dont le second est le nombre de lignes contenant du code Python
        dans celle-ci.
        """
        # ligne d'appel à la fonction `verification_programme`
        # il faut revenir deux frames en arrière !
        ligne = currentframe().f_back.f_back.f_lineno

        # le code exécuté dans la dernière cellule
        programme_cellule = __USER_CODE__
        # la liste avec les lignes de ce code jusqu'à l'appel à `verification_programme` (exclue)
        lignes_programme = programme_cellule.split('\n')[:ligne-1]

        # le nombre de lignes Python de la dernière cellule de code exécutée
        nb_lignes = self.compter_chaines_non_vides(lignes_programme)

        # la liste des lignes Python nettoyée au début et à la fin
        # (ne sert pas pour le moment : peut être utilisée pour récrire le code dans la fenêtre ou dans une image)
        lignes_programme_nettoyee = self.creer_liste_sans_chaine_vide_ou_d_espaces_en_debut_et_fin(lignes_programme)

        return nb_lignes

    def verifier_programme(self, liste_bonnes_cases, nb_max_lignes=None, animation=False, etapes=True):
        """
        Vérifie si le programme écrit correspond au bon parcours `liste_bonnes_cases`,
        et éventuellement que le nombre de lignes ne dépasse `nb_max_lignes`.

        Paramètres
        ----------
        liste_bonnes_cases
            une liste avec les cases du parcours
        nb_max_lignes
            un entier correspond au nombre maximal de lignes autorisé (optionnel)
        animation
            booléen dont la valeur détermine si l'animation est lancée.
            L'animation consiste à pouvoir animer le déplacement de l'alien, avec
            un mode pas à pas possible.
            Par défaut, l'animation n'est pas lancée : on obtient le déplacement
            complet directement.

        Si on utilise cette fonction, l'affichage des numéros de lignes est
        automatiquement désactivée car on ne dispose pas de ces numéros pour
        le parcours réponse.
        """
        # Déjà testé (tests publics vs validations)
        if self.ran_program:
            return

        self.puce = True
        # mise à jour des modalités du parcours
        self.alien['comparaison'] = True  # il y a une comparaison entre deux parcours
        if not animation:
            self.alien['deux_grilles'] = True  # deux grilles affichées si pas d'animation
        else:
            self.alien['deux_grilles'] = False  # sinon une seule grille
            self.alien['animation'] = True  # et une animation

        # nb de ligne de la dernière cellule exécutée
        nb_lignes = self.nb_lignes_python_derniere_cellule_executee()

        # comparaison du programme proposé à la liste de cases attendue
        correct = liste_bonnes_cases == self.cases_du_parcours(self.alien['positions'])

        # test de la longueur du programme proposé
        if nb_max_lignes:  # si nb_max_lignes n'est pas None
            # comparaison de la longueur du prog proposé avec le nombre max de lignes attendu
            longueur = nb_lignes <= nb_max_lignes
        else:  # si la valeur associée à la clé `nb_max_lignes` est None
            longueur = True

        # Prépare un éventuel test de la stdout, côté PMT:
        sys.stdout.truncate(0)
        sys.stdout.seek(0)

        # affichage de la correction
        if correct:
            #alien['comparaison'] = False
            if longueur:
                if self.alien['deux_grilles']:
                    print("✅ Excellent !")
                else:
                    print("✅ Excellent !\n Ci-dessous vous pouvez animer votre déplacement en bleu et vérifier qu'il correspond bien à celui attendu en blanc.")
            else:
                self.p5.print(f"⚠️ Le parcours est bon mais votre programme fait {nb_lignes} lignes alors qu'il doit en faire au plus {nb_max_lignes}.")
                if self.alien['deux_grilles']:
                    print("Ci-dessous à gauche votre déplacement et à droite celui qu'il faut obtenir.")
                else:
                    print("Ci-dessous vous pouvez animer votre déplacement en bleu et le comparer à celui qu'il faut obtenir en blanc.")
        else:
            if self.alien['deux_grilles']:
                print("❌ C'est à revoir. Ci-dessous à gauche votre déplacement et à droite celui qu'il faut obtenir :")
            elif self.alien['animation']:
                print("❌ C'est à revoir. Ci-dessous vous pouvez animer votre déplacement en bleu et le comparer au déplacement blanc qu'il faut obtenir :")
            else:
                print("❌ C'est à revoir. Ci-dessous votre déplacement.")
            #alien['comparaison'] = True

        self.creer_bonnes_positions_a_partir_listes_de_cases(liste_bonnes_cases)
        self.afficher_deplacement(etapes=etapes, num_lignes=False)  # OBLIGATOIREMENT num_lignes=False !!
        self.ran_program = True



    def creer_bonnes_positions_a_partir_listes_de_cases(self,liste_cases):
        """
        Crée la liste des coordonnées à partir d'une liste de cases.
        Utilisé uniquement à la fin de la fonction `verification_programme` pour
        créer les bonnes positions à partir d'une correction donnée dans le
        dictionnaire `REPONSES_EXERCICES`
        """
        bonnes_positions = []
        for etape, case in enumerate(liste_cases):
            coord = self.conversion_case_en_coordonnees(case)
            bonnes_positions.append({'x': coord[0], 'y': coord[1], 'etape': etape})
        self.alien['bonnes_positions'] = bonnes_positions  # mise à jour du dictionnaire `alien`


    ####---- BOUTONS D'ANIMATIONS ----####

    def dessiner_boutons_animation(self):
        """
        Dessine les boutons d'animation.
        Ne se positionnent pas bien selon la taille des cases.
        """
        self.p5.fill(239)
        self.p5.stroke(0)
        self.p5.strokeWeight(1)
        for i in range(5):
            self.p5.rect(75 * i + 45, self.alien['hauteur'] + 20, 65, 25, 2)

    def ecrire_texte_boutons_animation(self):
        """
        Écrit le texte sur chaque bouton.
        """
        self.p5.textSize(12)
        self.p5.textFont('Consolas')
        self.p5.noStroke()
        self.p5.fill(20)
        textes = ["▶Lecture", "<< Début", " < Préc.", " Suiv. >", " Fin >>"]
        for i in range(5):
            self.p5.text(textes[i], 75 * i + 50, self.alien['hauteur'] + 38)




    #### ---- GESTION DES CLICS ---- ####

    def survol_lecture(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton lecture. """
        return 45 <= x <= 45 + 60 and self.alien['hauteur'] + 20 <= y <= self.alien['hauteur'] + 45

    def survol_debut(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton début. """
        return 120 <= x <= 120 + 60 and self.alien['hauteur'] + 20 <= y <= self.alien['hauteur'] + 45

    def survol_reculer(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton reculer. """
        return 195 <= x <= 195 + 60 and self.alien['hauteur'] + 20 <= y <= self.alien['hauteur'] + 45

    def survol_avancer(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton avancer. """
        return 270 <= x <= 270 + 60 and self.alien['hauteur'] + 20 <= y <= self.alien['hauteur'] + 45

    def survol_fin(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton fin. """
        return 345 <= x <= 345 + 60 and self.alien['hauteur'] + 20 <= y <= self.alien['hauteur'] + 45

    def demarrer_lecture(self):
        """
        (Re)démarre l'animation automatique.
        """
        en_cours = self.alien['etape'] < len(self.alien['positions']) - 1
        self.alien['animation_en_cours'] = en_cours

    def debut(self):
        """
        Dessine l'alien à sa position de départ (et stoppe l'animation automatique).
        """
        self.alien['animation_en_cours'] = False
        self.alien['etape'] = 0  # première étape
        self.p5.stroke(50)
        self.dessiner_grille()
        self.p5.stroke(255)
        if self.alien['comparaison']:
            self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=1)
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
        else:
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)

    def reculer(self):
        """
        Recule l'alien d'une position (et stoppe l'animation automatique).
        """
        self.alien['animation_en_cours'] = False
        if self.alien['etape'] > 0:
            self.alien['etape'] = self.alien['etape'] - 1
            self.p5.stroke(50)
            self.dessiner_grille()
            self.p5.stroke(255)
            if self.alien['comparaison']:
                self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=1)
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
            else:
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)

    def avancer(self):
        """
        Avance l'alien d'une position (et stoppe l'animation automatique).
        """
        self.alien['animation_en_cours'] = False
        if self.alien['etape'] < len(self.alien['positions']) - 1:
            self.alien['etape'] = self.alien['etape'] + 1
            self.p5.stroke(50)
            self.dessiner_grille()
            self.p5.stroke(255)
            if self.alien['comparaison']:
                self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=1)
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
            else:
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)

    def fin(self):
        """
        Dessine l'alien à sa position finale (et stoppe l'animation automatique).
        """
        self.alien['animation_en_cours'] = False
        self.alien['etape'] = len(self.alien['positions']) - 1
        self.p5.stroke(50)
        self.dessiner_grille()
        self.p5.stroke(255)
        #strokeWeight(1)
        if self.alien['comparaison']:
            self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=1)
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
        else:
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)


    def gerer_animation_clic(self,x, y):
        """
        Détecte les clics sur les boutons et gère l'avancée de l'animation.
        """
        if self.p5.mouseIsPressed and self.survol_lecture(x, y):
            self.demarrer_lecture()
        elif self.p5.mouseIsPressed and self.survol_debut(x, y):
            self.debut()
            self.p5.frameRate(3)  # POUR NE PAS DÉTECTER PLUSIEURS CLICS !!
        elif self.p5.mouseIsPressed and self.survol_reculer(x, y):
            self.reculer()
            self.p5.frameRate(3)
        elif self.p5.mouseIsPressed and self.survol_avancer(x, y):
            self.avancer()
            self.p5.frameRate(3)
        elif self.p5.mouseIsPressed and self.survol_fin(x, y):
            self.fin()
            self.p5.frameRate(3)




    #### ---- ANIMATION ---- ####

    def tester_fin_animation(self):
        """
        Teste si la dernière position du déplacement est atteinte.
        Sinon, itère d'une unité l'étape à afficher.
        """
        if self.alien['animation_en_cours'] and self.alien['etape'] == len(self.alien['positions']) - 1:
            self.alien['animation_en_cours'] = False
        else:
            self.alien['etape'] = self.alien['etape'] + 1

    def animer(self):
        """
        Dessine l'alien à la position en cours.
        """
        if self.alien['comparaison']:
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
        else:
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)
        self.tester_fin_animation()
        self.p5.frameRate(3)  # POUR NE PAS DÉTECTER PLUSIEURS CLICS !!

    def taille(self, n=30):
        """
        Pour définir la taille d'une case en pixels.
        Ne pas choisir des valeurs trop petites ou trop grandes.
        """
        global TAILLE_CASE
        TAILLE_CASE = n



    ####---- TELECHARGER L'IMAGE DE LA FENETRE GRAPHIQUE ----####

    def sauvegarder(self,nom_fichier=''):
        """
        Lance le téléchargement de la dernière fenêtre graphique.
        L'image est téléchargée au format PNG et porte le nom passé en paramètre
        sous forme d'une chaîne de caractères.
        """
        #self.p5.stop()
        self.p5.save(nom_fichier)


    ####---- GESTION DU PARCOURS LIBRE ----####

    def dessiner_parcours(self, indication=False):
        """
        Permet à l'utilisateur de dessiner le parcours de l'alien.
        """
        self.alien['parcours_libre'] = True
        self.alien['parcours_propose'] = [{'x': 0, 'y': 0, 'etape': 0}]
        self.alien['num_lignes'] = False  # OBLIGATOIRE
        self.alien['etapes'] = True
        self.alien['indication_parcours'] = indication

        #print("Dessinez le parcours complet en cliquant sur les bonnes cases. Vous pouvez annuler la dernière position en cliquant dessus")
        self.run(target=self.cible, stop_others=False)


    def coord_case_cliquee(self,x, y, taille_case):
        """ Renvoie les coordonnées de la case cliquée.
        ATTENTION ! x et y sont les coordonnées dans le repère (et non de la grille)"""
        return int(x//taille_case - 7), int((MARGE_HAUT-y) // taille_case + 8 )


    def gerer_clic_sur_grille(self,x, y):
        """Gère les clics sur la grille et le survol des boutons."""
        largeur = self.alien['largeur']
        hauteur = self.alien['hauteur']
        if self.p5.mouseIsPressed and 0 <= x < largeur and MARGE_HAUT <= y < hauteur:
            # coordonnées de la case cliquée
            x_case, y_case = self.coord_case_cliquee(x, y, self.alien['taille_case'])
            # modification du parcours proposé
            self.modifier_parcours_propose(x_case, y_case)
            self.p5.frameRate(3)
        if self.survol_btn_validation(x, y) or self.survol_btn_reinitialiser(x, y) or self.survol_btn_reponse(x, y):
            self.p5.cursor('pointer')
        else:
            self.p5.cursor(self.p5.ARROW)


    def modifier_parcours_propose(self,x_case, y_case):
        """Modifie le parcours proposé par l'utilisateur."""
        nb_etapes = len(self.alien['parcours_propose'])
        derniere_position = self.alien['parcours_propose'][-1]
        if (derniere_position['x'] == x_case) ^ (derniere_position['y'] == y_case):  # XOR
            self.alien['parcours_propose'].append({'x': x_case, 'y': y_case, 'etape': nb_etapes})
            self.p5.stroke(50)
            self.p5.strokeWeight(3)
            self.dessiner_grille()
        if derniere_position['x'] == x_case and derniere_position['y'] == y_case and len(self.alien['parcours_propose']) != 1:
            self.alien['parcours_propose'].pop()
            self.p5.stroke(50)
            self.p5.strokeWeight(3)
            self.dessiner_grille()



    ####---- GESTION DE LA SELECTION DE LA CASE FINALE ----####

    def selectionner_case_finale(self):
        """
        Permet à l'utilisateur de sélectionner la case finale.
        """
        self.alien['selectionner_case'] = True
        print("Sélectionnez la case finale puis vérifiez votre réponse.")
        self.run(target=self.cible, stop_others=False)


    def gerer_selection_case(self,x, y):
        """Pour gérer la sélection d'une case par un clic."""
        largeur = self.alien['largeur']
        hauteur = self.alien['hauteur']
        if self.p5.mouseIsPressed and 0 <= x <= largeur and MARGE_HAUT <= y <= hauteur:
            # coordonnées de la case cliquée
            x_case, y_case = self.coord_case_cliquee(x, y, self.alien['taille_case'])
            self.marquer_case(x_case, y_case)


    def marquer_case(self,x_case, y_case, correct=None):
        """
        Marque la case de coordonnées (x_case, y_case) dans la grille en dessinant
        un rectangle coloré sur ses contours.

        Parametres
        ----------
        x_case et y_case
            des entiers compris entre -7 et 7 correspondant aux coordonnées
            de la case dans la grille (coordonnées de la case centrale: (0, 0)).
        correct
            un booléen permettant de définir la couleur de la case
            (None : blanc, True: vert, False: rouge)

        """
        self.alien['case_selectionnee'] = (x_case, y_case)
        abs_centre = 7 * TAILLE_CASE
        ord_centre = MARGE_HAUT + 7 * TAILLE_CASE
        abscisse = abs_centre + x_case * TAILLE_CASE
        ordonnee = ord_centre - y_case * TAILLE_CASE

        self.p5.stroke(50)
        self.p5.strokeWeight(3)
        self.dessiner_grille()
        self.dessiner_alien(0, self.alien['positions'], img=self.image_alien, num_grille=1)

        if correct is None:
            self.p5.stroke(255)  # en blanc
        elif correct == True:
            self.p5.stroke(111, 196, 169)
        else:
            self.p5.stroke(200, 0, 0)
        self.p5.strokeWeight(5)
        self.p5.noFill()
        self.p5.rect(abscisse , ordonnee, TAILLE_CASE)


    ####---- BOUTONS DESSIN LIBRE ----####

    def dessiner_boutons_travail_autonome(self):
        """Dessine les boutons dans le cas où un parcours libre doit être construit."""
        self.dessiner_btn_validation()
        self.dessiner_btn_reinitialiser()
        # self.dessiner_btn_reponse()
        self.dessiner_commentaire("")


    def dessiner_commentaire(self,comment):
        self.p5.fill(255)
        self.p5.noStroke()
        self.p5.rect(10, self.alien['hauteur'] + 48, 17*self.alien['taille_case'], 30)
        self.p5.textSize(14)
        self.p5.textFont('Consolas')
        self.p5.noStroke()
        self.p5.fill(20)
        self.p5.text(comment, 17, self.alien['hauteur'] + 68)


    def _dessiner_bouton(self, txt, nx):
        self.p5.fill(239)
        self.p5.stroke(0)
        self.p5.strokeWeight(1)
        self.p5.rect(nx*self.alien['taille_case'], self.alien['hauteur'] + 15, 3*self.alien['taille_case'], 30)
        self.p5.textSize(14)
        self.p5.textFont('Consolas')
        self.p5.noStroke()
        self.p5.fill(20)
        self.p5.text(txt, nx*self.alien['taille_case'] + 16, self.alien['hauteur'] + 35)

    def dessiner_btn_validation(self):
        self._dessiner_bouton("Valider", 2)

    def dessiner_btn_reinitialiser(self):
        self._dessiner_bouton("Effacer", 6)

    def dessiner_btn_reponse(self):
        self._dessiner_bouton("Réponse", 10)

    ####---- GESTION DES BOUTONS -----####

    # BOUTON DE VALIDATION

    def survol_btn_validation(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton Valider. """
        abs_correcte = 2*self.alien['taille_case'] <= x <= 5*self.alien['taille_case']  # largeur = 3*alien['taille_case']
        ord_correcte = self.alien['hauteur'] + 15 <= y <= self.alien['hauteur'] + 15 + 30
        return abs_correcte and ord_correcte


    def gerer_clic_btn_validation(self,x, y):
        """Teste si la case sélectionnée ou si le parcours proposé est correct
        lorsque l'utilisateur clique sur le bouton de validation."""
        if self.p5.mouseIsPressed and self.survol_btn_validation(x, y):
            if self.alien['parcours_libre'] :  # cas d'un parcours à dessiner
                success = False
                liste_bonnes_positions = [{'x': p['x'], 'y': p['y'], 'etape': p['etape']} for p in self.alien['positions']]
                if self.alien['parcours_propose'] == liste_bonnes_positions:
                    self.dessiner_commentaire("✅ Excellent !")
                    success = True
                elif self.alien['indication_parcours']:
                    indice = self.comparer(self.alien['parcours_propose'], liste_bonnes_positions)
                    if indice == "-":
                        self.dessiner_commentaire("❌ Le parcours proposé est incomplet, il manque des positions.")
                    elif indice == "+":
                        self.dessiner_commentaire("❌ Le parcours proposé est trop long, il y a des positions en trop.")
                    else:
                        self.dessiner_commentaire(f"❌ Le parcours proposé est incorrect, il y a un problème à partir de l'étape {indice + 1}.")
                else:
                    self.dessiner_commentaire("❌ Le parcours proposé est incorrect.")
                self.p5.frameRate(3)


            elif self.alien['selectionner_case']:  # cas de la case finale à sélectionner
                if self.alien['case_selectionnee'] is None:
                    self.dessiner_commentaire("Vous devez sélectionner une case.")
                else:
                    coord_case_finale = (self.alien['positions'][-1]['x'], self.alien['positions'][-1]['y'])
                    if self.alien['case_selectionnee'] == coord_case_finale:

                        self.marquer_case(self.alien['case_selectionnee'][0], self.alien['case_selectionnee'][1], correct=True)
                        self.dessiner_commentaire("✅ Excellent !")
                        #self.p5.stop()
                    else:
                        self.marquer_case(self.alien['case_selectionnee'][0], self.alien['case_selectionnee'][1], correct=False)
                        self.dessiner_commentaire("❌ C'est à revoir.")
                self.p5.frameRate(3)


    def comparer(self,liste_test, bonne_liste):
        """
        Renvoie -1 si les deux listes sont identiques.
        Sinon, renvoie :
            '-' si liste_test est le début de bonne_liste
            '+' si bonne_liste est le début de liste_test
            le premier indice i tel que liste_test[i] != bonne_liste[i], sinon.
        """
        if liste_test == bonne_liste:
            return -1
        n1 = len(liste_test)
        n2 = len(bonne_liste)
        n = min(n1, n2)  # n est la taille mini des deux listes
        i = 0
        while i < n:
            if liste_test[i] == bonne_liste[i]:
                i = i + 1
            else:
                break
        if i == n:  # si aucune différence sur les n premiers termes
            if n1 < n2:
                return '-'  # si liste_test est plus petite que bonne_liste
            else:
                return '+'  # si liste_test est plus grande que bonne_liste
        else:
            return i  # indice de la première différence

    # BOUTON DE REINITIALISATION

    def survol_btn_reinitialiser(self,x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton Effacer. """
        abs_correcte = 6*self.alien['taille_case'] <= x <= 9*self.alien['taille_case']  # largeur = 3*alien['taille_case']
        ord_correcte = self.alien['hauteur'] + 15 <= y <= self.alien['hauteur'] + 15 + 30
        return abs_correcte and ord_correcte


    def gerer_clic_btn_reinitialiser(self, x, y):
        """Réinitiatilise la case sélectionnée ou le parcours proposé
        lorsque l'utilisateur clique sur le bouton de réinitialisation."""
        if self.p5.mouseIsPressed and self.survol_btn_reinitialiser(x, y):

            self.p5.stroke(50)
            self.p5.strokeWeight(3)

            # cas d'un parcours à dessiner
            if self.alien['parcours_libre'] :
                self.alien['parcours_propose'] = [{'x': 0, 'y': 0, 'etape': 0}]
                self.dessiner_grille()
                self.dessiner_commentaire("")

            # cas de la case finale à sélectionner
            elif self.alien['selectionner_case']:
                self.alien['case_selectionnee'] = None
                self.dessiner_grille()
                self.dessiner_alien(0, self.alien['positions'], img=self.image_alien, num_grille=1)

            self.p5.frameRate(3)


    # BOUTON DE REPONSE

    def survol_btn_reponse(self, x, y):
        """ Renvoie True si les coordonnées (x, y) de la souris sont sur le bouton Reponse. """
        abs_correcte = 10*self.alien['taille_case'] <= x <= 13*self.alien['taille_case']  # largeur = 3*alien['taille_case']
        ord_correcte = self.alien['hauteur'] + 15 <= y <= self.alien['hauteur'] + 15 + 30
        return abs_correcte and ord_correcte


    def gerer_clic_btn_reponse(self,x, y):
        """Affiche le bon déplacement et la case finale si l'utilisateur
        clique sur le bouton de réponse."""
        if self.p5.mouseIsPressed and self.survol_btn_reponse(x, y):
            #if self.alien['parcours_libre'] :  # cas d'un parcours à dessiner
            #    self.alien['parcours_libre'] = False
            #elif self.alien['selectionner_case']:  # cas de la case finale à sélectionner
            #    self.alien['selectionner_case'] = False

            case_finale = self.conversion_coordonnees_en_case(self.alien['positions'][-1]['x'], self.alien['positions'][-1]['y'])
            self.dessiner_commentaire(f"Voici la correction 👆. La case finale était {case_finale}.")
            self.p5.stroke(50)
            self.p5.strokeWeight(3)
            self.dessiner_grille()
            self.dessiner_case_finale(num_grille=1)
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, num_grille=1)



    ####---- FONCTIONS PRELOAD SETUP ET DRAW ----####

    @p5.hook
    def preload(self):
        """
        Pour charger les deux images avant l'exécution de setup().
        La fonction run() doit alors préciser d'exécuter la fonction preload().
        """
        self.image_alien = self.p5.loadImage('https://codex.forge.apps.education.fr/images/alien.svg')
        self.image_alien2 = self.p5.loadImage('https://codex.forge.apps.education.fr/images/alien2.svg')

    @p5.hook
    def setup(self):
        """
        Fonction setup nécessaire au module self.p5.
        Définit tous les paramètres nécessaires à l'affichage et affiche
        """
        # PARAMETRES ET CREATION DE LA FENETRE GRAPHIQUE
        if not self.alien['deux_grilles']:
            LARGEUR = TAILLE_CASE * 15
        else:
            LARGEUR = 2 * TAILLE_CASE * (15 + 1)
        if self.alien['animation'] or self.alien['parcours_libre'] or self.alien['selectionner_case']:
            HAUTEUR = TAILLE_CASE * 15 + MARGE_HAUT + MARGE_BAS
        else:
            HAUTEUR = TAILLE_CASE * 15 + MARGE_HAUT

        canvas = self.p5.createCanvas(LARGEUR, HAUTEUR)
        js.p5canvasAutoWidthAndAdmonitions(canvas, self.drawingFlag, LARGEUR, HAUTEUR, self.cible)

        self.p5.textFont("Calibri")
        self.p5.textSize(TAILLE_CASE // 3)


        # AFFICHAGES PRÉLIMINAIRES (ou définifs s'il n'y a pas d'animation)
        self.p5.stroke(50)
        self.p5.strokeWeight(3)
        if self.alien['deux_grilles']:
            # il y a nécessairement comparaison et pas d'animation !
            self.dessiner_grille()
            self.dessiner_grille(TAILLE_CASE*16, 0)  # deuxième grille
            self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, num_grille=1)
            self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=2)
            self.p5.noLoop()

        else:
            self.dessiner_grille()

            if self.alien['parcours_libre']:  #  pour dessiner le parcours avec la souris
                self.dessiner_deplacement(self.alien['parcours_propose'], img=self.image_alien, num_grille=1)
                self.dessiner_boutons_travail_autonome()

            elif self.alien['selectionner_case']:  #  pour sélectionner la case finale avec la souris
                self.dessiner_alien(0, self.alien['positions'], img=self.image_alien, num_grille=1)
                self.dessiner_boutons_travail_autonome()

            elif self.alien['comparaison']:
                # il y a nécessairement animation
                # on dessine le déplacement attendu
                self.dessiner_deplacement(self.alien['bonnes_positions'], img=self.image_alien, num_grille=1)
                # on dessine l'alien en position initiale (jusqu'à alien['etape'] qui vaut 1 initialement)
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien2, etape_fin=self.alien['etape'], num_grille=1)
                # on ajoute les boutons d'animations
                self.dessiner_boutons_animation()
                self.ecrire_texte_boutons_animation()

            elif self.alien['animation']:
                # on dessine l'alien en position initiale (jusqu'à alien['etape'] qui vaut 1 initialement)
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, etape_fin=self.alien['etape'], num_grille=1)
                # on ajoute les boutons d'animations
                self.dessiner_boutons_animation()
                self.ecrire_texte_boutons_animation()

            else:
                self.dessiner_deplacement(self.alien['positions'], img=self.image_alien, num_grille=1)
                self.p5.noLoop()

    @p5.hook
    def draw(self):
        """
        Fonction draw nécessaire au module self.p5.
        Actualise continuellement la fenêtre graphique.
        Ne sert qu'en cas d'animation.
        """
        # Do not draw/apply anything if the canvas is hidden inside a closed "???" admonition:
        if not self.drawingFlag[0]:
            return

        self.p5.frameRate(30)
        if self.alien['animation']:
            self.gerer_animation_clic(self.p5.mouseX, self.p5.mouseY)  # gestion clic sur boutons d'animations
            if self.alien['animation_en_cours']:
                self.animer()  # déplacement de l'alien
        if self.alien['parcours_libre']:
            self.gerer_clic_sur_grille(self.p5.mouseX, self.p5.mouseY)
            self.gerer_clic_btn_validation(self.p5.mouseX, self.p5.mouseY)
            self.gerer_clic_btn_reinitialiser(self.p5.mouseX, self.p5.mouseY)
            self.dessiner_deplacement(self.alien['parcours_propose'], img=self.image_alien, num_grille=1)
            # self.gerer_clic_btn_reponse(self.p5.mouseX, self.p5.mouseY)
        if self.alien['selectionner_case']:
            self.gerer_selection_case(self.p5.mouseX, self.p5.mouseY)
            self.gerer_clic_btn_validation(self.p5.mouseX, self.p5.mouseY)
            self.gerer_clic_btn_reinitialiser(self.p5.mouseX, self.p5.mouseY)
            # self.gerer_clic_btn_reponse(self.p5.mouseX, self.p5.mouseY)






def secret_tests():
    output = sys.stdout.getvalue()
    assert "✅ Excellent !" in output, "Ce n'est pas la bonne réponse!"
