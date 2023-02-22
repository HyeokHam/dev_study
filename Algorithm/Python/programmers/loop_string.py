# def solution(my_string, n):
#     return ''.join([i * n for i in my_string])

'''
다른 사람 풀이
'''

# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)

# 애초에 제너레이터로 반환되기 때문에 리스트 컴프리헨션을 사용할 필요가 없다.

def solution(my_string, n):
    answer = ''

    for c in my_string:
        answer += c*n
    return answer

my_string = input()
n = int(input())
print(solution(my_string=my_string, n=n))