# [A+B-4] Baekjoon 10951 - A+B-4
# https://www.acmicpc.net/problem/10951

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
    import sys

    for line in sys.stdin:
        if line.strip():
            a, b = map(int, line.strip().split())
            print(a + b)

if __name__ == "__main__":
    main()
