def solution(n):
    return [i for i in range(1, n+1) if i % 2 != 0]

'''
다른 사람 풀이
'''

# def solution(n):
#     return [x for x in range(n + 1) if x % 2]

# True = 1, False = 0 이기 때문에 따로 추가 조건을 주지 않아도 x % 2 만으로 판별 가능

# def solution(n):
#     return [i for i in range(1, n+1, 2)]

# 짝, 홀이 반복되어 나오기 때문에 가능한 코드
# step = 2 이기 때문에 1부터 시작해 3, 5, 7 ... 이런 식으로 반환한다.
# 사실 상 짝수인지 홀수인지는 판별하지 않고 값을 반환함

n = int(input())
print(solution(n=n))