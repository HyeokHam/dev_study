def solution(str1, str2):
    return 1 if str1.find(str2) != -1 else 2

'''
다른 사람 풀이
'''

# def solution(str1, str2):
#     return 1 if str2 in str1 else 2

# str.find()로 굳이 안찾아도 됨...

# def solution(str1, str2):
#     return 1 + int(str2 not in str1)

# 기본이 1이고 없을 때 +1 을 추가로 해줘 2를 만드는 방식
# int(True) = 1, int(False) = 0 따라서 있으면 +0, 없으면 +1 

str1, str2 = input().split()
print(solution(str1=str1, str2=str2))