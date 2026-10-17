# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "matplotlib",
#   "numpy",
# ]
# ///
"""Generate plot SVGs for the distribution shift and extrapolation post."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent

# Configure fonts and clean style
plt.rcParams["font.sans-serif"] = ["Noto Sans CJK SC", "DejaVu Sans", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


def plot_day_night_covariate_shift():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw={"width_ratios": [1.4, 1.0]})

    scenarios = ["测试环境\n(离线评估)", "生产环境\n(线上实测)"]
    day_ratio = np.array([90.0, 30.0])
    night_ratio = np.array([10.0, 70.0])

    x_pos = np.arange(len(scenarios))
    bar_w = 0.45

    # Stacked bar plot for input ratio
    b_day = ax1.bar(x_pos, day_ratio, bar_w, label="白天样本 (准确率 99%)",
                    color="#2563eb", alpha=0.85, edgecolor="#1d4ed8", linewidth=1.2)
    b_night = ax1.bar(x_pos, night_ratio, bar_w, bottom=day_ratio, label="夜间样本 (准确率 89%)",
                      color="#64748b", alpha=0.85, edgecolor="#475569", linewidth=1.2)

    for i in range(len(scenarios)):
        ax1.text(x_pos[i], day_ratio[i] / 2, f"白天\n{day_ratio[i]:.0f}%",
                 ha="center", va="center", color="white", fontweight="bold", fontsize=11)
        ax1.text(x_pos[i], day_ratio[i] + night_ratio[i] / 2, f"夜间\n{night_ratio[i]:.0f}%",
                 ha="center", va="center", color="white", fontweight="bold", fontsize=11)

    ax1.set_ylabel("输入样本比例 (%)", fontsize=11)
    ax1.set_ylim(0, 115)
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(scenarios, fontsize=11)
    ax1.legend(loc="upper right", framealpha=0.9, fontsize=9.5)
    ax1.set_title("输入组成比例变化 (Covariate Shift)", fontsize=12, pad=10, fontweight="bold")

    # Bar plot for overall accuracy comparison
    overall_acc = [98.0, 92.0]
    b_acc = ax2.bar(x_pos, overall_acc, bar_w, color=["#16a34a", "#dc2626"], alpha=0.85,
                    edgecolor=["#15803d", "#b91c1c"], linewidth=1.2)

    for bar, acc in zip(b_acc, overall_acc):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                 f"{acc:.1f}%", ha="center", va="bottom", fontsize=12, fontweight="bold",
                 color="#15803d" if acc > 95 else "#b91c1c")

    ax2.annotate("模型未变、单场景能力未变\n整体准确率下滑 6.0%",
                 xy=(1, 92), xytext=(0.5, 78),
                 arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.5),
                 ha="center", fontsize=10, color="#dc2626", fontweight="bold")

    ax2.set_ylabel("模型整体准确率 (%)", fontsize=11)
    ax2.set_ylim(60, 108)
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(scenarios, fontsize=11)
    ax2.set_title("整体性能变化", fontsize=12, pad=10, fontweight="bold")

    plt.tight_layout()
    out = OUT_DIR / "day-night-covariate-shift.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_concept_drift_prob_curve():
    fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(8.5, 5.2), sharex=True,
                                         gridspec_kw={"height_ratios": [2.2, 1.2]})

    x = np.linspace(-4, 4, 400)

    # Concept Drift: P(Y=1|X) shifts
    # Historical relation
    p_test = 1 / (1 + np.exp(-1.8 * (x - 0.2)))
    # Production relation (decayed probability for positive outcome given same feature)
    p_prod = 1 / (1 + np.exp(-1.8 * (x - 2.0)))

    ax_top.plot(x, p_test, color="#2563eb", linewidth=2.5, label=r"测试环境条件概率 $P_{\mathrm{test}}(Y=1|X)$")
    ax_top.plot(x, p_prod, color="#dc2626", linewidth=2.5, linestyle="--", label=r"生产环境条件概率 $P_{\mathrm{prod}}(Y=1|X)$")

    ax_top.set_ylabel(r"$P(Y=1 \mid X)$", fontsize=11)
    ax_top.set_ylim(-0.05, 1.1)
    ax_top.legend(loc="upper left", framealpha=0.9, fontsize=10)
    ax_top.grid(True, linestyle=":", alpha=0.5)
    ax_top.set_title("Concept Drift：输入分布不变，预测规律发生变迁", fontsize=12, pad=10, fontweight="bold")

    # Mark divergence at x = 1.0
    x_val = 1.0
    y_test_val = 1 / (1 + np.exp(-1.8 * (x_val - 0.2)))
    y_prod_val = 1 / (1 + np.exp(-1.8 * (x_val - 2.0)))
    ax_top.scatter([x_val, x_val], [y_test_val, y_prod_val], color=["#2563eb", "#dc2626"], s=50, zorder=5)
    ax_top.plot([x_val, x_val], [y_prod_val, y_test_val], color="#888888", linestyle=":", lw=1.5)
    ax_top.text(x_val + 0.15, (y_test_val + y_prod_val) / 2,
                f"同一输入 X={x_val:.1f}\n正例概率从 {y_test_val:.2f} 降至 {y_prod_val:.2f}",
                fontsize=9.5, color="#333333", va="center")

    # Marginal distribution P(X) unchanged
    p_x = (1 / (np.sqrt(2 * np.pi) * 1.2)) * np.exp(-0.5 * (x / 1.2) ** 2)
    ax_bot.plot(x, p_x, color="#16a34a", linewidth=2.0, label=r"输入特征分布 $P_{\mathrm{test}}(X) = P_{\mathrm{prod}}(X)$ (完全一致)")
    ax_bot.fill_between(x, p_x, alpha=0.15, color="#16a34a")
    ax_bot.set_xlabel("输入特征 X", fontsize=11)
    ax_bot.set_ylabel(r"$P(X)$", fontsize=11)
    ax_bot.set_ylim(0, 0.4)
    ax_bot.legend(loc="upper left", framealpha=0.9, fontsize=10)
    ax_bot.grid(True, linestyle=":", alpha=0.5)

    plt.tight_layout()
    out = OUT_DIR / "concept-drift-prob-curve.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_extrapolation_bifurcation():
    fig, ax = plt.subplots(figsize=(8.8, 4.8))

    # Points in training region [1, 5]
    train_x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    train_y = np.array([2.0, 4.0, 6.0, 8.0, 10.0])

    x_interp = np.linspace(0.8, 5.0, 100)
    x_extrap = np.linspace(5.0, 20.0, 200)

    # f_A(x) = 2x
    y_A_interp = 2.0 * x_interp
    y_A_extrap = 2.0 * x_extrap

    # f_B(x) = 2x for x<=5, 2x + (x-5)^2 for x>5
    y_B_interp = 2.0 * x_interp
    y_B_extrap = 2.0 * x_extrap + (x_extrap - 5.0) ** 2

    # Shaded regions
    ax.axvspan(0.5, 5.0, color="#dcfce7", alpha=0.5, label="插值区域 (训练样本充分覆盖)")
    ax.axvspan(5.0, 21.0, color="#fee2e2", alpha=0.35, label="外推区域 (缺乏样本约束)")

    # Plot curves
    ax.plot(np.concatenate([x_interp, x_extrap]),
            np.concatenate([y_A_interp, y_A_extrap]),
            color="#2563eb", linewidth=2.5, label=r"候选模型 A: $f_A(x) = 2x$")
    ax.plot(x_extrap, y_B_extrap,
            color="#dc2626", linewidth=2.5, linestyle="--", label=r"候选模型 B: $f_B(x) = 2x + (x-5)^2$")

    # Plot training points
    ax.scatter(train_x, train_y, color="#16a34a", s=65, zorder=6, edgecolors="#15803d",
               linewidths=1.5, label="训练样本点 (x=1..5, y=2..10)")

    # Mark x = 20 bifurcation
    ax.scatter([20.0, 20.0], [40.0, 265.0], color=["#2563eb", "#dc2626"], s=55, zorder=6)
    ax.plot([20.0, 20.0], [40.0, 265.0], color="#888888", linestyle=":", lw=1.5)
    ax.annotate(r"$f_A(20) = 40$", xy=(20, 40), xytext=(17.5, 20),
                fontsize=10, fontweight="bold", color="#2563eb")
    ax.annotate(r"$f_B(20) = 265$", xy=(20, 265), xytext=(16.8, 255),
                fontsize=10, fontweight="bold", color="#dc2626")

    # Mark x = 2.5 interpolation
    ax.scatter([2.5], [5.0], color="#16a34a", s=45, zorder=6)
    ax.annotate("插值预测 x=2.5\nf_A = f_B = 5", xy=(2.5, 5), xytext=(2.8, 30),
                arrowprops=dict(arrowstyle="->", color="#16a34a", lw=1.2),
                fontsize=9.5, color="#15803d", fontweight="bold")

    ax.set_xlabel("输入变量 x", fontsize=11)
    ax.set_ylabel("输出变量 f(x)", fontsize=11)
    ax.set_xlim(0.5, 21.0)
    ax.set_ylim(-10, 290)
    ax.legend(loc="upper left", framealpha=0.9, fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.set_title("训练区域内等效，外推区域解剧烈分叉", fontsize=12, pad=10, fontweight="bold")

    plt.tight_layout()
    out = OUT_DIR / "extrapolation-bifurcation.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


def plot_high_dimensional_coverage_void():
    fig, ax = plt.subplots(figsize=(7.5, 6.0))

    np.random.seed(42)
    # Generate training points along diagonal with small noise
    t = np.random.uniform(0.05, 0.95, 120)
    noise = np.random.normal(0, 0.04, 120)
    x1 = t + noise
    x2 = t - noise

    # Clip to [0, 1]
    x1 = np.clip(x1, 0.02, 0.98)
    x2 = np.clip(x2, 0.02, 0.98)

    # Plot training points
    ax.scatter(x1, x2, color="#2563eb", alpha=0.6, s=35, label="训练样本 (集中于主对角线)", edgecolors="none")

    # New point (0.9, 0.1)
    novel_x1, novel_x2 = 0.9, 0.1
    ax.scatter([novel_x1], [novel_x2], color="#dc2626", s=100, zorder=7,
               edgecolors="#7f1d1d", linewidths=2.0, label="新样本 (0.9, 0.1)")

    # Projections to axes
    ax.plot([novel_x1, novel_x1], [0, novel_x2], color="#dc2626", linestyle="--", lw=1.5, alpha=0.8)
    ax.plot([0, novel_x1], [novel_x2, novel_x2], color="#dc2626", linestyle="--", lw=1.5, alpha=0.8)

    # Highlight 1D range on axes
    ax.plot([0, 1], [-0.02, -0.02], color="#16a34a", lw=4.0, clip_on=False)
    ax.plot([-0.02, -0.02], [0, 1], color="#16a34a", lw=4.0, clip_on=False)

    ax.text(0.5, -0.07, "X1 历史取值区间 [0, 1] (0.9 处于正常范围)",
            ha="center", fontsize=9.5, color="#15803d", fontweight="bold")
    ax.text(-0.06, 0.5, "X2 历史取值区间 [0, 1]\n(0.1 处于正常范围)",
            ha="right", va="center", fontsize=9.5, color="#15803d", fontweight="bold", rotation=90)

    # Annotation for the novel point
    ax.annotate("联合特征落入覆盖盲区！\n每个特征单独正常，\n组合却严重缺乏训练数据",
                xy=(novel_x1, novel_x2), xytext=(0.48, 0.28),
                arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.8),
                fontsize=10, color="#dc2626", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.5", facecolor="#fef2f2", edgecolor="#f87171", lw=1))

    ax.set_xlabel("特征 X1", fontsize=11)
    ax.set_ylabel("特征 X2", fontsize=11)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc="upper left", framealpha=0.9, fontsize=10)
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.set_title("高维特征空间中的覆盖盲区：单特征正常 ≠ 联合覆盖充分", fontsize=12, pad=12, fontweight="bold")

    plt.tight_layout()
    out = OUT_DIR / "high-dimensional-coverage-void.svg"
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    plot_day_night_covariate_shift()
    plot_concept_drift_prob_curve()
    plot_extrapolation_bifurcation()
    plot_high_dimensional_coverage_void()
    print("All plots generated successfully.")
