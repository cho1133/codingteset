# 🧠 Coding Test Practice with Baekjoon

AI 개발자 취업을 목표로 백준 문제를 Python으로 풀이하며 정리합니다.  
문제 접근 방식, 실수 방지 포인트, 복습 메모 등을 구조화해 기록합니다.

---

## 📁 폴더 구조

codingtest/
├── baekjoon/
│   ├── 01_입출력과_사칙연산/
│   │   ├── 01-05-01-Hello_World.py
│   │   ├── 01-05-01-Hello_World.md
│   ├── 02_조건문/
│   │   ├── 01-05-02-알람_시계.py
│   │   ├── 01-05-02-알람_시계.md
├── generate_template.py
├── update_readme.py
└── .vscode/
└── tasks.json

---

## ⚙️ 자동 템플릿 생성기 사용법

Python 스크립트를 통해 문제 풀이 템플릿을 자동 생성합니다:

```bash
python generate_template.py [문제번호] "[문제제목]" "[카테고리폴더]"


예시 
- python 실행
python generate_template.py 2884 "알람 시계" "02_조건문"

- vscode 실행
Tasks: Run Task → Generate Baekjoon Template


📌 파일 명명 규칙
[순서번호]-[MM-DD]-[문제이름].py / .md


📌 풀이 목록
아래 목록은 python update_readme.py로 자동 갱신됩니다.

<!-- START_PROBLEM_LIST -->


<!-- 여기에 update_readme.py가 테이블 자동 삽입 -->


<!-- END_PROBLEM_LIST -->

💡 학습 전략
	•	하루 1~2문제 풀이
	•	.md 중심으로 접근법 / 실수 포인트 정리
	•	정답 여부 표시로 복습 대상 관리

---

```bash