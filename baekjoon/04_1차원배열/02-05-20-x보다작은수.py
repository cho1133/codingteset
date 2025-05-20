# [x보다작은수] Baekjoon 10871 - x보다작은수
# https://www.acmicpc.net/problem/10871

"""
[문제 설명 요약]
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

입력)
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 
주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.


[접근 방식]

둘째 줄에 수열 A를 이루는 정수 N이 주어진다??
1) 문제에서 이미 주어지는 것인지

2) 직접 입력을 해야하는 것인지 -> 이것임!


이어서 출력하기

print( 내용  , end=" ") - 줄을 바꾸지 않고 " " 빈칸을 출력



[주의할 점]

-for i in a : a가 리스트이기 때문에 range(a) 사용하지 말 것

- print()는 기본적으로 end = \n 같이 기본 줄바꿈이 적용됨
end  = " " 공백을 부여함으로 줄이 넘어가지 않고 출력 될 수 있도록 코드 구현 


"""

def main():
    import sys

    n,x = map(int, sys.stdin.readline().rstrip().split())

    a = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in a:
        if i < x:
            print(i, end=" ")

if __name__ == "__main__":
    main()
