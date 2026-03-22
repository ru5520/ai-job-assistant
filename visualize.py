import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from classifier import classify_job

BASE_DIR = Path(__file__).resolve().parent


def plot_radar(scores, output_path="radar_chart.png"):
    """根据分类得分绘制雷达图，并保存为图片文件。"""
    categories = list(scores.keys())
    values = list(scores.values())

    # 闭合图形：首尾相连
    values += values[:1]

    # 生成每个维度对应的角度
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    # 创建极坐标图
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 绘制轮廓和填充区域
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)

    # 设置每个轴的标签
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # 标题
    ax.set_title("Job Direction Radar Chart", pad=20)

    # 自动调整布局
    plt.tight_layout()

    # 保存图片（使用 Agg 后端，不依赖弹窗显示）
    plt.savefig(output_path)
    plt.close(fig)


if __name__ == "__main__":
    sample_path = BASE_DIR / "sample_jd.txt"
    with open(sample_path, "r", encoding="utf-8") as f:
        jd_text = f.read()

    result = classify_job(jd_text)

    print("识别结果:", result["primary_direction"])
    print("置信度:", result["confidence"])
    print("详细得分:", result["detail_scores"])

    if "proportions" in result:
        print("方向占比:")
        for category, ratio in result["proportions"].items():
            print(f"{category}: {ratio:.0%}")

    out_png = BASE_DIR / "radar_chart.png"
    plot_radar(result["detail_scores"], str(out_png))

    print(f"雷达图已保存到 {out_png}")