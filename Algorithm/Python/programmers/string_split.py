def solution(my_str, n):
    return [my_str[n*i:n*(i+1)] for i in range((len(my_str) // n)+1) 
    if my_str[n*i:n*(i+1)] != ""]

'''
다른 사람 풀이
'''

# def solution(my_str, n):
#     return [my_str[i: i + n] for i in range(0, len(my_str), n)]

# range 도 step이 존재함 즉, range(0, 12, 6) 이면

print(list(range(0, 13, 6)))