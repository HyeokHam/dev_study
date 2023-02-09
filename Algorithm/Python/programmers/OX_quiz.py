from collections import deque
'''
실패 목록
'''
# def solution(quiz):
#     temp = 0
#     for i in quiz :
#         stack = deque(i.split())
#         temp = stack.pop(0)
#         if temp == '+' :
#             temp += int(stack.pop(0))
#         elif temp == '-' :
#             temp -= int(stack.pop(0))
#         elif temp == '=' :
#             return ['O' if temp == int(stack.pop(0)) else 'X' ]
#         else :
#             temp += int(stack.pop(0))

# def solution(quiz):
#     temp = 0
#     for i in quiz :
#         stack = deque(i.split())
#         temp = stack.popleft()
#         if temp == '+' :
#             temp += int(stack.popleft())
#         elif temp == '-' :
#             temp -= int(stack.popleft())
#         elif temp == '=' :
#             return ['O' if temp == int(stack.popleft()) else 'X' ]
#         else :
#             temp += int(stack.popleft())

# def solution(quiz):
#     anwser = []
#     temp = 0
    
#     for i in quiz :
#         stack = list(i.split())
        
#         for _ in range(len(stack)) :
#             if stack.pop(0) == '+':
#                 temp += int(stack.pop(0))
#             elif stack.pop(0) == '-':
#                 temp -= int(stack.pop(0))
#             elif stack.pop(0) == '=':
#                 if temp == int(stack.pop(0)) :
#                     anwser.append('O')
#                 else :
#                     anwser.append('X')
#     return anwser

'''
다른 사람 풀이
'''

# def valid(equation):
#     equation = equation.replace('=', '==')
#     return eval(equation)

# def solution(equations):
#     return ["O" if valid(equation) else "X" for equation in equations]

# str.replace(변경하고싶은 문자, 변경 할 문자, 횟수(defalut = -1))는 문자열을 다른 문자열로 바꾸는 메서드이다.
# 횟수는 default가 -1로 지정되어있어 따로 지정해주지 않는 이상 문자열 전체를 다 바꾼다.
# eval(expression;식)은 문자열로 된 식을 넣으면 연산하여 반환해주는 함수이다.
# 사용성에 있어서는 매우 넓고 유용하지만 보안성에 있어서 치명적인 위험이 있다.
# eval() 함수는 표현식을 그대로 실행하는 것이기 때문에 Commend injection을 통한 해킹의 위험성이 존재한다.

def solution(quiz):
    anwser = []
    temp = 0
    store = 0
    
    for i in quiz :
        stack = list(i.split())
        
        for _ in range(len(stack)) :
            temp = stack.pop(0)
            if temp == '+' :
                store += int(stack.pop(0))
            elif temp == '-' :
                store -= int(stack.pop(0))
            elif temp == '=' :
                if store == int(stack.pop(0)) :
                    anwser.append('O')
                    break
                else :
                    anwser.append('X')
                    break
            else :
              store = int(temp)  
                
    return anwser

quiz = list(input().split(','))
print(solution(quiz=quiz))