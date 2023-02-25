def solution(age):
    num_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    age = list(map(int, str(age)))
    return ''.join([num_dict[i] for i in age])

'''
다른 사람 풀이
'''

# def solution(age):
#     conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
#             ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
#     return ''.join(conv[i] for i in str(age))

# 같은 방식의 풀이 방법
# 단, string이 이미 iterator(반복 가능한 객체)이므로 따로 리스트화 할 필요가 없다. 

# def solution(age):
#     return ''.join([chr(int(i)+97) for i in str(age)])

# 문자열 age에서 추출 된 i를 정수형으로 바꾼 다음 97('a'의 아스키(유니)코드)을 더해서 유니코드로 반환
# 참고로 'A'의 아스키(유니)코드는 65이며 'a'의 아스키(유니)코드는 97이다.

# def solution(age):
#     age = str(age)
#     age = age.replace("0", "a")
#     age = age.replace("1", "b")
#     age = age.replace("2", "c")
#     age = age.replace("3", "d")
#     age = age.replace("4", "e")
#     age = age.replace("5", "f")
#     age = age.replace("6", "g")
#     age = age.replace("7", "h")
#     age = age.replace("8", "i")
#     age = age.replace("9", "j")
#     return age

# 단순히 모든 숫자를 replace를 사용해 변환해준다.

age = int(input())
print(solution(age=age))