# def solution(common):
#     answer = 0
#     plus_d = common[1]-common[0]
#     times_d = common[1]/common[0]
    
#     if common[-1]-common[-2] == plus_d:
#         answer = common[-1] + plus_d
#     else :
#         answer = common[-1]*times_d
    
#     return answer

# 공비를 구하는 과정에서 common[0]가 0이면 공비를 계산하지 못해 런타임에러 발생
# https://school.programmers.co.kr/questions/39146

def solution(common):
    answer = 0
    plus_d = common[1]-common[0] # 공차
    
    if common[-1]-common[-2] == plus_d: # 공차인지 판별
        answer = common[-1] + plus_d
    else : # 공차수열 또는 공비수열 이므로 공차수열이 아닐 경우 공비수열
        times_d = common[1]/common[0] # 공비수열일 경우 0가 나오는 경우가 없으므로 위와 같은 에러 발생 X
        answer = common[-1]*times_d
    
    return answer

common = list(map(int,input().split()))
print(solution(common = common))