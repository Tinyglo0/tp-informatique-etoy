# --------- PYODIDE:dessin --------- #
@auto_run
def _():
    import p5
    from alien_python import App

    app = App("figureFIGURE")
    haut,bas,gauche,droite,case,ligne,colonne = app.get_functions()

    ## {{ [py]:dessin }}

    app.dessiner_parcours()



# --------- PYODIDE:grille --------- #
@auto_run
def _grill():
    import p5
    from alien_python import App

    app = App("grilleFIGURE")
    haut,bas,gauche,droite,case,ligne,colonne = app.get_functions()

    ## {{ [py]:dessin }}

    app.afficher_deplacement(etapes=True, num_lignes=False)




# --------- PYODIDE:env --------- #

@auto_run
def _alien():
    import p5
    from alien_python import App

    app = App("figureFIGURE")

    glob = globals()
    app.centrer(globals=glob)

    def verifier_programme():
        if app.ran_program:
            return
        app.verifier_programme('SOLUCE'.split())
        import alien_python
        alien_python.secret_tests()

    glob['verifier_programme'] = verifier_programme


# --------- PYODIDE:tests --------- #
verifier_programme()


# --------- PYODIDE:checks --------- #

def check_code(targets, msg, ok=True, count=None, with_def=True):
    assert all( (t in __USER_CODE__) == ok for t in targets), "\u274C "+ msg.strip()

    if count is not None:
        assert all( (__USER_CODE__.count(t)==count) == ok for t in targets), f"\u274C {msg.strip()} {count-with_def} fois"

def complete():
    check_code("...", "Le code ne devrait plus contenir de '...'", ok=False)

def conditions(*targets):
    check_code(targets, "On doit utiliser les structures conditionnelles")

def variables(*targets):
    check_code(targets, f"On doit utiliser les variables pour déplacer l'alien: " + ", ".join(targets))

def check_str(*vs):
    assert all(type(v)==str for v in vs), "\u274C Les variables doivent être des chaînes de caractères"

def col2(v):
    assert len(v) == 2, "\u274C Le numéro de colonne doit comporter deux chiffres"

def lines(less=None, more=None):
    lines = len(__USER_CODE__.split('# Tests')[0].strip().splitlines())

    if less is not None:
        assert lines <= less, f"Le code ne doit pas dépasser les { less } lignes !"
    if more is not None:
        assert lines >= more, f"Le code doit avoir au moins { more } lignes !"

def func(name, calls=None, with_def=True):
    if with_def:
        check_code([f"def {name}("], f"On doit créer la fonction {name}")
    if calls:
        msg = f"On doit { 'créer puis ' * with_def }appeler la fonction {name}"
        check_code([f"{name}("], msg, count=calls+with_def, with_def=with_def)

def indexing(name, *idxs):
    targets = [f"{ name }[{ i }]" for i in idxs]
    check_code(targets, "On doit utiliser les valeurs contenues dans le tableau là où demandé")

def taille(name, N):
    iterable = globals().get(name)
    assert iterable is not None, f"\u274C {name} n'est pas défini"
    assert len(iterable) == N, f"\u274C {name} devrait être de longueur {N}"

def valeurs(**kw):
    msg = "\u274C La variable n'a pas la bonne valeur" if len(kw)==1 else "\u274C Les variables n'ont pas les bonnes valeurs"
    assert all(globals().get(x) == v for x,v in kw.items()), msg