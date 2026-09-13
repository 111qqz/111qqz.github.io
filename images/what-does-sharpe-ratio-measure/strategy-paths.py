#!/usr/bin/env python3
"""Generate the A/B/C net-value chart for the what-does-sharpe-ratio-measure post.

A and B are calibrated to annualized excess return / volatility of 10%/5% and
15%/15%: monthly mean = annual / 12, monthly population sigma = annual / sqrt(12).
C is the 11 x +0.5% then -20% monthly series used in the post.

Run from anywhere: python3 strategy-paths.py
Output: strategy-paths.svg in the same directory as this script.
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

MONTHS = 12


def cosine_series(annual_mean_pct: float, annual_sigma_pct: float) -> tuple[list[float], list[float]]:
    mu = annual_mean_pct / 100 / MONTHS
    sigma = annual_sigma_pct / 100 / math.sqrt(MONTHS)
    amplitude = sigma * math.sqrt(2)
    returns = [mu + amplitude * math.cos(2 * math.pi * k / MONTHS) for k in range(MONTHS)]
    nav = [100.0]
    for r in returns:
        nav.append(nav[-1] * (1 + r))
    return returns, nav


def main() -> None:
    returns_a, nav_a = cosine_series(10, 5)
    returns_b, nav_b = cosine_series(15, 15)
    returns_c = [0.005] * 11 + [-0.20]
    nav_c = [100.0]
    for r in returns_c:
        nav_c.append(nav_c[-1] * (1 + r))

    periods = list(range(MONTHS + 1))

    plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=150)

    ax.plot(
        periods,
        nav_a,
        label="A：年化超额 10%，波动 5%",
        color="#2563eb",
        marker="o",
        linewidth=1.8,
        markersize=4.0,
    )
    ax.plot(
        periods,
        nav_b,
        label="B：年化超额 15%，波动 15%",
        color="#dc2626",
        marker="s",
        linewidth=1.8,
        markersize=4.0,
    )
    ax.plot(
        periods,
        nav_c,
        label="C：11 个月 +0.5%，最后一个月 -20%",
        color="#16a34a",
        marker="^",
        linewidth=1.8,
        markersize=4.0,
    )

    ax.axvspan(11, 12, color="#16a34a", alpha=0.08)
    ax.annotate(
        "C 最后一个月 -20%",
        xy=(12, nav_c[-1]),
        xytext=(9.6, 88.0),
        fontsize=8.5,
        color="#16a34a",
        arrowprops=dict(arrowstyle="->", color="#16a34a", linewidth=0.9),
    )

    ax.set_xlabel("期数（月）")
    ax.set_ylabel("净值（期初 = 100）")
    ax.set_xticks(periods)
    ax.set_ylim(80, 122)
    ax.grid(True, linewidth=0.5, alpha=0.4)
    ax.legend(frameon=False, loc="lower left", fontsize=8.5)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    fig.tight_layout()
    fig.savefig(HERE / "strategy-paths.svg", format="svg")
    print(f"saved {HERE / 'strategy-paths.svg'}")

    for name, returns, nav in (("A", returns_a, nav_a), ("B", returns_b, nav_b), ("C", returns_c, nav_c)):
        mean = sum(returns) / len(returns)
        pop_sigma = math.sqrt(sum((r - mean) ** 2 for r in returns) / len(returns))
        print(
            f"{name}: final={nav[-1]:.2f} monthly_mean={mean * 100:.4f}% "
            f"annualized_mean={mean * 12 * 100:.4f}% pop_sigma_ann={pop_sigma * math.sqrt(12) * 100:.4f}%"
        )


if __name__ == "__main__":
    main()
