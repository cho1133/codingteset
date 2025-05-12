# [빠른 A+B] Baekjoon 15552 - 빠른 A+B
# https://www.acmicpc.net/problem/15552

"""
[문제 설명 요약]

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 
다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

[접근 방식]

숫자로 입력을 받아야 함 - range(literable)
반복하여 입력을 받기 
각 입력마다 A+B를 한 줄에 하나씩 순서대로 출력


[주의할 점]

input()은 입력에서 속도가 느릴 수 있음,
sys.stdin.readline()은 빠르지만 \n이 붙음 ex) hello\n
.rstrip() 없으면 문자열 비교, 처리 시 의도치 않은 버그 발생 
그래서 실전에서는 항상 .rstrip() 붙여주는 습관이 필요

colab, jupyter 에서는 또 - input()을 써야하네 

ValueError                                
Traceback (most recent call last)
<ipython-input-5-5fee02319279> in <cell line: 0>()
----> 1 a = int(sys.stdin.readline().rstrip())

ValueError: invalid literal for int() with base 10: ''


"""
import sys

def main():
    a = int(sys.stdin.readline().rstrip())

    for _ in range(a):
        b,c = map(int, sys.stdin.readline().rstrip().split())
        print(b+c)

if __name__ == "__main__":
    main()
