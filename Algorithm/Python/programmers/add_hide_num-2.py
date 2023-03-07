import re

def solution(my_string):
    return sum(map(int, re.findall(r'\d+', my_string)))

'''
다른 사람 풀이
'''

# def solution(my_string):
#     s = ''.join(i if i.isdigit() else ' ' for i in my_string)
#     return sum(int(i) for i in s.split())
