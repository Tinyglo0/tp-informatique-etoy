
from mkdocs.structure.files import Files, File

from .config import log_func





@log_func
def open_mermaid_shadow_root_in_material_bundle_script(files:Files):
    """ !!!HACK-de-la-mort-qui-tue!!!
    Change material's mermaid shadowRoot rendering mode on the fly,
    to get access to the shadowRoot content from JS...
    """
    def is_material_bundle(file:File):
        return file.src_uri.startswith('assets/javascripts/bundle.') and file.src_uri.endswith('.min.js')

    bundle = next(filter(is_material_bundle, files))
    code   = bundle.content_string
    i      = code.find("attachShadow")
    j      = code.find("closed", i) + len("closed") + 1
    code   = f'{ code[:i] }attachShadow({ "{" }mode:"open"{ code[j:] }'
    bundle.content_string = code
    bundle.content_bytes  = bytes(code, encoding='utf-8')
