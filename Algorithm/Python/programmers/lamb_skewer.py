def solution(n, k):
    return n * 12000 + (k - (n//10)) * 2000

'''
다른 사람 풀이
''' 

# def solution(n, k):
#     service = n//10
#     drink = max(0, k-service)
#     return (12000*n)+(2000*drink)

# 문제에서는 k는 n의 1/10보다 크거나 같다라고 되어있으므로 k-service가 음수가 될 수 없다.
# 다만, 이는 문제에서 따로 정의한 것이기 때문에 문제에서 내건 조건이 없었을 경우 음수가 나오는 경우가 발생한다.
# 따라서 위의 코드 drink = max(0, k-service)를 통해 k-service가 음수이면 0으로 바꿔주는 코드가 필요하다.

n, k = int(input().split())
print(solution(n=n, k=k))