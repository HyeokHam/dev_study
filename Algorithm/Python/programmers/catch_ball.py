from collections import deque
def solution(numbers, k):
    numbers = deque(numbers)
    for _ in range(k-1) :
        numbers.rotate(-2)
    return numbers[0]

'''
다른 사람 풀이
'''

# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]

# 한 번 던질 때 마다 공을 가진 사람이 두 사람 씩 이동이므로 2 * (k - 1)이라는 식이 성립
# 0 % n = 0 이므로 k = 1일 때도 성립함

# def solution(numbers, k):
#     return 2 * (k - 1) % numbers[-1] + 1

# 위와 같은 풀이방식 단 len()을 사용하지 않고 numbers의 마지막 요소의 값을 사용함, 이는 numbers의 숫자가 1부터 시작해 순서대로 올라가기 떄문에 가능
# 마지막에 +1을 넣은 이유는 k = 1일 때 0 부터 시작이기 때문에 순서를 맞춰주기 위해서임

# from collections import deque
# def solution(numbers, k):
#     array = deque(numbers)
#     array.rotate(-(k-1)*2)
#     return array[0]

# 나의 풀이와 비슷한 방식, 차이점이 있다면 반복문을 사용하지 않고 전체 lotate() 수를 구함

numbers = list(map(int, input().split()))
k = int(input())
print(solution(numbers=numbers, k=k))