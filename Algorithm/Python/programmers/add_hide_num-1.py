def solution(my_string):
    return sum(int(i) for i in my_string if i.isdecimal())

'''
다른 사람 풀이
'''

# def solution(my_string):
#     return sum(int(i) for i in my_string if i.isdigit())

# 문자열에서 숫자를 판별하는 함수로는 3가지가 있다.
# 1. string.isdecimal() : 어떤 문자열이 int형으로 변환이 가능하면 True
# 2. string.digit() : 어떤 문자열이 숫자의 형태면 True
# 3. string.isnumeric() : 숫자값 표현에 해당하는 문자열이면 True
# 1번은 단지 int형만 판별하고, 2번은 숫자의 형태(예를 들어 0.2342와 같은)도 판별하고, 3번은 숫자값 표현(예를 들면 1/2와 같은)도 판별한다.
# 즉 isdecimal()의 기능이 isdigit()에 포함되어 있고 isdigit()의 기능이 isnumeric()에 포함되어 있다.

# import re

# def solution(my_string):
#     return sum(int(n) for n in re.sub('[^1-9]', '', my_string))

# 정규표현식을 사용한 풀이 방법
# [^1-9]를 풀어쓰면 ^는 문자열의 시작 및 not을 의미, []는 문자열의 집합을 의미하므로 [^1-9]는 1~9까지의 문자를 제외한 모든 문자를 의미한다.
# 또한 re.sub(pattern, new, string)는 문자열 치환메소드로 string에서 pattern에 해당하는 부분을 new로 치환하라는 의미이다.
# 따라서 위 코드의 re.sub()를 실행하면 숫자를 제외한 모든 문자를 제거할 수 있다.

# def solution(my_string):
#     answer = 0
#     for i in my_string:
#         try:
#             answer = answer + int(i)
#         except:
#             pass

#     return answer

# 원래 문자열을 int형으로 바꿀려고 하면 에러가 발생한다. (예를 들어 int(a)를 하면 에러 발생)
# 근데 여기서 예외처리로 에러가 발생하면 except 구문을 실행하기 때문에 pass 처리된다.
# 파이썬에서 pass구문은 1. 클래스, 함수에서 사용 2. 반복문, if문에서 사용 3. 예외 무시용으로 사용 된다.
# 1. 클래스. 함수에서의 사용은 내부동작은 필요 없고, 의미적으로 껍데기만 필요한 경우에 사용된다.
# 2. 반복문이나 if문에서 아무 동작을 하지 않고 넘기는 용도로 사용
# 3. 프로그램 실행 중 예외가 발생했을 때 예외를 의도적으로 무시하기 위해 사용 (예외를 넘기기 위해 사용)
# 즉 pass의 의미가 기본적으로 넘긴다기 때문에 그 의미와 하는 일이 같다고 보면된다.