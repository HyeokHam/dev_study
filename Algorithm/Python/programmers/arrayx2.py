def solution(numbers):
    return [i*2 for i in numbers]

numbers = map(int, input().split())
print(solution(numbers=numbers))