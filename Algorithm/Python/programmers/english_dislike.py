def solution(numbers):
    answer = 0
    num_dic = {"zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9" }
    
    for i in num_dic :
        if numbers.find(i)+1 :
            numbers = numbers.replace(i, num_dic.get(i))
            
    answer = int(numbers)
    
    return answer

# str.find() 를 사용하면 검색하여 존재하는 index를 반환하고, 없을 시 -1을 반환하기 때문에
# False = 0, True = 1 이상인 Python에서는 나온 값에 +1을 해주어야 제대로 된 판별이 된다.

'''
다른 사람 풀이
'''

# def solution(numbers):
#     for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
#         numbers = numbers.replace(eng, str(num))
#     return int(numbers)

# enumerate를 통해 각 값의 순번이 num에 들어간다 즉 dict 자료형과 똑같은 기능을 하게 된다.

numbers = input()
print(solution(numbers=numbers))