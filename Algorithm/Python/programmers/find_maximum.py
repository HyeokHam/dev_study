def solution(array):
    array_copy = sorted(array, reverse=True)
    return [array_copy[0], array.index(array_copy[0])]

'''
다른 사람 풀이
'''

# def solution(array):
#     return [max(array), array.index(max(array))]

# max 함수를 통해 array 자체에서 최댓값을 알 수 있음
# 단순히 최댓값만 알면 되므로 정렬하지 않아도 됨 (뻘짓했네..)

# def solution(array):
#     return sorted([[a, i] for i, a in enumerate(array)])[::-1][0]

# enumerate 함수는 리스트의 원소에 순서를 부여해주는 함수 (예시: (0, '1st'), (1, '2nd'), (3, '3nd'))
# sorted 이후 오름차순으로 정렬되어있음 따라서 제일 마지막의 0번째 원소 즉 가장 큰 값과 그 index가 저장되어있는 리스트를 반환함

array = list(map(int, input().split()))
print(solution(array=array))
