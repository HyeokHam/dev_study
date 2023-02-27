def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i) :
            if i % j == 0 :
                answer += 1
                break
    return answer

'''
다른 사람 풀이
'''

# def solution(n):
#     output = 0
#     for i in range(4, n + 1):
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 output += 1
#                 break
#     return output

# 풀이 방식은 같지만 반복범위가 다른 풀이
# 처음 range(4, n+1) 부분은 1, 2, 3이 모두 합성수가 아니기 때문에 시작수를 4로 설정함
# 두 번째 range(2, int(i**0.5)+1)은 소수임을 판별하기 위한 범위인데 자연수의 약수는 대상의 제곱근 이하의 약수 하나와 이상의 약수 하나씩 한 쌍을 이룬다는 점을 이용한 범위이다.
# (가운데를 기준으로 대칭인 약수의 구조 이용)
# 자세한 내용은 count_ordered_pair.py 참고

# def get_divisors(n):
#     return list(filter(lambda v: n % v ==0, range(1, n+1)))
# def solution(n):
#     return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))

# 각 숫자의 약수를 모두 구해서 리스트화 하고 그 리스트의 길이를 통해 합성수를 구하는 방법


# def solution(n):
#     def is_composite_num(num):
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return True
#         return False

#     return len([x for x in range(1, n + 1) if is_composite_num(x)])

# 비슷한 풀이 방법
# 함수 안에 함수를 넣은 점이 특이해서 기록

n = int(input())
print(solution(n=n))