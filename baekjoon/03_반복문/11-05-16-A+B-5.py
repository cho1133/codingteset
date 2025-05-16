# [A+B-5] Baekjoon 10952 - A+B-5
# https://www.acmicpc.net/problem/10952

"""
[문제 설명 요약]

입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.


[접근 방식]

입력의 개수가 정해지지 않으면 어떻게 반복을 멈추고 처리할 것인가?

-> whlie True로 무한 루프 돌리기
if 조건으로 a,b == 0이라면  break로 종료


[주의할 점]

break point 잘 찾기


"""

def main():

    import sys

    while True:
        a, b = map(int, sys.stdin.readline().strip().split())
        if a == 0 and b == 0:
            break
        print(a + b)
    

if __name__ == "__main__":
    main()
