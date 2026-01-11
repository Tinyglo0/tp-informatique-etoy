
from dataclasses import dataclass, field
from functools import wraps
from pathlib import Path
from typing import ClassVar, Dict, List, Tuple


#---------------------------------------
# Various tokens used for string replacements (from macro output to
# on_page_content or on_page_context).
# Using empty spans so that the token doesn't show up in search results.

SEARCH_TAGS_CONTROLLER_TOKEN = "SEARCH_TAGS_CONTROLLER_TOKEN"
PARKOUR_MERMAID_REPL_TOKEN   = "PARKOUR_MERMAID_REPL_TOKEN"
    # No `span`/html here: it breaks because of the mermaid code block around
    # (didn't try to ding a solution to this)



#---------------------------------------
# Internal config/paths/constants/...:


SKIP_CHECKS_SERVE = False
"""
Set to True to bypass all the securities during a serve (to use to make a non dirty serve
while only a bunch of files aren't excluded).
"""

CAPYTALE_WITH_WIP = False
""" If True, the capytale_create page will show "en travaux" exercices. """

CAPYTALE_WITH_SQL = False
""" If True, the SQL tag is visible on Capytale """

CHECK_NO_WIP_LEGACY_IN_PARKOUR = False
""" Raise if True, log if False. """

LEGACY_CAPYTALE = "legacy_capytale"
"""
Tag à utiliser pour marquer les exercices validés dans leur version originale, lorsqu'on
souhaite en modifier un existant.
Les exercices avec ce tag n'apparaissent pas dans la page de recherche
"""

VALIDATED_DIR = "exercices"
""" Dossier contenant les exercices validés. """

REMARK_PATH = "remarques"
""" Chemin vers le dossier de remarques depuis la racine de la documentation """


# Various files to track during serve/build:
HOME_PAGE       = 'index.md'
PARKOUR_PAGE    = 'parcours.md'
RECHERCHE_PAGE  = 'recherche.md'
CAPYTALE_CREATE = 'capytale_create.md'


# Various directories or files (should always exist):
PATHS_TO_VALIDATE = (
    EXERCICES,
    TOOLS_IDS,
    CAP_PREPARE_SYNC
) = (
    Path("docs", VALIDATED_DIR),
    Path("tools","capytale_exos_ids.txt"),
    Path('overrides', 'javascripts', 'capytale0_PrepareSynch.js'),
)





 #---------------------------------------


@dataclass
class PageKind:
    """ Order of the properties must be compliant with TO_BUILD_ON_CTX """

    is_home: bool
    is_parcours: bool
    is_recherche: bool
    is_capytale_create: bool

    TO_BUILD_ON_CTX: ClassVar[Tuple] = (HOME_PAGE, PARKOUR_PAGE, RECHERCHE_PAGE, CAPYTALE_CREATE)

    @classmethod
    def build(cls, page_name):
        return cls(*(page_name==file for file in cls.TO_BUILD_ON_CTX))

    @classmethod
    def fresh_tracker(cls):
        return {file: False for file in cls.TO_BUILD_ON_CTX}



#---------------------------------------
# Default values and types:


ExByCategory = Dict[str, List["Exercice"]]
"""
Dict of category name -> list of Exercices
"""

GroupsPerPages = Dict[str, Dict[int, List[Tuple[str,str]]]]
"""
Dict of page_url -> group_index -> List of (ideId, pyName)
"""

DiffData = Tuple[str, str]
""" (category ID (ASCII + no spaces), category name (not ASCII + spaces)) """


# Must be defined _in order_:
DIFFICULTY_CATEGORIES: List[DiffData] = [
    ("debutant", "débutant"),
    ("facile", "facile"),
    ("moyen", "moyen"),
    ("difficile", "difficile"),
    ("non-renseigne", "non renseigné"),
]
OTHER_CATEGORIES = (
    "autre",
    "brouillon",
    "exam",
)

ALL_CATEGORIES  = OTHER_CATEGORIES + tuple(cat_id for cat_id, _ in DIFFICULTY_CATEGORIES)

DEFAULT_LICENSE = 'by-sa'

SKIPPED_TAGS_IN_TABLE = ("brouillon", LEGACY_CAPYTALE)


EXOS_MACROS = 'IDE', 'terminal', 'py_btn', "sqlide"
"""
Name of the macros defining an exercice.
"""

@dataclass
class Exercice:
    """Regrouping the data for a file/problem targeted by the search engine"""

    path: Path  # mandatory; absolute

    title: str = "Pas de titre :("
    stripped_title: str = "pasdetitre"
    difficulty: int = 400
    tags: List[str] = field(default_factory=list)
    is_exercise: bool = True  # "validé" ou "en travaux"
    is_validated: bool = False  # dans "./exercices/..."
    is_draft: bool = False  # "TROP en travaux"... XD
    is_legacy:bool = False # Ancien exo déjà validé, version gardée pour assurer la disponibilité de l'original dans Capytale
    is_exam: bool = False  # exam-type exercises, to be ignored in some occasion
    href: str = "" # Absolute url
    page_url: str = "" # Relative to the site_dir (used to identify an IDE against page.url)
    folder_name: str = "" # name of the directory holding the index.md file
    diff_category_data: DiffData = ("", "")
    index_file_last_update: str = "01/01/2024"  # Exercise's last update dd/mm/yyyyy
                                                # (default: before starting CodEx)

    @property
    def is_wip(self):
        return self.is_exercise and not self.is_validated





#-------------------------------------------------------------
# Dedicated codex logger

from pyodide_mkdocs_theme.pyodide_macros.pyodide_logger import get_plugin_logger

_hook = None

codex_log = get_plugin_logger('codex', color=33)


def log_func(func=None, custom=None):

    def dec(func):
        @wraps(func)
        def wrapper(*a, **kw):
            msg = [
                _hook or '',
                f"{ func.__name__ }(...)",
                (custom(a,kw) if custom else ""),
            ]
            codex_log.info(' '.join(msg).strip())
            return func(*a, **kw)
        return wrapper

    return dec(func) if func is not None else dec


def log_hook(func):
    @wraps(func)
    def wrapper(*a, **kw):
        global _hook
        _hook = f"[{ func.__name__ }] -"
        out = func(*a, **kw)
        _hook = None
        return out
    return wrapper



#-------------------------------------------------------------
# Decorator to bypass some verifications during serve

def skip_secu_if_needed(func):
    @wraps(func)
    def wrapper(*a,**kw):
        if not SKIP_CHECKS_SERVE:
            return func(*a,**kw)
    return wrapper
