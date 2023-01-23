def solution(num1, num2):
    answer = 0
    
    if num1 == num2 :
        answer = 1
    else :
        answer = -1
    return answer
num1, num2 = map(int,input().split())

print(solution(num1=num1, num2=num2))