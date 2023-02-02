from collections import deque
# collections 모듈은 list, tuple, dict들에게 확장된 기능 제공
# 그 중 stack 과 queue 역할을 할 수 있는 deque 제공

def solution(A, B):
    answer = 0
    queue = deque(list(A)) 
    
    for i in range(len(A)) : # 문자열 끝까지 반복
        if ''.join(queue) == B : # list형인 queue를 문자열로 바꿔 검사
            break
        elif i == len(A)-1 and ''.join(queue) != B : # 끝까지 밀었는데 같지 않은 경우
            answer = -1
        else :
            answer += 1
        queue.rotate(1) # 문자열 1칸 밀기
            
    return answer

'''
다른 사람 풀이
'''

# solution=lambda a,b:(b*2).find(a)

# lambda 식 사용, b*2 의 이유는 문자열을 밀었을 때의 순환을 표현하기 위해서 -> 바뀐 문자열을 순환했을 시 본래 문자열을 찾기 위함
# find는 문자열에 존재하는 문자열의 위치를 파악
# 즉 A = apple 이고 B = eappl 일 때 B*2는 eappleappl이고 여기서 원래 문자열인 A를 찾으면 
# apple의 첫 번째 index인 a가 있는 위치 즉 1이 반환된다.

# from collections import deque

# def solution(A, B):
#     a, b = deque(A), deque(B)
#     for cnt in range(0, len(A)):
#         if a == b:
#             return cnt
#         a.rotate(1)
#     return -1

# 나 같이 번거롭게 string 변환을 하지않고 처음부터 deque로 모두 바꿔 비교했다
# return을 통해 조건을 만족하면 바로 반환하도록 했다.

A, B = input().split()
print(solution(A=A, B=B))