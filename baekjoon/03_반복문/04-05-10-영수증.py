# [영수증] Baekjoon 25304 - 영수증
# https://www.acmicpc.net/problem/25304

"""
[문제 설명 요약]
총 금액 X,  N개의 물건의 가격과 수량
물건 가격 * 수량의 합이 X와 같은지 비교


[접근 방식]
1. X, N을 입력

2. 반복문을 N번 돌면서:
각 줄의 가격 a, 수량 b를 입력받고
total += a * b 로 누적합 계산

3. total == X 이면 "Yes", 아니면 "No" 출력

[주의할 점]

total 부분 표현과 생각



"""

def main():
    total = 0
    X = int(input())
    N = int(input())

    for _ in range(N):
        a, b = map(int, input().split())
        total += a * b

    if total == X:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()