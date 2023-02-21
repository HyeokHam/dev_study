def solution(num_list):
    j, k = 0, 0
    for i in num_list :
        if i % 2 == 0 :
            j += 1
        else :
            k += 1
    return [j, k]

'''
다른 사람 풀이
'''

# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer

# 나머지를 인덱스로 사용함. 이것이 가능한 이유는 홀수이면 2로 나눴을 때 나머지가 1이고 짝수이면 0이기 때문

# def solution(num_list):
#     div_num_list = list(map(lambda v: v % 2, num_list))
#     return [div_num_list.count(0), div_num_list.count(1)]

# lambda식을 통해 num_list의 각 숫자를 2로 나눈 나머지를 리스트로 만들어 (짝[0],홀[1])
# 해당 리스트의 0과 1의 개수로 문제를 해결했다.


num_list = list(map(int, input().split()))
print(solution(num_list=num_list))