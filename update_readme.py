import os
import re

ROOT_DIR = os.getcwd()
BAEKJOON_DIR = os.path.join(ROOT_DIR, "baekjoon")
README_PATH = os.path.join(ROOT_DIR, "README.md")

PROBLEM_LIST_HEADER = "## 📌 풀이 목록"
PROBLEM_TABLE_HEADER = "| 카테고리 | 순번 | 날짜 | 문제 번호 | 문제 이름 | 상태 | 링크 |\n" + \
                       "|----------|------|--------|------------|-------------|------|------|\n"

def extract_problem_info(category, filename):
    match = re.match(r"(\d+)-(\d{2})-(\d{2})-(.+)\.md", filename)
    if not match:
        return None

    index, mm, dd, title = match.groups()
    title_kor = title.replace('_', ' ')
    filepath = os.path.join(BAEKJOON_DIR, category, filename)

    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # 문제 번호 추출
    match_num = re.search(r"Baekjoon\s+(\d+)", content)
    if not match_num:
        return None
    problem_num = match_num.group(1)
    link = f"https://www.acmicpc.net/problem/{problem_num}"

    return {
        "category": category,
        "index": index,
        "date": f"2025-{mm}-{dd}",
        "num": problem_num,
        "title": title_kor,
        "link": link,
        "status": "✅"  # 기본값은 성공, 필요시 실패 표시 가능
    }

def generate_table():
    rows = []
    for category in sorted(os.listdir(BAEKJOON_DIR)):
        cat_path = os.path.join(BAEKJOON_DIR, category)
        if not os.path.isdir(cat_path):
            continue
        for fname in sorted(os.listdir(cat_path)):
            if not fname.endswith(".md"):
                continue
            info = extract_problem_info(category, fname)
            if info:
                row = f"| {info['category']} | {info['index']} | {info['date']} | {info['num']} | {info['title']} | {info['status']} | [🔗]({info['link']}) |"
                rows.append(row)
    return PROBLEM_TABLE_HEADER + "\n".join(rows)

def update_readme():
    with open(README_PATH, encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    in_table = False
    for line in lines:
        if PROBLEM_LIST_HEADER in line:
            new_lines.append(line)
            new_lines.append("\n" + generate_table() + "\n")
            in_table = True
        elif in_table:
            if line.startswith("## "):
                new_lines.append(line)
                in_table = False
        elif not in_table:
            new_lines.append(line)

    with open(README_PATH, "w", encoding='utf-8') as f:
        f.writelines(new_lines)

    print("✅ README.md 풀이 목록 갱신 완료!")

if __name__ == "__main__":
    update_readme()