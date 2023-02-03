def solution(n, t):
    answer = 0
    
    for _ in range(0, t) :
        n *= 2
    answer = n

    return answer

'''
다른 사람 풀이
'''

# def solution(n, t):
#     return n << t

# 왼쪽 비트 시프트를 하면 *2의 효과가 나고, 오른쪽 비트 시프트를 하면 /2의 효과가 난다.

# def solution(n, t):
#     return n*(2**t)

n, t = map(int, input().split())
print(solution(n=n, t=t))