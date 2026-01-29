# matplotdrip

<div align="center">
<img src="https://raw.githubusercontent.com/TomHilder/matplotdrip/main/examples/histogram.png" alt="histogram" width="500"></img>
</div>

Installable matplotlib style sheet, a color cycle, and some nice colormaps.

I use these settings because I think they make plots that are "good", but also (as the kids would say) "dripped up".

## Installation

Easiest is from PyPI either with `pip`

```sh
pip install matplotdrip
```

or `uv` (recommended)

```sh
uv add matplotdrip
```

Or, you can clone and build from source

```sh
git clone git@github.com:TomHilder/matplotdrip.git
cd matplotdrip
pip install -e .
```

where in the last step we made an editable install with pip but you can do whatever you like.

## Usage

To use the plotting style:

```python
import matplotdrip  # Registers the style with matplotlib

plt.style.use("drip")
```

To get a colour from the cycle by index, wrapping around if the index exceeds the number of colours:

```python
from matplotdrip import get_color
c = get_color(N) # N is any positive integer
```

To access the custom colormaps:

```python
from matplotdrip import colormaps
# Then simply use `red_white_blue` or `red_white_blue_r` in place of any mpl cmap
plt.imshow(..., cmap="red_white_blue_r")
```

## LaTeX

For the best-looking plots, install LaTeX on your system. The style will automatically use LaTeX for text rendering when available, giving you proper Computer Modern fonts and math typesetting.

If LaTeX is not installed, the style falls back to matplotlib's built-in mathtext renderer with Computer Modern fonts - still looks good, just not quite as crisp.

**Installing LaTeX:**

- **macOS:** `brew install --cask mactex` or install [BasicTeX](https://www.tug.org/mactex/morepackages.html) for a smaller footprint
- **Ubuntu/Debian:** `sudo apt install texlive-latex-extra texlive-fonts-recommended dvipng cm-super`
- **Windows:** Install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

## Credit

The colour cycle is from [manim](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html), and the `red_white_blue` colourmap is from [this repo](https://github.com/c-white/colormaps).
