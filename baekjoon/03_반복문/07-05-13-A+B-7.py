# [A+B-7] Baekjoon 11021 - A+B-7
# https://www.acmicpc.net/problem/11021

"""
[문제 설명 요약]

테스트 케이스 T
T줄에 걸쳐 두 정수 A, B가 입력
각 테스트마다 "Case #x: A+B" 형식으로 출력

[접근 방식]

- 첫 줄에서 테스트 케이스 수 T를 입력
- T번 반복하면서 각 줄의 A, B를 입력받고 A + B를 계산
- f-string을 이용해 형식에 맞춰 출력

[주의할 점]

- 출력 형식 정확히 맞추기 (Case #x: 와 결과 사이 공백, : 위치 등)
- 인덱스는 1부터 시작해야 하므로 range(T) → i+1 사용

"""
import sys

def main():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(f"Case #{i + 1}: {a + b}")

if __name__ == "__main__":
    main()