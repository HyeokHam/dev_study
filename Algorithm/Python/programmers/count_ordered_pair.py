def solution(n):
    return sum(1 for i in range(1, n+1) if n % i == 0)

'''
다른 사람 풀이
'''

# def solution(n):
#     return len(list(filter(lambda v: n % (v+1) == 0, range(n))))

# filter() 함수로 조건에 맞는 것 (n % (v+1))만 뽑아내서 리스트화 하고 그것의 길이를 반환

# def solution(n):
#     answer =0 
#     for i in range(n):
#         if n % (i+1) ==0:
#             answer +=1
#     return answer

# for loop를 통한 풀이 방법

# def solution(n):
#     answer = 0
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             answer+=1
#     return answer*2-1 if n**0.5==int(n**0.5) else answer*2

# 수학적 풀이 방법
# n의 약수들 중 n**0.5 이하인 것들만 구하면 나머지는 n을 그 약수들로 나누면 구할 수 있다.
# 즉 n**0.5까지의 약수들은 n의 약수의 절반이라는 결론이 나온다.
# 이때 주의할 점은 n**0.5가 정수 즉 n이 제곱수 였을 경우 n**0.5가 약수에 포함되므로 2배를 하게 되었을 경우 같은 수가 2번 나오게 된다.
# 따라서 2배 해준 값에 -1을 해줄 필요가 있다.
# 또한 이때의 시간 복잡도는 O(n**0.5)이다.

n = int(input())
print(solution(n=n))