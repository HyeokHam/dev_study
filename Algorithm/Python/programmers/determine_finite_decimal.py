from fractions import Fraction

def solution(a, b):
    denominator = Fraction(a, b).denominator
    prime_factor = []
    n = 2
    
    while n <= denominator  :
        if denominator % n == 0 :
            prime_factor.append(n)
            denominator = denominator / n
        else :
            n += 1
            
    for i in prime_factor :
        if i == 2 or i == 5 :
            continue
        else :
            return 2
        
    return 1

# fractions 모듈은 유리수를 계산할 때 사용하는 모듈이다. (소숫점 형태가 아닌 분수 형태의 계산)
# fractions 모듈의 Fraction(a, b)은 2개의 인자를 받아 분수로 만들어 준다.
# 여기서 a는 분자를 b는 분모를 뜻하며 자동으로 기약분수로 만들어준다.
# 또한 Fraction('a/b')와 같이 문자열로 분수를 표현한 것 또한 분수로 만들어 준다.
# 해당 모듈에서 .numerator를 통해 분자의 값을 알 수 있으며, .denominator를 통해 분모의 값을 알 수 있다.
# 또한 Fraction(1, 5) + Fraction(2, 5)와 같이 연산자를 사용해서 계산할 수 있다. 해당 결과는 Fraction(3, 5)로 반환된다.

# 위의 코드에서는 Fraction을 사용하여 기약분수로 만들고 그 분모를 저장했다.
# 이후 약수를 prime_factor에 넣고 반복문을 통해 2와 5 이외에 다른 숫자가 나오면 2를 반환하게, 성공적으로 반복문이 끝나면 1을 반환하게 했다.

'''
다른 사람 풀이
'''

# from math import gcd

# def solution(a, b):
#     b //= gcd(a,b)
#     while b%2==0:
#         b//=2
#     while b%5==0:
#         b//=5
#     return 1 if b==1 else 2

# math.gcd 함수는 들어온 숫자들의 최대 공약수(정수)를 반환한다.
# 인자가 0개 일 경우 0 반환, 모든 인자가 0일 경우도 0 반환
# 해당 코드에서 b //= gcd(a, b)는 공약수로 나누는 과정이다. 이러한 과정은 a/b를 기약분수로 만들기 위한 과정이다.
# 이후 분모인 b를 2로 나눌 수 있을 때 까지 나눈 후 5로 나눌 수 있을 때 까지 나눈다.
# 이후 b가 1이 아닌 다른 수가 있다면 이는 소인수에 2와 5 외에 다른 수가 존재한다는 의미이므로 해당 조건에 따른 유한소수가 아니다.

# def solution(a, b):
#     answer = 0
#     for i in range(2, min([a, b]) + 1):
#         while a % i == 0 and b % i == 0:
#             a = a // i
#             b = b // i
#     while b % 2 == 0:
#         b = b // 2
#     while b % 5 == 0:
#         b = b // 5
#     if b == 1:
#         answer = 1
#     else:
#         answer = 2
#     return answer

# 위와 같은 방식의 코드이다. 대신 기약분수를 구하는 과정을 gcd를 사용하지 않고 이중반복문을 통해 직접 구했다.

a, b = map(int, input().split())
print(solution(a=a, b=b))