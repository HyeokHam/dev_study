from functools import reduce

def solution(numbers):
    return reduce(lambda x,y : x*y, [sorted(numbers, reverse = True)[i] for i in range(2)])

# functools.reduce 함수는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수

'''
다른 사람 풀이
'''

# def solution(numbers):
#     numbers.sort(reverse=True)
#     return numbers[0]*numbers[1]

numbers = list(map(int, input().split()))
print(solution(numbers=numbers))