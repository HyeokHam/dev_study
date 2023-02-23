def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdecimal()])

'''
다른 사람 풀이
'''

# import re

# def solution(my_string):
#     return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

# 정규표현식을 사용한 풀이 방법

# def solution(my_string):
#     return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))

# filter() 함수를 사용한 풀이 방법

my_string = input()
print(solution(my_string=my_string))