# [공바꾸기] Baekjoon 10813 - 공바꾸기
# https://www.acmicpc.net/problem/10813

"""
[문제 설명 요약]

1부터 N번까지 번호가 적힌 바구니가 있다.
두 바구니의 번호를 계속해서 M번 입력받아, 서로 공을 교환한다.
마지막에 바구니 순서를 출력한다.

[접근 방식]

N개의 바구니 리스트 생성 (값은 1~N)
M번 반복하며 i, j를 입력받고 i-1, j-1 인덱스를 스왑
print(*baskets)로 출력

[주의할 점]

스왑방식 
a, b = b, a 형태 인데 더 추가적인 방법이 있을까??

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

swap(ba, i-1, j-1)

"""

def main():
    import sys


    n, m = map(int, sys.stdin.readline().rstrip().split())

    ba = list(range(1, n+1))


    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        ba[i - 1], ba[j - 1] = ba[j - 1], ba[i - 1]

    print(*ba)


if __name__ == "__main__":
    main()


