# 짝수의 합
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.


# 나의 풀이
def solution(n):
    total = 0 # 합계 초기값 
    int(n)

    for n in range(1, n+1) :
        if n % 2 == 0:
            total += n
        else :
            continue
    return total


# 조금 더 간단하게 작성하는 법
"""
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])
"""
