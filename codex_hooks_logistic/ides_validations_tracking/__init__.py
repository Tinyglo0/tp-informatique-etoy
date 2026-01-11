
import re
from pathlib import Path
from typing import Optional

from mkdocs.structure.pages import Page

from pyodide_mkdocs_theme.pyodide_macros import html_builder as Html
from pyodide_mkdocs_theme.pyodide_macros import PyodideMacrosPlugin
from pyodide_mkdocs_theme.pyodide_macros.macros.ide_manager import IdeManager



TRACKING_TOKEN = 'IDE_TRACKING_TOKEN'
TRACKING_TOKEN_TEMPLATE_URL = f'<span { TRACKING_TOKEN }="{"{}"}"></span>'



def get_validations_template_token(url:str):
    """
    Build the token that will allow to spot where to put the needed html to display information
    about the IDEs/content of each exercice (used for mermaid parkours and the search table).
    These tokens are replaced in the on_page_context event.
    """
    return TRACKING_TOKEN_TEMPLATE_URL.format(url)



def _get_ide_tracking_script_or_css(suffixe:str, file:str="ides_tracking"):
    path = Path(__file__).parent / (file + suffixe)
    return path.read_text(encoding='utf-8')



def add_js_css_and_ide_tracking_logistic(page:Page, env:PyodideMacrosPlugin, *, wraps_tag='span'):
    """
    Mutate page.content to insert the IDE tracking logistic (only called on the pages requiring
    this logistic during on_page_context hook. As of now: recherche.md and parcours.md).

    Proceed by replacing fake text content as `f"IDE_TRACKING_TOKEN!{ url }!IDE_TRACKING_TOKEN"`
    that has been dumped in the md at earlier stage in the build (through other macros).

    WARNING: this happens "in order", so the amount of data and their order has to exactly
    match the number of tokens.

    Also adds on the fly the css and js scripts/content needed for ides tracking stuff.
    """
    # pylint: disable=protected-access

    css = Html.style(_get_ide_tracking_script_or_css('.css'))

    # Add css specific to parcours.md if needed (at the beginning):
    if page.file.src_uri.endswith('parcours.md'):
        css = Html.style(_get_ide_tracking_script_or_css('.css', 'parcours')) + css

    # If for capytale_create.md, no tracking token in the html, so the following is a "no op":
    html = re.sub(
        TRACKING_TOKEN_TEMPLATE_URL.format('([^"]*?)'),
        lambda m: insert_validations(env, m[1], wraps_tag),
        page.content,
    )

    # Scripts are now inserted through jinja hook to allow real time debugging in the browser.
    #   See: macros_related_data:insert_grouped_ides_in_page_data

    page.content = f"{ css }\n\n{ html }"




def insert_validations(
    env: PyodideMacrosPlugin,
    url: str,
    wraps_tag: Optional[str]=None,
    **wraps_extras
):
    """
    Add the html holding as many IDEs' validation buttons as there are groups of IDEs referenced
    in the page with the given url.
    """
    from codex_hooks_logistic.macros_related_data import GROUPS_PER_PAGE
        # Avoiding circular imports shits... :rolleyes:

    if url not in GROUPS_PER_PAGE:
        return ""

    groups_dct = GROUPS_PER_PAGE[url]

    buttons = ''.join(
        IdeManager.cls_create_button(
            env, 'check',
            disabled = "",
            style = "display: var(--show-tracking);",      # Flag for the recherche.md page
            exo_url = url,
            pmt_group = i_key,
        )
        for i_key in groups_dct
    )

    if wraps_tag:
        buttons = getattr(Html, wraps_tag)(
            buttons, kls='ide_tracker_wrapper', **wraps_extras
        )
    return buttons

