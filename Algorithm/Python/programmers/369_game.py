def solution(order):
    order = str(order)
    return order.count("3")+order.count("6")+order.count("9")

'''
다른 사람 풀이
'''

# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# 람다식을 잘 쓰면 이런 한 줄 코딩이 가능함..
# map(function, iterable) = 두 번째 인자로 들어온 반복 가능한 자료형을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어 수행

# def solution(order):
#     answer = len([1 for ch in str(order) if ch in "369"])
#     return answer

# in 연산자를 사용해서 369 안에 ch가 있으면 1로 list를 만듦 그것의 길이를 반환

order = int(input())
print(solution(order=order))