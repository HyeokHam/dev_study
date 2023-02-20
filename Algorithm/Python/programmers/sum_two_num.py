def solution(num1, num2):
    return num1 + num2

num1, num2 = int(input().split())

'''
다른 사람 풀이
'''

# solution=lambda *x:sum(x)

# lambda에 가변인자를 표현한 * 사용

print(solution(num1=num1, num2=num2))