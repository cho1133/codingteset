# [A+B-4] Baekjoon 10951 - A+B-4
# https://www.acmicpc.net/problem/10951

"""
[문제 설명 요약]
> 여기에 문제 설명을 복사 붙여넣기 하세요.


[접근 방식]

for line in sys.stdin 구문으로 EOF까지 자동 반복 처리
또는 while 루프 + readline() + try-except로 직접 예외 처리

[주의할 점]


EOF 도달 시 문제 발생
sys.stdin.readline() → 빈 문자열 '' 반환
rstrip().split() → 빈 리스트 []
map(int, []) → unpacking 에러 (ValueError: not enough values to unpack)


"""

def main():
    import sys

    for line in sys.stdin:
        if line.strip():
            a, b = map(int, line.strip().split())
            print(a + b)

if __name__ == "__main__":
    main()


def main():
    import sys

    while True:
        line = sys.stdin.readline()
        if not line:
            break  # EOF
        try:
            a, b = map(int, line.strip().split())
            print(a + b)
        except ValueError:
            continue  # 빈 줄이나 잘못된 입력 무시
if __name__ == "__main__":
    main()