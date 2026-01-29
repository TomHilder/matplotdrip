import shutil
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style

# Check if LaTeX is available
LATEX_AVAILABLE = shutil.which("latex") is not None

# Register the style as "drip" in matplotlib's style library
_style_file = Path(__file__).parent / "custom.mplstyle"
_style_params = mpl.rc_params_from_file(_style_file, use_default_template=False)

# If LaTeX is not available, disable it and use mathtext instead
if not LATEX_AVAILABLE:
    _style_params["text.usetex"] = False
    _style_params["text.latex.preamble"] = ""
    _style_params["mathtext.fontset"] = "cm"  # Computer Modern for math

style.library["drip"] = _style_params
style.available[:] = sorted(style.library.keys())

# Load the style temporarily to extract the color cycle
with plt.style.context("drip"):
    _prop_cycle = plt.rcParams["axes.prop_cycle"]
    COLORS = _prop_cycle.by_key().get("color", [])


# Make colors accessible by name
def get_color(index: int):
    """Returns a color from the style's color cycle by index."""
    return COLORS[index % len(COLORS)]  # Wrap around if index is too large
