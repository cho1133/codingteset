# [평균구하기] Baekjoon 1546 - 평균구하기
# https://www.acmicpc.net/problem/1546

"""
[문제 설명 요약]

시험 점수 n개가 주어짐
가장 높은 점수 M을 기준으로 모든 점수를 조작함
→ 각각의 점수를 점수 / M * 100으로 바꿔야 해
작된 점수들의 평균을 출력


[접근 방식]

점수의 개수 입력
리스트로 점수들 받기
계산을 위한 max, sum 구하기
print()를 통한 출력

뭔가 풀긴 했지만 1차원 적인 풀이다..

------------------------

[주의할 점]

백준에서는 자동적으로 입력의 개수를 정해주지만
실전 코드에서는 항상 예외처리를 생각하여 입력개수를 맞출 것.

if len(numlist) != num:
        print("입력 개수 불일치")
        exit()

        
리스트가 있다면 -> 리스트컴프리헨션 사용해보기



"""
import sys

def main():


    num = int(sys.stdin.readline().rstrip())
    numlist = list(map(int, sys.stdin.readline().rstrip().split()))

    
    # if len(numlist) != num:
    #     print("입력 개수 불일치")
    #     exit()
    
    totalsum = sum(numlist)
    maxnum = max(numlist)
        
    print(totalsum / maxnum * 100 / num)

if __name__ == "__main__":
    main()

## 리스트 컴프리헨션은 차후
def main():
    
    num = int(sys.stdin.readline().rstrip())
    numlist = list(map(int, sys.stdin.readline().rstrip().split()))

    
    

if __name__ == "__main__":
    main()
