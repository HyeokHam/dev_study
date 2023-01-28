import re # 정규표현식 모듈

def solution(babbling):
    answer = 0
    for i in babbling :
        if re.search(r"^(aya|ye|woo|ma)+$", i): # 문자열에서 aya, ye, woo, ma가 반복해서 나오고 맨 처음과 맨 끝에 있으면
            answer += 1
            
    return answer

babbling = input().split()
print(solution(babbling=babbling))