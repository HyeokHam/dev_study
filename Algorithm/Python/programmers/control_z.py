# def solution(s):
#     number_list = s.split()
#     answer = 0
#     for i in number_list:
#         if i == 'Z':
#             del number_list[number_list.index('Z')-1]
#             del number_list[number_list.index('Z')]                 
#             print(number_list)
#     return answer

# solution(input())


def solution(s):
    number_list = s.split()
    temp_list = number_list.copy()
    list_len = len(number_list)
    answer = 0
    
    for i in range(list_len):
        if number_list[i] == 'Z':
            del temp_list[number_list.index('Z')-1:number_list.index('Z')+1]
            
    for j in temp_list:
        answer += int(j,10)
    
    return answer

a = solution(input())
print(a)
