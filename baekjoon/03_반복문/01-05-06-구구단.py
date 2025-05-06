# [구구단] Baekjoon 2739 - 구구단
# https://www.acmicpc.net/problem/2739

"""
[문제 설명 요약]
정수 N(1 ≤ N ≤ 9)을 입력받아 N단 구구단을 출력하는 문제  
출력 결과  `N * i = 결과` (i: 1~9)

[접근 방식]
- 입력값 N을 정수로 받음
- `for i in range(1, 10)` 반복문 사용
- `print(f"{n} * {i} = {n * i}")` 형식으로 출력

[주의할 점]
f 스트링 사용법 공부 
반복 되는 범위를 생각하기 

"""

def main():
    n = int(input())
    for i in range(1, 10):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    main()
