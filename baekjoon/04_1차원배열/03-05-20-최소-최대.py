# [최소-최대] Baekjoon 10818 - 최소-최대
# https://www.acmicpc.net/problem/10818

"""
[문제 설명 요약]

첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 

 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.



[접근 방식]

n정수 입력
리스트를 통한 n개의 정수 입력
공백으로 최소, 쵀대값 출력


[주의할 점]

공백을 구분해 출력하는 방법

print(a, b, sep= " " )  일반적으로 print()는 sep이 공백으로 한칸 띄어짐



"""

def main():

    import sys


    n = int(sys.stdin.readline().rstrip())
    total= list(map(int, sys.stdin.readline().rstrip().split()))

    print(min(total), max(total), sep=" ")

if __name__ == "__main__":
    main()
