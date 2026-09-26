"""Generate mathematical curve plots for the Bernoulli-to-BCE blog post.

Produces two SVG files:
  - log-likelihood-curve.svg: L(p) and log L(p) for n=10, k=7
  - bce-loss-curves.svg: -log(p) and -log(1-p)

Both support light/dark mode via embedded CSS media queries.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent

LIGHT_TEXT = "#1a1a2e"
LIGHT_GRID = "#d0d0d0"
LIGHT_BG = "#ffffff"
DARK_TEXT = "#cdd6f4"
DARK_GRID = "#45475a"
DARK_BG = "#1e1e2e"


def _add_dark_mode_css(svg_path: Path) -> None:
    """Inject CSS media query for dark mode into an SVG file."""
    content = svg_path.read_text()
    css = """
<style>
@media (prefers-color-scheme: dark) {
  .figure { fill: """ + DARK_BG + """ !important; }
  text { fill: """ + DARK_TEXT + """ !important; }
  .axes-bg { fill: """ + DARK_BG + """ !important; }
}
</style>"""
    content = content.replace("<defs>", css + "\n<defs>", 1)
    svg_path.write_text(content)


def plot_log_likelihood():
    """Plot L(p) and log L(p) for n=10, k=7."""
    p = np.linspace(0.001, 0.999, 500)
    k, n = 7, 10
    L = p**k * (1 - p)**(n - k)
    logL = k * np.log(p) + (n - k) * np.log(1 - p)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
    fig.patch.set_facecolor(LIGHT_BG)

    # Left: L(p)
    ax1.plot(p, L, color="#2563eb", linewidth=2.2)
    ax1.axvline(x=0.7, color="#dc2626", linestyle="--", linewidth=1.5, alpha=0.8)
    peak_L = 0.7**7 * 0.3**3
    ax1.plot(0.7, peak_L, "o", color="#dc2626", markersize=8, zorder=5)
    ax1.annotate(f"p = 0.7\nL = {peak_L:.4f}",
                 xy=(0.7, peak_L), xytext=(0.78, peak_L * 0.8),
                 fontsize=10, color="#dc2626",
                 arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.2))
    ax1.set_xlabel("p", fontsize=12, color=LIGHT_TEXT)
    ax1.set_ylabel("L(p)", fontsize=12, color=LIGHT_TEXT)
    ax1.set_title("Likelihood   L(p) = p⁷(1-p)³", fontsize=12, color=LIGHT_TEXT)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(bottom=0)
    ax1.grid(True, alpha=0.3, color=LIGHT_GRID)
    ax1.tick_params(colors=LIGHT_TEXT)
    ax1.set_facecolor(LIGHT_BG)

    # Right: log L(p)
    ax2.plot(p, logL, color="#16a34a", linewidth=2.2)
    ax2.axvline(x=0.7, color="#dc2626", linestyle="--", linewidth=1.5, alpha=0.8)
    peak_logL = 7 * np.log(0.7) + 3 * np.log(0.3)
    ax2.plot(0.7, peak_logL, "o", color="#dc2626", markersize=8, zorder=5)
    ax2.annotate(f"p = 0.7\nl = {peak_logL:.2f}",
                 xy=(0.7, peak_logL), xytext=(0.78, peak_logL - 1.5),
                 fontsize=10, color="#dc2626",
                 arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.2))
    ax2.set_xlabel("p", fontsize=12, color=LIGHT_TEXT)
    ax2.set_ylabel("l(p) = log L(p)", fontsize=12, color=LIGHT_TEXT)
    ax2.set_title("Log-Likelihood   l(p) = 7 log p + 3 log(1-p)",
                  fontsize=12, color=LIGHT_TEXT)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(-25, 0)
    ax2.grid(True, alpha=0.3, color=LIGHT_GRID)
    ax2.tick_params(colors=LIGHT_TEXT)
    ax2.set_facecolor(LIGHT_BG)

    fig.tight_layout(pad=2.0)
    out = OUTPUT_DIR / "log-likelihood-curve.svg"
    fig.savefig(out, format="svg", bbox_inches="tight",
                facecolor=LIGHT_BG, edgecolor="none")
    plt.close(fig)
    _add_dark_mode_css(out)
    print(f"Saved {out}")


def plot_bce_loss():
    """Plot -log(p) and -log(1-p) on the same axes."""
    p = np.linspace(0.005, 0.995, 500)
    loss_y1 = -np.log(p)
    loss_y0 = -np.log(1 - p)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    fig.patch.set_facecolor(LIGHT_BG)

    ax.plot(p, loss_y1, color="#2563eb", linewidth=2.2,
            label="y=1:  -log(p)")
    ax.plot(p, loss_y0, color="#dc2626", linewidth=2.2,
            label="y=0:  -log(1-p)")

    # Annotate key points
    ax.plot(0.8, -np.log(0.8), "o", color="#2563eb", markersize=7, zorder=5)
    ax.annotate(f"p=0.8\nloss={-np.log(0.8):.3f}",
                xy=(0.8, -np.log(0.8)), xytext=(0.60, 1.2),
                fontsize=9, color="#2563eb",
                arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.0))

    ax.plot(0.8, -np.log(0.2), "o", color="#dc2626", markersize=7, zorder=5)
    ax.annotate(f"p=0.8\nloss={-np.log(0.2):.3f}",
                xy=(0.8, -np.log(0.2)), xytext=(0.60, 2.5),
                fontsize=9, color="#dc2626",
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.0))

    ax.set_xlabel("p", fontsize=12, color=LIGHT_TEXT)
    ax.set_ylabel("BCE Loss", fontsize=12, color=LIGHT_TEXT)
    ax.set_title("Binary Cross Entropy Loss", fontsize=12, color=LIGHT_TEXT)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5)
    ax.legend(fontsize=10, loc="upper center", framealpha=0.9)
    ax.grid(True, alpha=0.3, color=LIGHT_GRID)
    ax.tick_params(colors=LIGHT_TEXT)
    ax.set_facecolor(LIGHT_BG)

    fig.tight_layout()
    out = OUTPUT_DIR / "bce-loss-curves.svg"
    fig.savefig(out, format="svg", bbox_inches="tight",
                facecolor=LIGHT_BG, edgecolor="none")
    plt.close(fig)
    _add_dark_mode_css(out)
    print(f"Saved {out}")


if __name__ == "__main__":
    plot_log_likelihood()
    plot_bce_loss()
