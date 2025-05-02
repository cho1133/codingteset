import os
import sys
from datetime import datetime

def get_next_index(category_dir):
    if not os.path.exists(category_dir):
        return 1
    files = [f for f in os.listdir(category_dir) if f.endswith('.py')]
    return len(files) + 1

def create_template_files(problem_num, problem_title, category):
    platform = "baekjoon"
    now = datetime.now()
    month_day = now.strftime("%m-%d")
    safe_title = problem_title.replace(' ', '_')
    
    # 폴더 경로
    base_dir = os.path.join(os.getcwd(), platform, category)
    os.makedirs(base_dir, exist_ok=True)

    # 순서 번호
    index = get_next_index(base_dir)
    index_str = str(index).zfill(2)

    # 최종 파일명: 01-05-02-알람_시계
    filename = f"{index_str}-{month_day}-{safe_title}"

    py_path = os.path.join(base_dir, f"{filename}.py")
    md_path = os.path.join(base_dir, f"{filename}.md")
    problem_url = f"https://www.acmicpc.net/problem/{problem_num}"
    today = now.strftime("%Y-%m-%d")

    py_content = f'''# [{problem_title}] Baekjoon {problem_num} - {problem_title}
# {problem_url}

"""
[문제 설명 요약]
> 여기에 문제 설명을 복사 붙여넣기 하세요.


[접근 방식]
- 문제를 분류한다: 구현 / 그리디 / 정렬 / DP / ...
- 핵심 로직은 무엇인가?
- 필요한 자료구조 또는 알고리즘은?

[주의할 점]
- 엣지 케이스: 
- 시간 복잡도 고려: 
- 실수하기 쉬운 조건 분기:

"""

def main():
    pass  # 여기에 문제 해결 코드 작성

if __name__ == "__main__":
    main()
'''

    md_content = f'''# 📝 Baekjoon {problem_num} - {problem_title}

## 📅 날짜
- {today}

## 🔗 문제 링크
[문제 바로가기]({problem_url})

---

## 📌 문제 설명 요약

> 여기에 문제 설명을 복사 붙여넣기 하세요.

---

## 💡 접근 방식

- 분류: (예: 정렬, 탐색, 구현, DP 등)
- 핵심 아이디어:
- 필요한 자료구조 / 알고리즘:

---

## ⚠️ 실수 방지 포인트

- 조건 분기에서 놓치기 쉬운 부분:
- 엣지 케이스:
- 시간 복잡도 / 공간 복잡도 고려:

---

## 🧠 복습 메모

- 나중에 떠올릴 키워드:
- 처음에 어떤 실수를 했는가:
'''

    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(py_content)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"✅ 템플릿 생성 완료:\n- {py_path}\n- {md_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("사용법: python generate_template.py [문제번호] [문제제목] [카테고리폴더이름]")
        print("예시: python generate_template.py 2884 '알람 시계' '02_조건문'")
        sys.exit(1)

    problem_num = sys.argv[1]
    problem_title = sys.argv[2]
    category = sys.argv[3]
    create_template_files(problem_num, problem_title, category)