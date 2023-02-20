def solution(num1, num2):
    return num1 % num2

'''
다른 사람 풀이
'''

# def solution(num1, num2):
#     return divmod(num1, num2)[1]

num1, num2 = int(input().split())
print(solution(num1=num1, num2=num2))