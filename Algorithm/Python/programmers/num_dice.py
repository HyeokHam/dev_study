from functools import reduce

def solution(box, n):
    return reduce(lambda x,y : x*y, [i // n for i in box])

'''
다른 사람 풀이
'''

# import math

# def solution(box, n):
#     return math.prod(map(lambda v: v//n, box))

# math.prod는 주어진 iterable(리스트, 튜플 등 반복 가능한 자료형)에 대해 모든 요소들의 곱셈을 계산하여 반환함

# def solution(box, n):
#     return ( box[0] // n * n ) * ( box[1] // n * n ) * ( box[2] // n * n ) // ( n ** 3 )

# 상자에 넣을 수 있는 모든 주사위의 면적을 구해 주사위의 개당 면적으로 나눈 풀이 방법

box = list(map(int, input().split()))
n = int(input())
print(solution(box=box, n=n))