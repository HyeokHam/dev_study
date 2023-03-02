def solution(n):
    dict_factorial = {1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880, 10:3628800}
    for i in range(10, 0, -1) :
        if n >= dict_factorial[i] :
            return i 

# def factorial(n):
#     if n > 0 : return factorial(n-1) * n
#     else :
#         return 1

# def solution(n):
#     i = 1
#     while n >= factorial(i) :
#         i += 1
#     return i-1

# 재귀로 해도 안터지네? 실행 시간 때문에 터질 줄 알았는데..
# return에 -1을 추가해준 이유는 n이 처음으로 작아지는 값 - 1이 i! <= n을 성립하는 조건에 만족하는 최대 팩토리얼 값 이기 떄문이다.


'''
다른 사람 풀이
'''

# from math import factorial

# def solution(n):
#     k = 10
#     while n < factorial(k):
#         k -= 1
#     return k

# math.factorial(n) 메소드를 사용한 방법

n = int(input())
print(solution(n))


