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
# reversed() 로 반환된 값은 리스트 이므로 ''.join()을 사용하여 문자열로 만들어줌

# def solution(my_string):
#     answer = ''
#     for c in my_string:
#         answer= c+answer
#     return answer

# for loop를 사용한 방법
# 여기서 문자열을 더하면 뒤에 붙는 것이 아닌 앞에 붙는다. (스택, 큐 같이 생각하면 편함, 사실 상 리스트의 구조가 그렇기도 하고..) 

my_string = input()
print(solution(my_string=my_string))