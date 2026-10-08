#!/usr/bin/env python3
"""Generate discount factor curves (gamma^k) as SVG for the RL blog post."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

output_path = Path(__file__).parent / "discount-curves.svg"

steps = np.arange(0, 101)
gammas = [0.9, 0.99, 0.999]
colors = ["#e63946", "#2563eb", "#16a34a"]
labels = [r"$\gamma = 0.9$", r"$\gamma = 0.99$", r"$\gamma = 0.999$"]

fig, ax = plt.subplots(figsize=(8, 4))
fig.patch.set_alpha(0.0)
ax.set_facecolor("none")

for gamma, color, label in zip(gammas, colors, labels):
    weights = gamma ** steps
    ax.plot(steps, weights, color=color, linewidth=2.2, label=label)

ax.set_xlabel("Future step k", fontsize=13, color="#374151")
ax.set_ylabel(r"Weight $\gamma^k$", fontsize=13, color="#374151")
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=12, framealpha=0.0)
ax.tick_params(colors="#374151", labelsize=11)
for spine in ax.spines.values():
    spine.set_color("#94a3b8")

fig.tight_layout(pad=1.0)
fig.savefig(output_path, format="svg", transparent=True, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {output_path}")
