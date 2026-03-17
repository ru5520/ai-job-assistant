"""AI Job Assistant.

This script compares a resume against a job description by extracting simple
keyword sets and reporting:
- keywords found in the resume
- keywords found in the job description
- matched keywords
- missing keywords (present in JD but not resume)

Inputs (same folder as this script):
- `resume.txt`
- `jd.txt`

Outputs:
- prints results to the terminal
- writes a report to `output.txt`
"""


def read_file(path: str) -> str:
    """Read a UTF-8 text file and return its contents."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def clean_and_extract_keywords(text: str) -> set[str]:
    """Normalize text and extract a set of keywords.

    Steps:
    - lowercase
    - replace basic punctuation/newlines with spaces
    - split on whitespace
    - remove a small built-in stop-word list

    This is intentionally simple and language-agnostic; for real NLP, you would
    use a tokenizer and a richer stop-word list.
    """
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
        "a",
        "an",
        "and",
        "are",
        "be",
        "for",
        "has",
        "have",
        "in",
        "is",
        "looking",
        "of",
        "on",
        "our",
        "that",
        "the",
        "this",
        "to",
        "we",
        "will",
        "with",
        "you",
    }

    filtered_words = [word for word in words if word not in stop_words]

    return set(filtered_words)


def analyze_match(
    resume_keywords: set[str],
    jd_keywords: set[str],
) -> tuple[set[str], set[str]]:
    """Compute matched and missing keywords.

    Returns:
    - matched_keywords: keywords present in both resume and JD
    - missing_keywords: keywords present in JD but not in resume
    """
    matched_keywords = resume_keywords & jd_keywords
    missing_keywords = jd_keywords - resume_keywords
    return matched_keywords, missing_keywords


def format_keywords(keyword_set: set[str]) -> str:
    """Format a keyword set into a sorted, comma-separated string."""
    return ", ".join(sorted(keyword_set))


def save_report(
    output_path: str,
    resume_keywords: set[str],
    jd_keywords: set[str],
    matched_keywords: set[str],
    missing_keywords: set[str],
) -> None:
    """Write an analysis report to a UTF-8 text file."""
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


def main() -> None:
    """Run the keyword extraction, comparison, and reporting pipeline."""
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
        "output.txt",
        resume_keywords,
        jd_keywords,
        matched_keywords,
        missing_keywords,
    )

    print("\nReport saved to output.txt")


if __name__ == "__main__":
    main()