#!/usr/bin/env python3
"""Generate the A/B/C net-value chart for the risk-is-not-a-number post.

Run from anywhere: python3 nav-paths.py
Output: nav-paths.svg in the same directory as this script.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

PERIODS = list(range(6))
PATHS = [
    ("A（平稳）", [100.00, 101.50, 103.02, 104.57, 106.14, 107.73], "#2563eb", "o"),
    ("B（大起大落）", [100.00, 110.00, 104.50, 114.95, 97.71, 107.48], "#dc2626", "s"),
    ("C（平静后闪崩）", [100.00, 101.00, 102.01, 103.03, 104.06, 91.57], "#16a34a", "^"),
]

plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=150)

for label, values, color, marker in PATHS:
    ax.plot(
        PERIODS,
        values,
        label=label,
        color=color,
        marker=marker,
        linewidth=1.8,
        markersize=4.5,
    )

ax.axvspan(3, 4, color="#dc2626", alpha=0.07)
ax.annotate(
    "B 最大回撤 15%",
    xy=(3.5, 106.3),
    ha="center",
    va="center",
    fontsize=8.5,
    color="#dc2626",
)

ax.set_xlabel("期数（月）")
ax.set_ylabel("净值（期初 = 100）")
ax.set_xticks(PERIODS)
ax.set_ylim(88, 120)
ax.grid(True, linewidth=0.5, alpha=0.4)
ax.legend(frameon=False, loc="lower right")
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
fig.tight_layout()
fig.savefig(HERE / "nav-paths.svg", format="svg")
print(f"saved {HERE / 'nav-paths.svg'}")
