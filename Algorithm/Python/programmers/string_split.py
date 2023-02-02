def solution(my_str, n):
    return [my_str[n*i:n*(i+1)] for i in range((len(my_str) // n)+1) 
    if my_str[n*i:n*(i+1)] != ""]

'''
다른 사람 풀이
'''

# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]

# range 도 step이 존재함 즉, range(0, 12, 6) 이면 0 ~ 11 까지 6씩 증가하므로 0, 6에 해당된다. (7 ~ 11 까지는 6에 못미치므로 잘림)
# 또한 슬라이싱은 인덱스를 초과해도 에러가 나지 않는다.

my_string = input()
n = int(input())
print(solution(my_str=my_string, n=n))