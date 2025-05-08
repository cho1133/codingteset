# [합] Baekjoon 8393 - 합
# https://www.acmicpc.net/problem/8393

"""
[문제 설명 요약]

정수 n이 주어질 때 1부터 n까지의 합을 출력하는 문제

[접근 방식]

방법 1: 반복문 사용 → 총합 변수에 누적
방법 2: 수학공식 사용 → n(n+1)//2

[주의할 점]

출력 형식은 숫자 하나
공백/줄바꿈 없음
"""

# 방법 1
def main():
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += i
    print(total)


# 방법 2
def main():
    n = int(input())
    print(n * (n + 1) // 2)

if __name__ == "__main__":
    main()
