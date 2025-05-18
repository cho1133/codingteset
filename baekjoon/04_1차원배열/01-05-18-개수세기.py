# [개수세기] Baekjoon 10807 - 개수세기
# https://www.acmicpc.net/problem/10807

"""
[문제 설명 요약]

정수 N개가 주어졌을 때, 정수 v가 몇 개 있는지 구하는 문제


[접근 방식]

리스트트에 N개 정수 저장 뒤 count()


[주의할 점]

N과 v는 따로 주어지고, 숫자 리스트는 한 줄에 공백으로 주어짐
리스트가 문자열로 입력되기 때문에 반드시 map(int, ...)를 통해 정수로 변환해야 함
.count()는 문자열 리스트에서는 정확히 작동하지 않음 → 정수 리스트로 변환 필수

"""

def main():
    import sys

    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    v = int(sys.stdin.readline())

    print(numbers.count(v))
if __name__ == "__main__":
    main()
