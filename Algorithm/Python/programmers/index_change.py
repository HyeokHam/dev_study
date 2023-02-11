def solution(my_string, num1, num2):
    my_string = list(my_string)
    
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    
    answer = ''.join(my_string)
    
    return answer

my_string = input()
num1, num2 = map(int, input().split())
print(solution(my_string=my_string, num1=num1, num2=num2))