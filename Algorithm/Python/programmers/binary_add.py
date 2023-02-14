def solution(bin1, bin2):
    return format(int(bin1, 2)+int(bin2, 2), "b")

# 기본적으로 파이썬에서 10진수 형태로 숫자를 표현, 각 진수 별로 접두어가 필요함
# 2진수 : 0b, 8진수 : 0o, 16진수 : 0x, 해당 진수를 벗어난 범위의 숫자를 사용하면 SyntaxError 뱔생
# 10진수 숫자에서 다른 진수의 문자열로 변경하는 방법은 각 진수별로 내장함수가 존재
# 2진수 : bin(), 8진수 : oct(), 16진수 : hax(), 단, 변환하면 진수에 해당하는 접두어가 붙음
# 문자열을 숫자로 바꾸기 위해서는 int(string, bias) (예를 들어 int("0x2a", 16))을 사용하면 된다. 여기서 디폴트값은 10진수 이다.
# format() 내장함수를 사용하면 다른 진수의 문자열로 바꿀 때 접두어를 제외할 수 있다.
# 2진수 : format(숫자, 'b'), 8진수 : format(숫자, 'o'), 10진수 : format(숫자, 'd'), 16진수 : format(숫자, 'x'(여기서 'X'이면 16진수를 대문자로 표현))
# 두 번째 인자 앞에 #을 붙여주면 접두어를 포함시킴

'''
다른 사람 풀이
'''

# def solution(bin1, bin2):
#     answer = bin(int(bin1,2) + int(bin2,2))[2:]
#     return answer

# 슬라이싱을 통해 앞의 0~1번째인 0b 부분을 없앰

bin1 , bin2 = input().split()
print(solution(bin1=bin1, bin2=bin2))