def solution(n):
    diviser  = len([n / i for i in range(1, n+1) if n % i == 0])
    if diviser % 2 == 0 :
        return 2
    else :
        return 1

# 제곱수는 약수가 홀수개 라는 특성을 이용함

'''
다른 사람 풀이
'''

# def solution(n):
#     return 1 if (n ** 0.5).is_integer() else 2

# 0.5 제곱 = 루트 (1/2 제곱) 즉 루트를 씌워서 자연수가 나온다면 제곱수이기 때문에 판별이 가능하다.

n = int(input())
print(solution(n=n))
