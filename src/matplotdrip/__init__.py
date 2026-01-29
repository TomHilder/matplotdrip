from .colors import COLORS, get_color

__all__ = ["COLORS", "get_color"]

try:
    from ._version import __version__
except Exception:
    __version__ = "0+unknown"
