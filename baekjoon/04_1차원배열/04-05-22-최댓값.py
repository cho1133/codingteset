# [최댓값] Baekjoon 2562 - 최댓값
# https://www.acmicpc.net/problem/2562

"""
[문제 설명 요약]

첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

[접근 방식]

9개의 반복 숫자 입력 후 empty list에 추가
list안에서 max값과 index를 찾기


[주의할 점]


[88 8 18 28 38 48 58 68 78]

마지막 최대값의 인덱스를 추출하는 과정에서 " + 1 " 을 하여 사람이 파악하는 순서로 보정하기
print(num_list.index(max(num_list)) + 1)

"""

def main():

    import sys

    num_list = []

    for i in range(9):
        a = int(sys.stdin.readline().rstrip())
        num_list.append(a)

    print(max(num_list))
    print(num_list.index(max(num_list)) + 1)
        

if __name__ == "__main__":
    main()
