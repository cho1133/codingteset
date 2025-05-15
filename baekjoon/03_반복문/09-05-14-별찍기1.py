# [별찍기1] Baekjoon 2438 - 별찍기1
# https://www.acmicpc.net/problem/2438

"""
[문제 설명 요약]

첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
첫째 줄에 N(1 ≤ N ≤ 100)이 주어지고
첫째 줄부터 N번째 줄까지 차례대로 출력  

[접근 방식]

반복문 사용

[주의할 점]

반복하여 표현하는데 항상 시작은 0부터 시작이다.


"""

def main():

    import sys

    a = int(sys.stdin.readline().rstrip())

    for i in range(a):
        print("*" * (i+1))
    
    

if __name__ == "__main__":
    main()
