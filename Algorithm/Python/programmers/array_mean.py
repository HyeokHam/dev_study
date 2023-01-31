def solution(numbers):
    return sum(numbers)/len(numbers)

'''
다른 사람 풀이
'''

# import numpy as np
# def solution(numbers):
#     return np.mean(numbers)

numbers = list(map(int, input().split()))
print(solution(numbers=numbers))

