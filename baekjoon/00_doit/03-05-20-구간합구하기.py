# [구간합구하기] Baekjoon 11659 - 구간합구하기
# https://www.acmicpc.net/problem/11659

"""
[문제 설명 요약]

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 
둘째 줄에는 N개의 수가 주어진다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

[접근 방식]

구간의 합을 구하는 문제

N, M 입력  -> 5 ,3
mumbers 로 N개의 수 입력 -> 5개 입력
i, j -> 1번째 구간 
i, j -> 2번쨰 구간
i, j -> 3번째 구간


구간합 리스트 구하는 반복문
- sum_list 정의, temp = 0 
구간합을 출력하는 반복문
- M을 기준으로  i~j 범위 입력 
- 출력방식 

[주의할 점]

[0]이 담긴 리스트를 생성 - 누적합(Prefix Sum) 리스트를 만들기 위한 초기값

[0,5,9,12,14,15]에서
index - 0 / 합없음 - 0
index - 1 / sum_list[0] - 5
index - 2 / sum_list[0] + sum_list[1]  - 9

-> 빈 리스트는 누적합의 인덱스를 정의하는데 힘들어짐 , 구간합을 쉽게 계산하기 위해

temp로 누적합을 구하고 리스트에 저장 

"""

def main():

    import sys

    n, m = map(int, sys.stdin.readline().rstrip().split())

    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    sum_list = [0]
    temp = 0
                
                
    for i in numbers:
        temp = temp + i
        sum_list.append(temp)

    for i in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        print(sum_list[b]- sum_list[a-1])


if __name__ == "__main__":
    main()
