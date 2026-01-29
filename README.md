# mpl_drip

<div align="center">
<img src="https://raw.githubusercontent.com/TomHilder/mpl_drip/main/examples/histogram.png" alt="histogram" width="500"></img>
</div>

Installable matplotlib style sheet, a color cycle, and some nice colormaps.

I use these settings because I think they make plots that are "good", but also (as the kids would say) "dripped up".

## Installation

Easiest is from PyPI either with `pip`

```sh
pip install mpl-drip
```

or `uv` (recommended)

```sh
uv add mpl-drip
```

Or, you can clone and build from source

```sh
git clone git@github.com:TomHilder/mpl_drip.git
cd mpl_drip
pip install -e .
```

where in the last step we made an editable install with pip but you can do whatever you like.

## Usage

To use the plotting style:

```python
import mpl_drip  # Registers the style with matplotlib

plt.style.use("drip")
```

To get a colour from the cycle by index, wrapping around if the index exceeds the number of colours:

```python
from mpl_drip import get_color
c = get_color(N) # N is any positive integer
```

To access the custom colormaps:

```python
from mpl_drip import colormaps
# Then simply use `red_white_blue` or `red_white_blue_r` in place of any mpl cmap
plt.imshow(..., cmap="red_white_blue_r")
```

## Credit

The colour cycle is from [manim](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html), and the `red_white_blue` colourmap is from [this repo](https://github.com/c-white/colormaps).
