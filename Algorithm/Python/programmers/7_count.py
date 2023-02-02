def solution(array):
    array = str(array)
    ''.join(array)
    return array.count('7')

'''
다른 사람 풀이
'''

# def solution(array):
#     return str(array).count('7')

# list를 str로 바꾸면 ''.join()을 안해도 자동으로 합쳐진다.

# def solution(array):
#     return ''.join(map(str, array)).count('7')

# 만약 ''.join()을 사용하고 싶다면 map을 통해 문자열로 바꿔주자
# map 함수는 파이썬 내장 함수로 여러 개의 데이터를 한 번에 다른 형태로 변환할 때 사용함

array = list(map(int, input().split()))
print(solution(array=array))