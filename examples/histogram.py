import matplotlib.pyplot as plt
import numpy as np

import mpl_drip

rng = np.random.default_rng(seed=0)

plt.style.use("drip")


def plot_beta_hist(ax, a, b):
    ax.hist(
        rng.beta(a, b, size=10000),
        histtype="stepfilled",
        bins=25,
        alpha=0.85,
        density=True,
    )


fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title(r"mpl_drip histogram example")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$p(x)$")

plt.savefig("histogram.png", dpi=100, bbox_inches="tight")
plt.show()
