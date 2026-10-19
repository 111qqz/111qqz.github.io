# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate all SVG plots for the Emergent Abilities blog post."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent


def probability_vs_exact_match():
    """Fig 1: P(correct) smooth vs Exact Match jump for a single question."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=False)

    models = ["1B", "3B", "7B", "13B", "30B"]
    x = np.arange(len(models))
    p_correct = np.array([0.40, 0.45, 0.49, 0.51, 0.55])
    exact_match = np.array([0, 0, 0, 1, 1])

    ax1.plot(x, p_correct, "o-", color="#6366f1", linewidth=2, markersize=8)
    ax1.axhline(y=0.5, color="#9ca3af", linestyle=":", linewidth=1, alpha=0.7)
    ax1.text(4.3, 0.505, "50%", fontsize=8, color="#9ca3af")
    ax1.set_xticks(x)
    ax1.set_xticklabels(models)
    ax1.set_xlabel("Model Scale", fontsize=11)
    ax1.set_ylabel("P(correct answer)", fontsize=11)
    ax1.set_title("P(correct): smooth improvement", fontsize=10)
    ax1.set_ylim(0.3, 0.65)
    ax1.grid(True, alpha=0.3)

    colors = ["#dc2626" if v == 0 else "#16a34a" for v in exact_match]
    ax2.bar(x, exact_match, color=colors, width=0.5, edgecolor="none")
    ax2.set_xticks(x)
    ax2.set_xticklabels(models)
    ax2.set_xlabel("Model Scale", fontsize=11)
    ax2.set_ylabel("Exact Match (0 or 1)", fontsize=11)
    ax2.set_title("Exact Match: abrupt jump", fontsize=10)
    ax2.set_ylim(-0.05, 1.15)
    ax2.set_yticks([0, 1])
    ax2.set_yticklabels(["Wrong", "Correct"])
    ax2.grid(True, alpha=0.3, axis="y")

    fig.tight_layout(w_pad=3)
    fig.savefig(OUT_DIR / "probability-vs-exact-match.svg", format="svg", transparent=False)
    plt.close(fig)
    print(f"Saved: probability-vs-exact-match.svg")


def threshold_distribution():
    """Fig 2: Dispersed vs concentrated thresholds for 100 questions."""
    rng = np.random.default_rng(42)
    n_questions = 100
    model_sizes = np.linspace(1, 100, 200)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    thresholds_dispersed = rng.uniform(5, 95, size=n_questions)
    acc_dispersed = np.array([
        np.mean(model_sizes[i] >= thresholds_dispersed)
        for i in range(len(model_sizes))
    ])
    ax1.plot(model_sizes, acc_dispersed * 100, color="#6366f1", linewidth=2)
    ax1.set_xlabel("Model Scale (B params)", fontsize=11)
    ax1.set_ylabel("Accuracy (%)", fontsize=11)
    ax1.set_title("Thresholds dispersed (5B~95B)", fontsize=10)
    ax1.set_ylim(-5, 105)
    ax1.grid(True, alpha=0.3)

    thresholds_concentrated = rng.normal(loc=40, scale=5, size=n_questions)
    thresholds_concentrated = np.clip(thresholds_concentrated, 5, 95)
    acc_concentrated = np.array([
        np.mean(model_sizes[i] >= thresholds_concentrated)
        for i in range(len(model_sizes))
    ])
    ax2.plot(model_sizes, acc_concentrated * 100, color="#dc2626", linewidth=2)
    ax2.set_xlabel("Model Scale (B params)", fontsize=11)
    ax2.set_title("Thresholds concentrated (~40B)", fontsize=10)
    ax2.set_ylim(-5, 105)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout(w_pad=3)
    fig.savefig(OUT_DIR / "threshold-distribution.svg", format="svg", transparent=False)
    plt.close(fig)
    print(f"Saved: threshold-distribution.svg")


def multi_step_nonlinearity():
    """Fig 3: p vs p^10 showing nonlinear amplification."""
    fig, ax = plt.subplots(figsize=(6, 4))

    p = np.linspace(0.5, 1.0, 200)
    p10 = p ** 10

    ax.plot(p, p10 * 100, color="#6366f1", linewidth=2.5,
            label=r"$p^{10}$ (10 steps)")
    ax.plot(p, p * 100, color="#9ca3af", linewidth=1.5, linestyle="--",
            label=r"$p$ (single step)", alpha=0.7)

    key_points = [(0.6, 0.6**10), (0.7, 0.7**10), (0.8, 0.8**10),
                  (0.9, 0.9**10), (0.95, 0.95**10)]
    for px, py in key_points:
        ax.scatter([px], [py * 100], color="#dc2626", s=40, zorder=5)
        ax.annotate(f"p={px:.0%}: {py:.1%}",
                    xy=(px, py * 100),
                    xytext=(px - 0.08, py * 100 + 8),
                    fontsize=8, color="#dc2626",
                    arrowprops=dict(arrowstyle="->", color="#dc2626", lw=0.8))

    ax.set_xlabel("Per-step success rate p", fontsize=11)
    ax.set_ylabel("Overall success rate (%)", fontsize=11)
    ax.set_title("Multi-step task: small p improvement, large outcome change",
                 fontsize=10)
    ax.legend(fontsize=9, loc="upper left")
    ax.set_xlim(0.48, 1.02)
    ax.set_ylim(-5, 105)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_DIR / "multi-step-nonlinearity.svg", format="svg", transparent=False)
    plt.close(fig)
    print(f"Saved: multi-step-nonlinearity.svg")


if __name__ == "__main__":
    probability_vs_exact_match()
    threshold_distribution()
    multi_step_nonlinearity()
