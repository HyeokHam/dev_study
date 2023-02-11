def solution(numbers):
    answer = 0
    num_dic = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9" }
    
    for i in num_dic :
        if numbers.find(i) :
            numbers = numbers.replace(i, num_dic.get(i))
    print(numbers)
    
    return answer

numbers = input()
print(solution(numbers=numbers))