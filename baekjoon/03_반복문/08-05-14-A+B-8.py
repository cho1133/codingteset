# [A+B-8] Baekjoon 11022 - A+B-8
# https://www.acmicpc.net/problem/11022

"""
[문제 설명 요약]

T 총 횟수 입력
a,b 입력 후 두 수의 합을 출력하는 문제

[접근 방식]

T 입력
반복문 안에서 입력을 받고 합까지 진행
매 계산마다 print로 포멧에 맞게 출력


[주의할 점]

f-string 유의해서 사용하기

"""

def main():
    import sys

    T = int(sys.stdin.readline().rstrip())

    for i in range(T):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        c = a+b
        print(f'Case #{i+1}: {a} + {b} = {c}')
        
if __name__ == "__main__":
    main()
