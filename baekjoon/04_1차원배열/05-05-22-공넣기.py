# [공넣기] Baekjoon 10810 - 공넣기
# https://www.acmicpc.net/problem/10810

"""
[문제 설명 요약]

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다.
각 방법은 세 정수 i j k로 이루어져 있으며, 
i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 
예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. 

약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다.
공을 넣을 바구니는 연속되어 있어야 한다.
공을 어떻게 넣을지가 주어졌을 때, 
M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.


[접근 방식]

1.	n, m을 입력받는다
2.	n 크기의 바구니 리스트를 만든다
3.	m번 반복하며, 각 입력 a, b, c를 받는다
4.	a-1부터 b-1까지 반복하며 c번 공을 넣는다
5.	마지막에 리스트를 공백 구분으로 출력한다


[주의할 점]

바구니는 1번부터 시작 <-> 리스트는 0번부터 시작



"""

def main():

    import sys

    # 바구니 n개, 공 넣기 m번
    n, m = map(int, sys.stdin.readline().rstrip().split())


    ba = [0]*n

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        for i in range(a-1, b):
            ba[i] = c
            
    print(" ".join(map(str, ba)))


if __name__ == "__main__":
    main()

'''
다음의 예시들 처럼 구간에 대한 값을 바꾸는 로직을 리스트 기반으로 구현하는 것임.


🎮 게임 인벤토리: 특정 구간에 아이템 장착
inventory = [None] * 10  # 빈 인벤토리 10칸

# 2번~5번 칸에 'Potion' 넣기 (1-index라고 가정)
for i in range(1, 5):  # 1~4번 인덱스
    inventory[i] = 'Potion'

print(inventory)


📅 수업 타임테이블 예약
schedule = [0] * 9  # 9교시까지 0=비어있음

# 2교시부터 4교시까지 예약 (1-index 기준)
for i in range(1, 4):  # 인덱스 1~3
    schedule[i] = 1  # 1=예약됨

print(schedule)


🌐 서버 상태 동기화
server_status = ['ok'] * 10

# 유저 4~6번의 상태를 'disconnected'로 갱신
for i in range(3, 6):
    server_status[i] = 'disconnected'

print(server_status)

'''