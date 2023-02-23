def solution(my_string, letter):
    return my_string.replace(letter, '')


'''
다른 사람 풀이
'''

# def solution(my_string, letter):
#     answer = ''
#     for string in my_string:
#         if string != letter:
#             answer += string
#     return answer

# for loop를 통한 풀이 방법
# letter가 아닐때만 answer에 추가해 삭제와 같은 기능을 한다.

# def solution(my_string, letter):
#     my_string = list(my_string)
#     while letter in my_string:
#         my_string.remove(letter)
#     return "".join(my_string)

# list.remove() 메소드를 이용한 방법
# remove() 메소드는 하나의 문자만 제거하기 때문에 여러개의 문자를 삭제해야 할 때는 반복이 필요하다.

my_string, letter = input().split()
print(solution(my_string=my_string, letter=letter))