import matplotlib.pyplot as plt
import numpy as np
from classifier import classify_job


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

    # 保存图片
    plt.savefig(output_path)

    # 显示图表
    plt.show()


if __name__ == "__main__":
    # 读取 JD 文件
    with open("sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()

    # 分类
    result = classify_job(jd_text)

    # 终端输出
    print("识别结果:", result["primary_direction"])
    print("置信度:", result["confidence"])
    print("详细得分:", result["detail_scores"])

    if "proportions" in result:
        print("方向占比:")
        for category, ratio in result["proportions"].items():
            print(f"{category}: {ratio:.0%}")

    # 绘图并保存
    plot_radar(result["detail_scores"])

    print("雷达图已保存到 radar_chart.png")