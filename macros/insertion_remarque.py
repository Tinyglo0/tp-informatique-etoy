"""
##############################################
# Fichiers ajoutés pour Codex                #
# Insertion des remarques dans les exercices #
##############################################
"""

from pathlib import Path
import re
from functools import wraps
from textwrap import dedent
from typing import Optional

from pyodide_mkdocs_theme.pyodide_macros import PyodideMacrosPlugin

from codex_hooks_logistic.config import REMARK_PATH
from macros.includer import renderer




# Modèle
FORBIDDEN_TEMPLATE = """
???+ warning "{title}"

    Dans cet exercice on interdit d'utiliser {func_description} :
{funcs_list}
"""



def remarque(env: PyodideMacrosPlugin):
    """
    Insertion d'une remarque dans la documentation
    On passe en argument le nom du fichier markdown contenant la remarque sans l'extension

    Les fichiers de remarques sont tous dans `{docs_dir}/{REMARK_PATH}`
    """
    _render_inner_macros = renderer(env)

    @wraps(remarque)
    def wrapped(nom_fichier):
        src = Path(REMARK_PATH) / (f"{nom_fichier}.md")
        content = src.read_text(encoding='utf-8')
        md = _render_inner_macros(content, src, src)
        return md
        # return f'--8<-- "{REMARK_PATH}/{nom_fichier}.md"'

    return wrapped




def interdiction(env: PyodideMacrosPlugin):
    """
    Insertion d'une remarque précisant les fonctions interdites dans la documentation
    On passe en argument la chaîne contenant les noms des fonctions interdites

    Le paramètre "SANS" est une chaîne de caractères listant les fonctions à interdire
    séparées par des virgules (avec ou sans espaces médians)


    On construit le texte à partir de la chaîne FORBIDDEN_STRING
    Trois champs sont mis à jour :
    - le titre afin de tenir compte du pluriel
    - la description afin de tenir compte du pluriel
    - la liste des fonctions (dans le corps du texte si une seule fonction, dans une <ul>
      si plusieurs)
    """

    @wraps(interdiction)
    def wrapped(SANS: str, ID: Optional[int] = None):

        forbidden_funcs = re.split(r"[ ;,]+", SANS.strip(" ;,"))

        if len(forbidden_funcs) == 1:
            title = "Fonction, opérateur ou module interdit"
            func_description = "la fonction, l'opérateur ou le module"
        else:
            title = "Fonctions, opérateurs ou modules interdits"
            func_description = "les fonctions, les opérateurs ou les modules suivants"

        funcs = "\n".join([f"\n    * `#!py {func}`" for func in forbidden_funcs])

        md = FORBIDDEN_TEMPLATE.format(
            title = title,
            func_description = func_description,
            funcs_list = funcs,
        )
        indented_md = env.indent_macro(md)
        return indented_md

    return wrapped







def version_ep(env: PyodideMacrosPlugin):
    """
    ---------------------
    OBSOLETE (15/10/2025)
    ---------------------

    Insère une admonition indiquant si cet exercice est conçu pour être résolu dans sa
    version "vide" ou "à compléter" (ep1 ou ep2).

    Utilise les tags automatiquement pour savoir quel message intégrer.
    Usage:
        {{ version_ep() }}
    """

    @wraps(version_ep)
    def wrapped():

        if 'tags' not in env.page.meta:
            raise ValueError(f"No tags in the metadata of page {env.docs_dir_cwd_rel}/{env.page.file.src_uri}")

        tags = env.page.meta['tags']
        ep1, ep2 = (x in tags for x in ('ep1','ep2'))
        if not (ep1 ^ ep2):
            raise ValueError(f"Exactly one of 'ep1' or 'ep2' should be present in the metadata of page {env.docs_dir_cwd_rel}/{env.page.file.src_uri}")

        title = "Vide" if ep1 else "À compléter"

        admo = dedent(f"""
        ??? note "Exercice conseillé en version `{title}`"

            * Les exercices conseillés en version "Vide" sont conçus pour ressembler à un "exercice 1" des épreuves pratiques au baccalauréat de Terminale NSI.
            * Les exercices conseillés en version "À compléter" sont conçus pour ressembler à un "exercice 2" des épreuves pratiques au baccalauréat de Terminale NSI.

            La difficulté de l'exercice a été choisie en partant du principe qu'il est fait dans la version indiquée.
        """)

        admo = dedent(admo)
        indent = env.get_macro_indent()
        if indent:
            admo = admo.replace('\n', '\n'+indent)

        # print(admo)
        return admo

    return wrapped
