# [문자열] Baekjoon 9086 - 문자열
# https://www.acmicpc.net/problem/9086

"""
[문제 설명 요약]



[접근 방식]



[주의할 점]

문자열(str)도 인덱싱이 가능하다.

print(a,b sep='')  -> ab
print(a,b)  -> a b 한칸 공백
print(a+b)  -> ab 붙임

"""

def main():
    
    input_num = int(input())

    for i in range(input_num):
        input_char = list(input())
        print(input_char[0]+input_char[-1])

if __name__ == "__main__":
    main()
