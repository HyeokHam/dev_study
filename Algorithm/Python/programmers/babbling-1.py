import re # 정규표현식 모듈

def solution(babbling):
    answer = 0
    for i in babbling :
        if re.search(r"^(aya|ye|woo|ma)+$", i): # 문자열에서 aya, ye, woo, ma가 반복해서 나오고 맨 처음과 맨 끝에 있으면
            answer += 1
            
    return answer

# 정규표현식도 따로 공부해서 정리 해야할 필요가 있음
# 나중에 다른 사람 풀이도 확인해서 정리 해놓자...

babbling = input().split()
print(solution(babbling=babbling))