# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate plot SVGs for the rethinking-generalization blog post."""

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


def plot_complexity_error_curve():
    fig, ax = plt.subplots(figsize=(8, 4.5))

    x = np.linspace(0.5, 5.5, 300)

    train_err = 0.65 * np.exp(-0.7 * x) + 0.02
    test_err = 0.55 * np.exp(-1.0 * x) + 0.06 * (x - 1.0) ** 2 + 0.05

    ax.plot(x, train_err, color="#2563eb", linewidth=2.5, label="Training Error")
    ax.plot(x, test_err, color="#dc2626", linewidth=2.5, label="Test Error")

    best_idx = np.argmin(test_err)
    best_x = x[best_idx]

    ax.axvline(x=best_x, color="#888888", linestyle="--", linewidth=1, alpha=0.6)

    ax.annotate("Underfitting", xy=(1.0, 0.48), fontsize=11, color="#666666",
                ha="center", style="italic")
    ax.annotate("Good Fit", xy=(best_x, 0.48), fontsize=11, color="#16a34a",
                ha="center", style="italic", fontweight="bold")
    ax.annotate("Overfitting", xy=(4.8, 0.48), fontsize=11, color="#666666",
                ha="center", style="italic")

    ax.set_xlabel("Model Complexity", fontsize=12)
    ax.set_ylabel("Error", fontsize=12)
    ax.legend(fontsize=11, loc="upper right", framealpha=0.9)
    ax.set_xlim(0.3, 5.7)
    ax.set_ylim(-0.02, 0.55)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    out = OUT_DIR / "complexity-error-curve.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_true_vs_random_results():
    fig, ax = plt.subplots(figsize=(7, 4.5))

    labels = ["True Labels", "Random Labels"]
    train_acc = [100.0, 100.0]
    test_acc = [85.75, 9.78]

    x_pos = np.array([0, 1.2])
    bar_w = 0.3

    bars_train = ax.bar(x_pos - bar_w / 2, train_acc, bar_w,
                        label="Train Accuracy", color="#2563eb", alpha=0.85,
                        edgecolor="#1d4ed8", linewidth=0.8)
    bars_test = ax.bar(x_pos + bar_w / 2, test_acc, bar_w,
                       label="Test Accuracy", color="#dc2626", alpha=0.85,
                       edgecolor="#b91c1c", linewidth=0.8)

    for bar, val in zip(bars_train, train_acc):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f"{val:.0f}%", ha="center", va="bottom", fontsize=11,
                fontweight="bold", color="#1d4ed8")
    for bar, val in zip(bars_test, test_acc):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f"{val:.2f}%", ha="center", va="bottom", fontsize=11,
                fontweight="bold", color="#b91c1c")

    ax.set_xticks(x_pos)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel("Accuracy (%)", fontsize=12)
    ax.set_ylim(0, 115)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(fontsize=10, loc="upper right", framealpha=0.9)

    ax.annotate("Inception on CIFAR-10\n(no augmentation, no weight decay)",
                xy=(0.5, 0.95), xycoords="axes fraction",
                ha="center", va="top", fontsize=9, color="#666666",
                style="italic")

    plt.tight_layout()
    out = OUT_DIR / "true-vs-random-results.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    plot_complexity_error_curve()
    plot_true_vs_random_results()
    print("Done.")
