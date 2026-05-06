

# --------- PYODIDE:code --------- #

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, ...)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ...

    while nb_mystere != ... and compteur < ...:
        compteur = compteur + ...
        if nb_mystere ... nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", ...)
        print("Nombre d'essais: ", ...)
    else:
        print("Perdu ! Le nombre était ", ...)

# --------- PYODIDE:corr --------- #

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input('Proposez un nombre entre 1 et 99 : '))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input('Trop petit ! Testez encore : '))
        else:
            nb_test = int(input('Trop grand ! Testez encore : '))

    if nb_mystere == nb_test:
        print('Bravo ! Le nombre était ', nb_mystere)
        print("Nombre d'essais : ", compteur)
    else:
        print('Perdu ! Le nombre était ', nb_mystere)

# --------- PYODIDE:secrets --------- #

# Tests secrets
import sys

vrai_randint = randint

class Joueur:
    def __init__(self, secret=None, reponse=None):
        self.debut = 1
        self.fin = 99
        self.compteur = 0
        self.secret = secret
        self.reponse = reponse  # on va toujours proposer cette réponse si pas None
        if self.reponse is not None:
            self.milieu = self.reponse
        else:
            self.milieu = (self.debut + self.fin) // 2

    def input(self, texte):
        if "petit" in texte:
            if self.reponse is None:
                self.debut = self.milieu + 1
            if self.secret is not None:
                assert self.secret >= self.milieu, "menteur"
        elif "grand" in texte:
            if self.reponse is None:
                self.fin = self.milieu - 1
            if self.secret is not None:
                assert self.secret <= self.milieu, "menteur"
        if self.reponse is None:
            self.milieu = (self.debut + self.fin) // 2
        self.compteur += 1
        return self.milieu

    def test_print(self):
        affichages = sys.stdout.getvalue().rstrip().split("\n")
        assert len(affichages) > 0, "Il n'y a aucun affichage à la fin de l'exécution de la fonction"
        try:
            texte, valeur = affichages[-1].rsplit(" ", 1)
            valeur = int(valeur)
        except:
            assert False, "Le format du message affiché ne permet pas de comprendre la valeur indiquée"
        if "Bravo" in texte:
            assert False, "On attendait le nombre d'essais comme dernier message"
        elif "Perdu" in texte:
            assert self.compteur <= 10, "la partie dure trop longtemps"
            assert self.compteur >= 10, "la partie se termine trop tôt"
            assert valeur != self.milieu, "pourtant la valeur avait été trouvée"
            if self.secret is not None:
                assert valeur == self.secret, "pas le bon nombre secret"
            assert self.debut <= valeur <= self.fin, "les réponses ne sont pas cohérentes"
        elif "Nombre" in texte:
            self.compteur == valeur, "le nombre d'essais n'est pas le bon"
            try:
                texte, valeur = affichages[-2].rsplit(" ", 1)
                valeur = int(valeur)
            except:
                assert False, "Le format du message affiché ne permet pas de comprendre la valeur indiquée"
            assert "Bravo" in texte, "On n'a pas droit à un petit message de félicitation ?"
            assert valeur == self.milieu, "mauvais nombre affiché"
            assert valeur == randint(1, 99), "pas le bon nombre secret"
        else:
            assert False, "le message ne correspond pas à quelque chose d'attendu"
        sys.stdout.truncate(0)
        sys.stdout.seek(0)

def faux_randint(x, y, i):
    assert x == 1 and y == 99, "on doit deviner entre 1 et 99"
    return i

# On va tester toutes les valeurs
#vrai_print = print
for i in range(1, 100):
    # On surcharge randint pour choisir le résultat
    randint = lambda x, y: faux_randint(x, y, i)
    joueur = Joueur()  # joueur normal
    input = joueur.input
    plus_ou_moins()
    joueur.test_print()
    joueur = Joueur(secret=i)  # joueur qui connaît le secret
    input = joueur.input
    plus_ou_moins()
    joueur.test_print()
    joueur = Joueur(secret=i, reponse=i)  # joueur qui trouve tout de suite
    input = joueur.input
    plus_ou_moins()
    joueur.test_print()
    if i < 99:
        joueur = Joueur(secret=i, reponse=i+1)  # joueur qui dit toujours trop grand
        input = joueur.input
        plus_ou_moins()
        joueur.test_print()
    if i > 1:
        joueur = Joueur(secret=i, reponse=i-1)  # joueur qui dit toujours trop petit
        input = joueur.input
        plus_ou_moins()
        joueur.test_print()


# --------- PYODIDE:post --------- #
#print = vrai_print  # on remet le print normal
input = __builtins__.input
if "vrai_randint" in globals():
    randint = vrai_randint
