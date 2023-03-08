def solution(balls, share):
    numerator = 1
    denominator = 1
    temp = 1
    for i in range(1, balls+1):
        numerator *= i
    for j in range(1, share+1):
        denominator *= j
    for k in range(1, (balls-share+1)):
        temp *= k
    return numerator // (denominator*temp)

# 본 문제는 조합에 관련된 문제이기 때문에 문제를 풀기 전에 순열과 조합에 대해서 짚고 넘어가야 한다.
# 

'''
다른 사람 풀이
'''
# import math

# def solution(balls, share):
#     return math.comb(balls, share)

# math.comb(n, k)는 nCk와 같은 조합 값을 반환함(n개의 수에서 k개를 선택)

# def solution(balls, share):
#     answer = factorial(balls) / (factorial(balls - share) * factorial(share))
#     return answer

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = result * i
#     return result

# 나의 문제 풀이와 똑같은 방법이지만 factorial() 함수를 만들어서 사용함
# 나의 풀이 방법과 같이 for문의 반복 보단 함수로 만들어서 재사용하는 것이 좋음

# from math import factorial as f
# def solution(balls, share):
#     return f(balls)/(f(share)*f(balls-share))

# math.factorial(n)는 n!의 값을 구해줌
# 순열의 기본 공식은 n! / (n-r)! 이며, 조합의 기본 공식은 n! / r!(n-r)! 이다.
# 여기서 순열이란 순서가 존재하기 때문에 서로 선택한 순서가 바뀌면 경우의 수도 다른 수가 된다.
# 예를 들어 순열에서는 (1, 2)와 (2, 1)은 다른 경우로 친다.
# 조합이란 따로 순서가 존재하지 않고 단순 조합을 따지기 때문에 순서가 바뀌어도 다른 수가 아니다.
# 예를 들어 조합에서는 (1, 2)와 (2, 1)은 같은 경우로 따지기 때문에 r!이 추가로 나눠진다.

balls, share = map(int, input().split())
print(solution(balls=balls, share=share))