def solution(numbers):
    mul_array = []
    for i in numbers :
        numbers.remove(i)
        for j in numbers :
            mul_array.append(i*j)
    return max(mul_array)

'''
다른 사람 풀이
'''

# def solution(numbers):
#     numbers = sorted(numbers)
#     return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 

# def solution(numbers):
#     numbers.sort()
#     return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

# 두 풀이 방법은 똑같은 풀이 방법
# 정렬을 이용하여 오름차순으로 정렬한 뒤 제일 작은 두 값과 가장 큰 두 값 중 큰 수를 반환한다.
# 이유는 음수끼리 곱해졌을 경우 제일 작은 두 수를 곱한 값이 더 클 수도 있기 때문이다.

# from itertools import combinations as comb

# def solution(numbers):
#     an_list=[]
#     for i,j in comb(numbers,2):
#         an_list.append(i*j)
#     return max(an_list)

# 내가 처음 생각했던 부분, combinations 메소드를 사용해서 부분집합으로 만든 후 요소들을 곱하고 그 중 큰 값을 반환한다.

# def solution(numbers):

#      return max([k * j for i, k in enumerate(numbers) for j in numbers[i + 1:]])

# enumerate() 함수로 순서를 만들어 k 의 다음 값을 곱할 수 있게 했다.

numbers = list(map(int, input().split()))
print(solution(numbers=numbers))