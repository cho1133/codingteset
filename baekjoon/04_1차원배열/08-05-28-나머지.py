# [나머지] Baekjoon 3052 - 나머지
# https://www.acmicpc.net/problem/3052

"""
[문제 설명 요약]

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

[접근 방식]

반복하여 10개의 수를 입력받음
10개의 수를 각각 42로 나눔
나머지가 같은 것인지 판별
판별 후 중복없이 결과 출력 

[주의할 점]

count()는 특정 값이 몇번 등장했는지 세는 함수 [1,2,3,3] count(3) = 2
전체 개수를 알 땐 len() 사용 list = [1,2,3,3] len(list) = 3


count(set(split_list)) ❌ -> len(set(split_list)) 
"""

def main():


    normal_list = []
    split_list = []
    
    #시간복잡도가 높다.
    for _ in range(10):
        input_num = int(input())
        normal_list.append(input_num)
        for i in normal_list:
            split_num = i%42
            split_list.append(split_num)

    print(len(set(split_list)))
        

    # 조금 더 명확하고 단순하게 
    # remainder_set = set()

    # for _ in range(10):
    #     num = int(input())
    #     remainder_set.add(num % 42)

    # print(len(remainder_set))    

if __name__ == "__main__":
    main()
