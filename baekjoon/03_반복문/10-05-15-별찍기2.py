# [별찍기2] Baekjoon 2439 - 별찍기2
# https://www.acmicpc.net/problem/2439

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

    a = int(sys.stdin.readline().rstrip())

    for i in range(a):
        print(" " * (a - i - 1) + "*" * (i+1))

if __name__ == "__main__":
    main()
