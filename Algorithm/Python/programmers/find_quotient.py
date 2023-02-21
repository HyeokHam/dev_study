def solution(num1, num2):
    return num1 // num2

'''
다른 사람 풀이
'''

# solution = int.__floordiv__

# operator.floordiv(a, b) | operator.__floordiv__(a, b)는 a // b를 반환함
# 단순한 연산자의 메소드임

# def solution(num1, num2):
#     return divmod(num1, num2)[0]

# divmod(a, b)는 몫과 나머지를 구해 [몫, 나머지]와 같은 형태로 반환함 

num1, num2 = int(input().split())
print(solution(num1=num1, num2=num2))