#!/usr/bin/env python3
"""
Flesch-Kincaid Grade readability checker for Agentism project.

Usage:
    python check_readability.py <file1.md> [file2.md ...]
    python check_readability.py principles/CP-*.md

Exits with code 1 if any file fails the target range (Grade 8-10).
Exits with code 0 if all files pass.

See: research.md Section 2 for tool selection rationale.
"""
import sys
import re
import textstat


TARGET_MIN = 7.0   # Grade 7: allow slight under-shoot
TARGET_MAX = 12.0  # Grade 12: hard ceiling


def strip_markdown(text):
    """Remove markdown syntax before scoring."""
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    # Remove images and links, keep link text
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove heading markers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)
    text = re.sub(r'_{1,3}([^_]+)_{1,3}', r'\1', text)
    # Remove horizontal rules
    text = re.sub(r'^[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    # Remove blockquote markers
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    # Remove list markers
    text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
    return text.strip()


def extract_plain_language_summary(text):
    """Extract only the Plain-Language Summary section for targeted scoring."""
    match = re.search(
        r'##\s+Plain-Language Summary\s*\n(.*?)(?=\n##|\Z)',
        text,
        flags=re.DOTALL | re.IGNORECASE
    )
    if match:
        section = match.group(1)
        # Remove HTML comments
        section = re.sub(r'<!--.*?-->', '', section, flags=re.DOTALL)
        return section.strip()
    return None


def check_file(filepath):
    """Check a single file. Returns (passed, grade, message)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw = f.read()
    except FileNotFoundError:
        return False, None, f"File not found: {filepath}"
    except Exception as e:
        return False, None, f"Error reading {filepath}: {e}"

    # Try to score only the Plain-Language Summary section
    summary = extract_plain_language_summary(raw)
    if summary:
        text_to_score = strip_markdown(summary)
        scope = "Plain-Language Summary"
    else:
        text_to_score = strip_markdown(raw)
        scope = "full document"

    if len(text_to_score.split()) < 20:
        return False, None, f"SKIP  {filepath}: too short to score ({scope})"

    grade = textstat.flesch_kincaid_grade(text_to_score)

    if TARGET_MIN <= grade <= TARGET_MAX:
        status = "PASS"
        passed = True
    else:
        status = "FAIL"
        passed = False

    msg = f"{status}  {filepath}: FK Grade {grade:.1f}  [{scope}]  target {TARGET_MIN}-{TARGET_MAX}"
    return passed, grade, msg


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_readability.py <file.md> [file2.md ...]")
        sys.exit(1)

    files = sys.argv[1:]
    results = [check_file(f) for f in files]

    all_passed = True
    for passed, grade, msg in results:
        print(msg)
        if not passed and grade is not None:
            all_passed = False

    if not all_passed:
        print("\nReadability check FAILED. Revise plain-language summaries until FK Grade is within target range.")
        sys.exit(1)
    else:
        print("\nReadability check PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    main()
