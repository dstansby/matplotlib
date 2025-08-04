"""
Core functions and attributes for the matplotlib style library:

``use``
    Select style sheet to override the current matplotlib settings.
``context``
    Context manager to use a style sheet temporarily.
``available``
    List available style sheets.
``library``
    A dictionary of style names and matplotlib settings.
"""

from . import USER_LIBRARY_PATHS, available, context, library, reload_library, use
from . import _BASE_LIBRARY_PATH as BASE_LIBRARY_PATH
from . import _STYLE_BLACKLIST as STYLE_BLACKLIST
from . import _STYLE_EXTENSION as STYLE_EXTENSION
from .. import _api

__all__ = [
    "use", "context", "available", "library", "reload_library",
    "USER_LIBRARY_PATHS", "BASE_LIBRARY_PATH", "STYLE_EXTENSION", "STYLE_BLACKLIST",
]

_api.warn_deprecated("3.11", name=__name__, obj_type="module")
