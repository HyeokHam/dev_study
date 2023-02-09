def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

# 리스트 컴프리헨션 복습!

'''
다른 사람 풀이
'''

# def solution(n, numlist):
#     return list(filter(lambda v: v%n==0, numlist))

# filter()함수는 list와 같은 반복 가능한 자료형을 필터링 하는 기능을 수행함
# 여기서 필터링이란 특정 조건에 맞는 요소들만 뽑아내겠다는 의미이다.
# 즉 위의 코드는 numlist 에서 lambda 함수 : v를 n으로 나눈 나머지가 0이면 뽑아내는데 그걸 리스트화 하겠다는 의미이다.

n = int(input())
numlist = map(int,input().split())
print(solution(n=n, numlist=numlist))