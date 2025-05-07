# [A+B - 3] Baekjoon 10950 - A+B - 3
# https://www.acmicpc.net/problem/10950

"""
[문제 설명 요약]

입력으로 주어진 T개 만큼  
각 줄마다 A, B를 입력받아 합을 출력하는 반복문 문제


[접근 방식]

첫 줄에서 T = int(input())
그 다음 T번 반복 → `for _ in range(T)

[주의할 점]

T입력 -> 반복문
for _ in range(T) - 변수 미포함 반복
한줄에 입력되는 a,b

처음에 문제제목보고 뭔말인지 이해 못함 -> 문제의 정의를 잘 이해할 것


"""

def main():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        print(a + b)

if __name__ == "__main__":
    main()