# [코딩은 체육과목 입니다] Baekjoon 25314 - 코딩은 체육과목 입니다
# https://www.acmicpc.net/problem/25314

"""
[문제 설명 요약]

long 추가하여 마지막에 int 붙이기


[접근 방식]

이미 문제에서 n은 4의 배수라고 정의됨 - 따로 정의할 필요 없음
total 을 문자열로 정의 



[주의할 점]
range(n//4) - 이게 되네
long을 계속 붙이고 마지막에 int를 추가한다 -> 반복이 끝나고 붙이기


"""
def main():
    
    n = int(input())

    total=""

    for i in range(n//4):
        total += "long "
    total +="int"

    print(total)


if __name__ == "__main__":
    main()
