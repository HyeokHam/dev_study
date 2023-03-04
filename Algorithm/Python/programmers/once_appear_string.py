def solution(s):
    answer = ''
    for i in s :
        if s.count(i) < 2 :
            answer += i
    
    answer = ''.join(sorted(answer))
    
    return answer

'''
다른 사람 풀이
'''

# def solution(s):
#     answer = "".join(sorted([ch for ch in s if s.count(ch) == 1]))
#     return answer

# 방식은 똑같음 다만 컴프리헨션을 사용해서 코드라인을 줄임
# for ch in s -> for ch in set(s)로 사용해서 중복 조회를 줄일 수 있음

s = input()
print(solution(s=s))