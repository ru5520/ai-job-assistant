import re
from taxonomy import JOB_TAXONOMY

def save_report(result, output_path="report.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Job Classification Report\n\n")

        f.write("Primary Direction:\n")
        f.write(f"{result['primary_direction']}\n\n")

        f.write("Description:\n")
        f.write(f"{result['description']}\n\n")

        f.write("Confidence:\n")
        f.write(f"{result['confidence']}\n\n")

        f.write("Detailed Scores:\n")
        for category, score in result["detail_scores"].items():
            f.write(f"{category}: {score}\n")

        f.write("\nProportions:\n")
        for category, ratio in result["proportions"].items():
            f.write(f"{category}: {ratio:.0%}\n")

def clean_text(text):
    """基础数据清洗：统一小写，移除特殊符号"""
    text = text.lower()
    text = re.sub(r"[^\w\s\u4e00-\u9fa5]", " ", text)
    return text


def classify_job(jd_text):
    cleaned_jd = clean_text(jd_text)
    scores = {}

    for category, info in JOB_TAXONOMY.items():
        score = 0
        keywords = info["keywords"]

        if isinstance(keywords, dict):
            keyword_items = keywords.items()
        else:
            keyword_items = [(word, 1) for word in keywords]

        for word, keyword_weight in keyword_items:
            word_lower = str(word).lower()
            keyword_weight = int(keyword_weight)

            if (not word_lower.isascii()) or (" " in word_lower):
                count = cleaned_jd.count(word_lower)
            else:
                count = len(re.findall(rf"\b{re.escape(word_lower)}\b", cleaned_jd))

            score += count * keyword_weight

        scores[category] = score

    sorted_scores = dict(
        sorted(scores.items(), key=lambda x: x[1], reverse=True)
    )

    if all(score == 0 for score in scores.values()):
        top_category = "Unknown"
        proportions = {}
        confidence = 0
    else:
        top_category = next(iter(sorted_scores))
        total_score = sum(scores.values())
        confidence = scores[top_category] / total_score if total_score > 0 else 0

        proportions = {
            category: round(score / total_score, 2)
            for category, score in sorted_scores.items()
            if total_score > 0
        }

    return {
        "primary_direction": top_category,
        "confidence": round(confidence, 2),
        "detail_scores": sorted_scores,
        "proportions": proportions,
        "description": JOB_TAXONOMY.get(top_category, {}).get("desc", "")
    }


if __name__ == "__main__":
    with open("sample_jd.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()

    result = classify_job(jd_text)

    print("识别结果:", result["primary_direction"])
    print("置信度:", result["confidence"])
    print("详细得分:", result["detail_scores"])
    print("方向占比:", result["proportions"])

    save_report(result)
    print("报告已保存到 report.txt")