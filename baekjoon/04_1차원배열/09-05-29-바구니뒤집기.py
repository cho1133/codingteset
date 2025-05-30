# [바구니뒤집기] Baekjoon 10811 - 바구니뒤집기
# https://www.acmicpc.net/problem/10811

"""
[문제 설명 요약]

첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 
방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. 
(1 ≤ i ≤ j ≤ N)

[접근 방식]

n(바구니개수),m(반복횟수)입력
list를 입력값을 기준으로 정의
m번 반복하여 i,j 입력
리스트 슬라이싱을 통해 배열변경

[주의할 점]

10813 - 공바꾸기 문제와 다르다 : 각각의 원소를 바꾸는 방법이 아닌

리스트의 순서를 바꾸는 것 -  리스트의 슬라이싱(범위)지정 후 변경
*슬라이싱의 범위는 모두 포함 list[1:3] -> list[1],[2],[3]


"""

def main():
    import sys

    n, m = map(int, sys.stdin.readline().rstrip().split())

    ba = list(range(1,n+1))

    for _ in range(m):
        i,j = map(int, sys.stdin.readline().rstrip().split())
        ba[i-1 : j] = reversed(ba[i-1 : j])
        #ba[i-1:j] = ba[i-1:j][::-1]
        
    print(*ba)


if __name__ == "__main__":
    main()
