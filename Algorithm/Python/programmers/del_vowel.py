import re

def solution(my_string):
    return re.sub('[aeiou]', '', my_string)

'''
다른 사람 풀이
'''

# def solution(my_string):
#     return "".join([i for i in my_string if not(i in "aeiou")])

# i가 "aeiou" 중에 없다면 리스트에 포함시키고 이후 문자열로 바꾸는 풀이 방법

# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string

# 모음들을 리스트화 해서 for loop와 replace로 모음들을 지워버리는 풀이 방법

# import re

# def solution(my_string):
#     return re.sub(r"a|e|i|o|u", "", my_string)

# 정규 표현식의 또 다른 방법 집합으로 만들지 않고 or 기능을 통해 문자열을 치환하는 풀이 방법
# 여기서 r은 raw string을 의미함 raw string이란 \를 이스케이프 문자로 보지 않고 그냥 평범한 문자로 간주해 처리하겠다는 의미
# 원래 같으면 '\'를 표현 하기 위해서는 '\\'를 작성해야하는데 r을 붙이면 '\'는 그냥 '\'로 인식함
# 주의할 점으로 정규식 함수에서 파싱할 때 raw string은 적용이 안되는 것으로 이해하는 것이 아닌 이스케이프 문자로의 치환이 일어나지 않는 것 뿐이라는 것을 주의해야 한다.

# 참고 : [[Python] 정규식의 r prefix 의미] https://velog.io/@yoopark/r-prefix-in-regexp

my_string = input()
print(solution(my_string=my_string))