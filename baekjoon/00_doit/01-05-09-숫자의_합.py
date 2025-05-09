# [숫자의 합] Baekjoon 11720 - 숫자의 합
# https://www.acmicpc.net/problem/11720

"""
[문제 설명 요약]
첫줄 - 숫자개수 #5
둘쨰줄 - 첫줄 입력 숫자개수만큼 숫자 #54321


[접근 방식]
- 문제를 분류한다: 구현 / 그리디 / 정렬 / DP / ...
- 핵심 로직은 무엇인가?
- 필요한 자료구조 또는 알고리즘은?

[주의할 점]
풀이 1. 

- input() 은 숫자를 입력해도 출력은 str 형식으로 출력됨

- map(func, literable) literable객체(리스트, 문자열, 튜플 등)에 모든 함수를 적용함

- 반복(iteration)이 발생할 때 실행 (Lazy Evaluation)
	•	메모리 효율적: 리스트처럼 전체 데이터를 메모리에 올리지 않음
	•	속도 최적화: 필요한 순간까지만 계산하니까 느린 연산도 유리

- 처리순서
->  map(int, 54321(str)) -> map object [5,4,3,2,1] -> list[map(int, 54321)] 실제 정수 리스트 


풀이 2.  리스트 컴프리헨션

[변환할_값 for 반복변수 in 반복가능한_것]


풀이 3. input() 자체를 리스트로 받기 + 리스트 컴프리헨션 + 조건추가 

a = int(input())
b = input()

if len(b) == a:
    ~~
else:
    ~~


풀이 4. 리스트를 활용 + 반복문 합 구하기

"""

# 풀이 1.
def main():
    pass  # 여기에 문제 해결 코드 작성

    a = input()
    b = input()

    total = sum(map(int, b))
    print(total)

if __name__ == "__main__":
    main()


# 풀이 2. 리스트 컴프리헨션

a = input()
b = input()
print(sum([int(d) for d in b]))

# 풀이 3. 리스트 컴프리헨션에 조건 추가

def main():
    a = int(input())
    b = input()

    if len(b) == a:
        print(sum([int(d) for d in b]))
    else:
        print("입력 길이 불일치")

if __name__ == "__main__":
    main()

# 풀이 4. 리스트를 활용 + 반복문 합 구하기

def main():
    a = input()
    b = list(input())
    sum = 0

    for i in b:
        sum = sum + int(i)
    
    print(sum)

if __name__ == "__main__":
    main()