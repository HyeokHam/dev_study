def solution(n):
    answer = []
    for i in range(2, n+1) :
        while n % i == 0 :
            n //= i
            answer.append(i)
    return list(dict.fromkeys(answer))

'''
다른 사람 풀이
'''

# def solution(n):
#     answer = []
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             n /= d
#             if d not in answer:
#                 answer.append(d)
#         else:
#             d += 1
#     return answer

# for문을 통한 반복 대신 while문을 통해 2부터 n까지 반복을 구현함
# n이 d로 나눠 떨어질 경우 나눈 몫을 다시 n으로 함, 이후 n이 answer에 없다면 answer에 삽입
# 나누어 떨어지지 않는다면 다음 수로 나눠본다.

# import math
# from itertools import permutations

# def is_prime(n):
#     if n < 2:
#         return False
#     if n in [2, 3, 5, 7]:
#         return True

#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True


# def solution(n):
#     primes = list(filter(lambda n: is_prime(n), range(1, n+1)))

#     answer = []
#     while n != 1:
#         for prime in primes:
#             if n % prime == 0:
#                 n //= prime
#                 if prime not in answer:
#                     answer.append(prime)

#     return answer

# math.sqrt(x)는 x의 제곱근을 반환함 (반환형은 float 타입, 음수가 매개변수로 들어오면 error 발생)
# itertools는 효율적인 루핑을 위한 이터레이터를 만드는 함수들을 모아놓은 모듈이다.
# itertools.permutations()메소드는 순열을 만들어 주는 메소드이다. 예를 들어 itertools.permutations(['A', 'B', 'C'])를 실행하여 출력하면
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]과 같은 결과가 출력된다.
# 여기서는 is_prime(n)을 통해 n이 소수인지를 판별한다. 필터를 통해 함수 is_prime(n)으로 1에서 n+1까지 필터링 한 후 primes에 리스트로 생성한다.
# 이후 n이 1이 될 때까지 반복하며 리스트 primes에서 값을 하나씩 뺴온 prime으로 n을 나눈 나머지가 0이라면 n을 갱신하고, answer에 해당 숫자가 없다면 삽입한다.

n = int(input())
print(solution(n=n))