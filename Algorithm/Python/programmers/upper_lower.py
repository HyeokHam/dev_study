def solution(my_string):
    answer = [i.upper() if i.islower() else i.lower() for i in my_string ]
    return ''.join(answer)

'''
다른사람 풀이
'''

# def solution(my_string):
#     return my_string.swapcase()

# str.swapcase()는 소문자를 대문자로, 대문자를 소문자로 바꿔주는 메서드이다.

my_string = input()
print(solution(my_string=my_string))