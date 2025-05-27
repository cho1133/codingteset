# [과제안내신분] Baekjoon 5597 - 과제안내신분
# https://www.acmicpc.net/problem/5597

"""
[문제 설명 요약]

교수님이 내준 특별과제를 28명이 제출했는데, 
그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.


[접근 방식]

1~30 리스트 생성
28까지 새로운 리스트 생성
두 리스트를 비교하며 없는 원소 출력


[주의할 점]




"""

def main():


    stu = list(range(1, 31))

    submit = []

    for _ in range(28):
        n = int(input())
        submit.append(n)
        
    for s in stu:
        if s not in submit:
            print(s)
    
    # set으로 정의할 경우 원소의 배열이 일정하지 않습니다.
    # 따라서 sorted로 오름차순 정렬을 해야 합니다.

    # missing = set(stu) - set(submit)
    # for num in sorted(missing):
    #     print(num)

if __name__ == "__main__":
    main()
