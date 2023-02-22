def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

numbers = list(map(int, input().split()))
num1, num2 = map(int, input().split())
print(solution(numbers=numbers, num1=num1, num2=num2))