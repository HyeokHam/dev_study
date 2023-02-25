from collections import deque

def solution(numbers, direction):
    queue = deque(numbers)
    if direction == "right" :
        queue.rotate(1)
    else :
        queue.rotate(-1)
    return list(queue)

# deque에 관해서는 string_push.py의 주석 참조

'''
다른 사람 풀이
'''

# def solution(numbers, direction):
#     return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]

# list slicing을 이용한 방법
# direction = 'right'이면 오른쪽으로 한 칸 밀고 끝 요소는 제일 앞으로 보내야 하므로 끝 요소만 따로 떼어내어 리스트화 한 다음 처음부터 끝 바로 전까지의 요소를 뒤에 붙인다.
# direction = 'left'이면 왼쪽으로 한 칸 밀고 처음 요소는 제일 뒤로 보내야 하므로 처음 요소만 따로 떼어내어 리스트화 한 두 번째부터 끝까지의 요소를 앞에 붙인다.

numbers = list(map(int, input().split()))
direction = input()
print(solution(numbers=numbers, direction=direction))