# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate plot SVGs for the adversarial-attacks-fgsm blog post."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

OUT_DIR = Path(__file__).parent

plt.rcParams["font.family"] = ["DejaVu Sans", "sans-serif"]
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


def plot_decision_boundary():
    """2D decision boundary with two perturbation directions."""
    fig, ax = plt.subplots(figsize=(7, 5))

    bx = np.linspace(-2.5, 2.5, 300)
    by = 0.6 * bx + 0.2
    ax.plot(bx, by, color="#888888", linewidth=2, linestyle="--", zorder=2)

    xx = np.linspace(-2.5, 2.5, 200)
    yy = np.linspace(-2.5, 2.5, 200)
    X, Y = np.meshgrid(xx, yy)
    Z = Y - 0.6 * X - 0.2
    ax.contourf(X, Y, Z, levels=[-10, 0, 10],
                colors=["#dbeafe", "#fee2e2"], alpha=0.4, zorder=0)

    ax.text(-1.8, -2.0, "Class A", fontsize=13, color="#2563eb",
            fontweight="bold", alpha=0.7)
    ax.text(1.0, 2.0, "Class B", fontsize=13, color="#dc2626",
            fontweight="bold", alpha=0.7)
    ax.text(1.8, 1.55, "Decision\nBoundary", fontsize=9, color="#888888",
            rotation=31, ha="center", va="bottom")

    px, py = 0.8, 0.0
    ax.plot(px, py, "o", color="#1d4ed8", markersize=10, zorder=5)
    ax.annotate("x (original)", xy=(px, py), xytext=(px + 0.15, py - 0.35),
                fontsize=10, color="#1d4ed8", fontweight="bold")

    r = 1.0
    theta_rand = np.deg2rad(-10)
    dx_rand, dy_rand = r * np.cos(theta_rand), r * np.sin(theta_rand)
    ax.annotate("", xy=(px + dx_rand, py + dy_rand), xytext=(px, py),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.15",
                                color="#16a34a", lw=2.5))
    ax.text(px + dx_rand + 0.1, py + dy_rand - 0.25,
            "random perturbation\n(stays in Class A)", fontsize=9,
            color="#16a34a", fontweight="bold")

    normal = np.array([-0.6, 1.0])
    normal = normal / np.linalg.norm(normal)
    dx_adv, dy_adv = r * normal[0], r * normal[1]
    ax.annotate("", xy=(px + dx_adv, py + dy_adv), xytext=(px, py),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.15",
                                color="#dc2626", lw=2.5))
    ax.text(px + dx_adv - 1.3, py + dy_adv + 0.05,
            "adversarial perturbation\n(crosses to Class B)", fontsize=9,
            color="#dc2626", fontweight="bold")

    circle = plt.Circle((px, py), r, fill=False, linestyle=":",
                         color="#aaaaaa", linewidth=1, zorder=3)
    ax.add_patch(circle)

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(r"$x_1$", fontsize=12)
    ax.set_ylabel(r"$x_2$", fontsize=12)

    plt.tight_layout()
    out = OUT_DIR / "decision-boundary-perturbation.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_fgsm_comparison():
    """Bar chart comparing raw gradient scaling vs FGSM sign per component."""
    fig, ax = plt.subplots(figsize=(7, 4.5))

    components = [r"$x_1$", r"$x_2$", r"$x_3$"]
    grad = np.array([0.5, -2.0, 0.1])
    eps = 0.01

    raw_delta = np.abs(eps * grad)
    sign_delta = np.abs(eps * np.sign(grad))

    x_pos = np.arange(len(components))
    bar_w = 0.3

    bars_raw = ax.bar(x_pos - bar_w / 2, raw_delta, bar_w,
                      label=r"$\epsilon \cdot \nabla_x L$  (raw gradient)",
                      color="#f59e0b", alpha=0.85,
                      edgecolor="#d97706", linewidth=0.8)
    bars_sign = ax.bar(x_pos + bar_w / 2, sign_delta, bar_w,
                       label=r"$\epsilon \cdot \mathrm{sign}(\nabla_x L)$  (FGSM)",
                       color="#2563eb", alpha=0.85,
                       edgecolor="#1d4ed8", linewidth=0.8)

    ax.axhline(y=eps, color="#dc2626", linestyle="--", linewidth=1.5, alpha=0.8)
    ax.text(2.55, eps + 0.0005, r"$\epsilon = 0.01$", fontsize=10,
            color="#dc2626", fontweight="bold", va="bottom")

    for bar, val in zip(bars_raw, raw_delta):
        color = "#dc2626" if val > eps else "#d97706"
        suffix = "  (exceeds!)" if val > eps else ""
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0005,
                f"{val:.3f}{suffix}", ha="center", va="bottom", fontsize=8.5,
                fontweight="bold", color=color)
    for bar, val in zip(bars_sign, sign_delta):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0005,
                f"{val:.3f}", ha="center", va="bottom", fontsize=8.5,
                fontweight="bold", color="#1d4ed8")

    ax.set_xticks(x_pos)
    ax.set_xticklabels(components, fontsize=12)
    ax.set_ylabel(r"$|\delta_i|$  (perturbation magnitude)", fontsize=11)
    ax.set_ylim(0, 0.028)
    ax.legend(fontsize=9.5, loc="upper left", framealpha=0.9)

    ax.annotate(r"$\nabla_x L = [0.5, -2.0, 0.1]$,  $\epsilon = 0.01$",
                xy=(0.5, 0.95), xycoords="axes fraction",
                ha="center", va="top", fontsize=9, color="#666666",
                style="italic")

    plt.tight_layout()
    out = OUT_DIR / "fgsm-sign-vs-gradient.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_high_dim_accumulation():
    """Log-log plot: random noise vs directed perturbation scaling with dimension."""
    fig, ax = plt.subplots(figsize=(7.5, 4.5))

    dims = np.array([3, 10, 50, 100, 500, 1000, 10000, 150000])
    w_mag = 0.1
    eps = 0.01

    random_effect = eps * w_mag * np.sqrt(dims)
    directed_effect = eps * w_mag * dims

    ax.loglog(dims, random_effect, "o-", color="#f59e0b", linewidth=2.5,
              markersize=6, label=r"Random noise:  $O(\sqrt{n})$", zorder=4)
    ax.loglog(dims, directed_effect, "s-", color="#dc2626", linewidth=2.5,
              markersize=6, label=r"Directed perturbation:  $O(n)$", zorder=4)

    ax.fill_between(dims, random_effect, directed_effect,
                    alpha=0.08, color="#dc2626")

    ax.axvline(x=150000, color="#888888", linestyle=":", linewidth=1, alpha=0.5)
    ax.text(150000, ax.get_ylim()[0] * 3, "n = 150,000\n(typical image)",
            fontsize=8.5, color="#888888", ha="center", va="bottom")

    ax.set_xlabel("Input dimension  n", fontsize=12)
    ax.set_ylabel(r"$|\Delta f| = |w^T \delta|$", fontsize=12)
    ax.legend(fontsize=10, loc="upper left", framealpha=0.9)
    ax.grid(True, alpha=0.2, which="both")

    ax.annotate(
        r"$w_i = 0.1$,  $\epsilon = 0.01$"
        "\n(simplified linear model,\nequal weights for illustration)",
        xy=(0.97, 0.05), xycoords="axes fraction",
        ha="right", va="bottom", fontsize=8.5, color="#666666",
        style="italic",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="#cccccc", alpha=0.8))

    plt.tight_layout()
    out = OUT_DIR / "high-dim-accumulation.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    plot_decision_boundary()
    plot_fgsm_comparison()
    plot_high_dim_accumulation()
    print("Done.")
