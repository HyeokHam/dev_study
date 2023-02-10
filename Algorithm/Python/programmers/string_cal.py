def solution(my_string):
    answer = 0
    oper = ""
    str_list = list(my_string.split())
    
    for i in str_list :
        if i == '+' :
            oper = "ADD"
        elif i == '-' :
            oper = "SUB"
        else :
            if oper == "ADD" :
                answer += int(i)
            elif oper == "SUB" :
                answer -= int(i)
            else :
                answer = int(i)
            
    return answer
'''
다른 풀이
'''

# def solution(my_string):
#     return eval(my_string)

# eval 함수를 사용하여 풀은 풀이

'''
다른 사람 풀이
'''

# solution=eval

# 이게 어떻게 되는건지는 모르겠지만... 극한의 줄임이다..

# def solution(my_string):
#     return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# 감산을 없애고 그냥 음수로 바꾼후 더해서 감산하는 방법 즉 '-'를 '+-' 바꾸고 '+'로 split 해서 숫자 자체를 음수로 만든 후 모두 합산
# 창의력이 대단하신것 같다.

my_string = input()
print(solution(my_string=my_string))