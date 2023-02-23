def solution(hp):
    answer = 0
    for i in [5, 3, 1] :
        answer += hp // i
        hp %= i
    return answer

'''
다른 사람 풀이
'''

# def solution(hp):    
#     return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

# 맞네... 생각해보니 그냥 계산해서 더하면 되는 것을.. 변수에 집어넣어야 된다고 생각했다..

hp = int(input())
print(solution(hp=hp))
