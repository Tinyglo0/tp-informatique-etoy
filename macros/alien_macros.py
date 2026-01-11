from pyodide_mkdocs_theme.pyodide_macros import PyodideMacrosPlugin
from pathlib import Path
from .includer import renderer







def define_env(env:PyodideMacrosPlugin):

    _render_inner_macros = renderer(env)
    OP,CLO = '{{','}}'



    @env.macro
    def alien_dessin(num:int, num_question:int=None):
        """
        @num: numéro de l'exercice (fichier python, dans ./scripts/exo{num}.py).
        La section `PYODIDE:dessin` du fichier sert de source de vérité pour afficher le
        code à exécuter à droite de la grille. Elle sert également pour effectuer la vérification
        de la réponse de l'utilisateur.

        @num_question: si donné, permet de changer le numéro de la question dans l'admonition,
        si cela ne correspond pas avec le numéro de fichier.
        """
        content = f"""
??? question "Question { num if num_question is None else num_question } : Dessinez le parcours"

    {OP} composed_py('scripts/exo{ num }', sections='dessin', with_headers=False, attrs=".inline .end .w45") {CLO}
    {OP} run('scripts/exo{ num }') {CLO}
    {OP} figure("figure{ num }",
            inner_text = "L'image est en train de se charger",
            admo_title = "Dessinez le parcours") {CLO}
"""
        return _render_inner_macros(content)



    @env.macro
    def alien_IDE(
        num:int,
        *,
        num_question:int=None,
        header:str="",
        grille:bool=True,
        **kw,
    ):
        """
        Génère le fichier grille{num}.py automatiquement s'il n'existe pas.
        La section `PYODIDE:corr` du fichier python `./scripts/exo{num}.py` sert de source
        de vérité pour dessiner la figure au-dessus de l'IDE.

        @num: numéro de l'exercice (fichier python, dans ./scripts/exo{num}.py)

        @num_question: si donné, permet de changer le numéro de la question dans l'admonition,
        si cela ne correspond pas avec le numéro de fichier.

        @header: chaîne de caractères à insérer avec l'IDE (et l'éventuelle grille), au début
        de l'admonition.

        @grille: si True, le script initialisant l'image de solution à partir de la section corr
        est inséré avant l'IDE.

        **kw: tous les arguments nommés supplémentaires sont directement transmis à la macro IDE.
        """

        grill_file = "docs" / Path(*env.page.file.src_uri.split('/')).parent / 'scripts' / f"grille{num}.py"
        if grille and not grill_file.is_file():
            grill_file.touch()
            grill_file.write_text(f'''
# --------- PYODIDE:ignore --------- #
# Fichier généré automatiquement

# --------- PYODIDE:env --------- #
## {OP} [cwd]alien_python/.snippets:grille | FIGURE -> { num } {CLO}

# --------- PYODIDE:dessin --------- #
## {OP} exo{ num }:corr {CLO}
''', encoding='utf-8')

        unpacked = "".join( f', {k}={v!r}' for k,v in kw.items())
        grill = '' if not grille else f'''
    {OP} run('scripts/grille{ num }') {CLO}
    {OP} figure("grille{ num }",admo_title="Figure attendue") {CLO}
'''
        content = f"""
??? question "Question { num if num_question is None else num_question } : Codez le parcours"

    { header }

    { grill }

    {OP} IDE('scripts/exo{ num }'{ unpacked }) {CLO}
    {OP} figure("figure{ num }",
            inner_text = "Le parcours de votre code et la solution attendue s'afficheront ici",
            admo_title = "Tracé du parcours (le vôtre à gauche, la solution à droite)") {CLO}
"""
        return _render_inner_macros(content)
