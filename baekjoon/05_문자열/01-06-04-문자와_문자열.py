# [문자와_문자열] Baekjoon 27866 - 문자와_문자열
# https://www.acmicpc.net/problem/27866

"""
[문제 설명 요약]

단어 S와 정수 i를 입력받고
s의 i 번째 글자를 출력


[접근 방식]

단어의 입력 구현
i 입력
단어의 i번째 글자 출력

[주의할 점]

list(word) = apple 
i  = 3  p를 출력하려고 하지만 0부터 시작하기 때문에 l이 출력됨
word[3-1] 따라서 마지막에 -1을 하여 사용자의 입력순서와 동일하게 수정 


"""

def main():

    word = input()
    i = int(input())

    a = list(word)


    print(a[i-1])
    

if __name__ == "__main__":
    main()
