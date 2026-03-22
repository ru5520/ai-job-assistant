from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_file(name: str) -> str:
    path = BASE_DIR / name
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def clean_and_extract_keywords(text):
    text = text.lower()
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace("\n", " ")

    words = text.split()

    stop_words = {
        "we", "are", "the", "for", "with", "a", "an", "and",
        "to", "of", "in", "on", "is", "looking", "have", "has",
        "be", "will", "this", "that", "our", "you"
    }

    filtered_words = [word for word in words if word not in stop_words]

    return set(filtered_words)


def analyze_match(resume_keywords, jd_keywords):
    matched_keywords = resume_keywords & jd_keywords
    missing_keywords = jd_keywords - resume_keywords
    return matched_keywords, missing_keywords


def format_keywords(keyword_set):
    return ", ".join(sorted(keyword_set))


def save_report(output_path, resume_keywords, jd_keywords, matched_keywords, missing_keywords):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("AI Job Assistant Report\n\n")
        f.write("Resume Keywords:\n")
        f.write(format_keywords(resume_keywords) + "\n\n")

        f.write("JD Keywords:\n")
        f.write(format_keywords(jd_keywords) + "\n\n")

        f.write("Matched Keywords:\n")
        f.write(format_keywords(matched_keywords) + "\n\n")

        f.write("Missing Keywords:\n")
        f.write(format_keywords(missing_keywords) + "\n")


def main():
    print("AI Job Assistant is running...\n")

    resume_text = read_file("resume.txt")
    jd_text = read_file("jd.txt")

    resume_keywords = clean_and_extract_keywords(resume_text)
    jd_keywords = clean_and_extract_keywords(jd_text)

    matched_keywords, missing_keywords = analyze_match(resume_keywords, jd_keywords)

    print("Resume Keywords:")
    print(format_keywords(resume_keywords))

    print("\nJD Keywords:")
    print(format_keywords(jd_keywords))

    print("\nMatched Keywords:")
    print(format_keywords(matched_keywords))

    print("\nMissing Keywords:")
    print(format_keywords(missing_keywords))

    save_report(
        str(BASE_DIR / "output.txt"),
        resume_keywords,
        jd_keywords,
        matched_keywords,
        missing_keywords,
    )

    print("\nReport saved to output.txt")


if __name__ == "__main__":
    main()