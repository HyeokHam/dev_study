def solution(n):
    answer = [n//i for i in reversed(range(1, n+1)) if n % i == 0]
    return answer
# reversed 대신 range(n+1, 0, -1) 로 하면 똑같은 결과가 나온다.

n = int(input())
print(solution(n=n))