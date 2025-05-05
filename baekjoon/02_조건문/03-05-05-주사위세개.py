# [주사위세개] Baekjoon 2480 - 주사위세개
# https://www.acmicpc.net/problem/2480

"""
[문제 설명 요약]

같은 눈이 3개: 10,000 + (같은 눈) x 1,000
같은 눈이 2개: 1,000 + (같은 눈) x 100
모두 다름: (가장 큰 눈) x 100


[접근 방식]

a,b,c 3가지 입력
3개가 동일할 때 / 2개가 같을 떄 / 모두 다를 때 분기
가장 큰 것? -> max()


[주의할 점]

모든 눈이 다른 경우 가장 큰 값을 사용하기
분기 파악을 명확히 할 것.


"""


def main():
    a, b, c = map(int, input().split())

    if a == b == c:
        print(10000 + a * 1000)
    elif a == b or a == c:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(max(a, b, c) * 100)

if __name__ == "__main__":
    main()