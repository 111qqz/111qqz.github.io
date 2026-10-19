# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate power-law curve SVG for the Scaling Laws blog post."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent


def power_law_curve():
    fig, ax = plt.subplots(figsize=(7, 4))

    N_observed = np.array([1, 4, 16])
    L_observed = 2 + 1 / np.sqrt(N_observed)

    N_predicted = np.array([64])
    L_predicted = 2 + 1 / np.sqrt(N_predicted)

    N_curve = np.linspace(0.5, 80, 300)
    L_curve = 2 + 1 / np.sqrt(N_curve)

    ax.plot(N_curve, L_curve, color="#6366f1", linewidth=2,
            label=r"$L(N) = 2 + 1/\sqrt{N}$")
    ax.scatter(N_observed, L_observed, color="#2563eb", s=80, zorder=5,
               label="Observed (trained)")
    ax.scatter(N_predicted, L_predicted, color="#dc2626", s=100, zorder=5,
               marker="D", label="64B (predicted)")
    ax.annotate("Predicted: 2.125", xy=(64, 2.125), xytext=(42, 2.35),
                fontsize=9, color="#dc2626",
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.2))

    for n, l in zip(N_observed, L_observed):
        ax.annotate(f"{n}B: {l:.2f}", xy=(n, l), xytext=(n + 3, l + 0.08),
                    fontsize=8, color="#2563eb")

    ax.axhline(y=2.0, color="#9ca3af", linestyle=":", linewidth=1, alpha=0.7)
    ax.text(70, 2.02, r"$L_\infty = 2$", fontsize=8, color="#9ca3af", ha="right")

    ax.set_xlabel("Parameters N (Billions)", fontsize=11)
    ax.set_ylabel("Loss", fontsize=11)
    ax.set_title("Illustrative data (not real fitted parameters)",
                 fontsize=10, color="#6b7280", style="italic")
    ax.legend(fontsize=9, loc="upper right")
    ax.set_xlim(0, 80)
    ax.set_ylim(1.9, 3.2)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "power-law-curve.svg", format="svg", transparent=False)
    plt.close(fig)
    print(f"Saved: {OUT_DIR / 'power-law-curve.svg'}")


if __name__ == "__main__":
    power_law_curve()
