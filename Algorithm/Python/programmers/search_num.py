def solution(num, k):
    answer = 0
    num_str, k = str(num), str(k)
    index = int(num_str.find(k))
    if index != -1 :
        answer = index + 1
    else :
        answer = index
    return answer

'''
다른 사람 풀이
'''

# def solution(num, k):
#     return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1

# in, not in : 포함 연산자 
# 1. 값이 있는지 확인하는데 사용 ( 리스트, 문자열, 튜플, 딕셔너리 ) * if i in a = a에 i 요소가 존재하는지 확인
# 2. 반복문에서 요소를 빼오는데 사용 * for i in a = a에 있는 요소를 하나씩 i로 옮김

# if문 한줄 표현
# if 문 : if a is a : a = a
# if - else 문 : 결과 = _ if 조건 else _ -> a = a if a is a else b => a가 a이면 a = a이고 아니면 a = b
# if - elif - else 문 : 결과 = _ if 조건 else _ if 조건 else _ -> a = a if a is a else b if a is b else c
# => a 가 a 이면 a = a, a가 b 이면 a = b, 둘 다 아니면 a = c
num, k = map(int, input().split())
print(solution(num=num, k=k))