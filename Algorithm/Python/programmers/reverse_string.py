def solution(my_string):
    return my_string[::-1]

# 슬라이싱을 이용한 방법
# step에 -1을 줌으로써 반대방향으로 리스트를 자름

'''
다른 사람 풀이
'''

# def solution(my_string):
#     return ''.join(reversed(my_string))

# reversed() 함수를 사용한 방법
# reversed() 로 반환된 값은 reversed 객체 이므로 ''.join()을 사용하여 문자열로 만들어줌

# def solution(my_string):
#     answer = ''
#     for c in my_string:
#         answer= c+answer
#     return answer

# for loop를 사용한 방법
# c+answer 이기 때문에 문자가 뒤에 붙는 것이 아닌 앞에 붙는다.

my_string = input()
print(solution(my_string=my_string))