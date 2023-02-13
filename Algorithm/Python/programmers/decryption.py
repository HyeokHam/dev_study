def solution(cipher, code):
    answer = ''
    for i in range(1, len(cipher)+1):
        if i % code == 0 :
            answer += cipher[i-1]
    return answer

'''
다른 사람 풀이
'''

# def solution(cipher, code):
#     answer = cipher[code-1::code]
#     return answer

# index 가 0 부터 시작이니 슬라이싱 시작을 code-1 에서 끝까지, step은 code 만큼
# 발상력의 차이... 슬라이싱은 생각했었는데..

# def solution(cipher, code):
#     answer=''
#     index=list(range(code,len(cipher)+1,code))
#     for i in index:
#         answer+=cipher[i-1]
#     return answer

# 유사한 코드 눈여결 볼 건 range의 start가 code인 것, index가 0부터 시작이므로 answer += cipher[i-1]인 것

cipher = input()
code = int(input())
print(solution(cipher=cipher, code=code))