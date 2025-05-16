# [별찍기2] Baekjoon 2439 - 별찍기2
# https://www.acmicpc.net/problem/2439

"""
[문제 설명 요약]

빈칸이 줄어들면서 뒤에서 별 찍기


[접근 방식]

빈칸을 어떻게 수식으로 표현할 수 있는가?

빈칸이 줄어드는 수를 파악하고 별이 증가하는 것을 생각하기 



[주의할 점]

i는 0부터 시작


"""

def main():
    import sys

    a = int(sys.stdin.readline().rstrip())

    for i in range(a):
        print(" " * (a - i - 1) + "*" * (i+1))

if __name__ == "__main__":
    main()
