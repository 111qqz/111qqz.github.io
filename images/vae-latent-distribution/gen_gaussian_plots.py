# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate gaussian parameter visualization SVGs for the VAE blog post."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent


def gaussian_pdf(x, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def kl_divergence(mu_q, sigma_q, mu_p=0.0, sigma_p=1.0):
    return (
        np.log(sigma_p / sigma_q)
        + (sigma_q**2 + (mu_q - mu_p) ** 2) / (2 * sigma_p**2)
        - 0.5
    )


def plot_gaussian_params():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.8))
    x = np.linspace(-6, 6, 500)

    # Left: different mu, same sigma
    params_mu = [(-2, 1, "#2563eb"), (0, 1, "#16a34a"), (2, 1, "#dc2626")]
    for mu, sigma, color in params_mu:
        y = gaussian_pdf(x, mu, sigma)
        ax1.plot(x, y, color=color, linewidth=2.2, label=f"μ={mu}, σ²=1")
    ax1.set_title("μ 不同，σ² 相同", fontsize=13)
    ax1.set_xlabel("z", fontsize=11)
    ax1.set_ylabel("概率密度", fontsize=11)
    ax1.legend(fontsize=10)
    ax1.set_xlim(-5.5, 5.5)
    ax1.set_ylim(0, 0.5)

    # Right: same mu, different sigma
    params_sigma = [(0, 0.5, "#2563eb"), (0, 1.0, "#16a34a"), (0, 2.0, "#dc2626")]
    for mu, sigma, color in params_sigma:
        y = gaussian_pdf(x, mu, sigma)
        ax2.plot(x, y, color=color, linewidth=2.2, label=f"μ=0, σ={sigma}")
    ax2.set_title("μ 相同，σ 不同", fontsize=13)
    ax2.set_xlabel("z", fontsize=11)
    ax2.set_ylabel("概率密度", fontsize=11)
    ax2.legend(fontsize=10)
    ax2.set_xlim(-5.5, 5.5)
    ax2.set_ylim(0, 0.9)

    plt.tight_layout()
    out = OUT_DIR / "gaussian-params.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_kl_divergence():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.2))
    x = np.linspace(-5, 8, 500)
    p_y = gaussian_pdf(x, 0, 1)

    cases = [
        {"mu_q": 0, "sigma_q": 1.0, "title": "完全重合"},
        {"mu_q": 0.5, "sigma_q": 0.8, "title": "稍有偏移"},
        {"mu_q": 5, "sigma_q": 0.2, "title": "严重偏离"},
    ]

    for ax, case in zip(axes, cases):
        q_y = gaussian_pdf(x, case["mu_q"], case["sigma_q"])
        kl = kl_divergence(case["mu_q"], case["sigma_q"])

        ax.fill_between(x, p_y, alpha=0.15, color="#2563eb")
        ax.plot(x, p_y, color="#2563eb", linewidth=2.2, label="p(z) = N(0,1)")

        ax.fill_between(x, q_y, alpha=0.15, color="#dc2626")
        ax.plot(
            x,
            q_y,
            color="#dc2626",
            linewidth=2.2,
            label=f"q(z|x) = N({case['mu_q']},{case['sigma_q']:.1f}²)",
        )

        ax.set_title(f"{case['title']}  KL={kl:.2f}", fontsize=12)
        ax.set_xlabel("z", fontsize=10)
        ax.legend(fontsize=8, loc="upper right")
        ax.set_xlim(-4, 8)
        ax.set_ylim(0, max(p_y.max(), q_y.max()) * 1.15)

    plt.tight_layout()
    out = OUT_DIR / "kl-divergence-visual.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    plt.rcParams["font.family"] = ["DejaVu Sans", "WenQuanYi Micro Hei", "sans-serif"]
    plot_gaussian_params()
    plot_kl_divergence()
    print("Done.")
