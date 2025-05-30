# [평균] Baekjoon 1546 - 평균
# https://www.acmicpc.net/problem/1546

"""
[문제 설명 요약]

준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
그리고 나서 모든 점수를 점수/M*100으로 고쳤다
준이의 최고점이 70이고, 수학점수가 50이었으면 
수학점수는 50/70*100이 되어 71.43점이 된다.


첫째 줄에 시험 본 과목의 개수 N이 주어진다.
둘째 줄에 세준이의 현재 성적이 주어진다
첫째 줄에 새로운 평균을 출력

[접근 방식]

n 개수를 입력받기
socres - n개의 점수 입력
max(scores)으로 새롭게 정의되는 total값
개수만큼 반복하며 마지막에 새로운 평균을 구하기


[주의할 점]

doit 풀이처럼 한번에 묶어서 진행하는 것이 아닌
새로운 점수 환산 방식을 구하고 나중에 평균 나누기를 진행

"""

def main():
    import sys

    n = int(sys.stdin.readline())
    scores = list(map(int, sys.stdin.readline().split()))

    if len(scores) != n:
        print("입력 개수 불일치")
        exit()

    max_score = max(scores)
    adjusted_total = 0

    for score in scores:
        adjusted_total += score / max_score * 100

    print(adjusted_total / n)

if __name__ == "__main__":
    main()
