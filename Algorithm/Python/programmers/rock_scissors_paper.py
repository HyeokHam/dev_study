def solution(rsp):
    win_dict = {'2':'0', '0':'5', '5':'2'}
    return ''.join([win_dict[i] for i in rsp])

'''
다른 사람 풀이
'''

# def solution(rsp):
#     rsp =rsp.replace('2','s')
#     rsp =rsp.replace('5','p')
#     rsp =rsp.replace('0','r')
#     rsp =rsp.replace('r','5')
#     rsp =rsp.replace('s','0')
#     rsp =rsp.replace('p','2')
#     return rsp

# string.replace()메소드를 이용한 풀이 방법
# 먼저 이기는 문자열로 바꾼 이유는 반복되는 replace()로 인해 이후의 문자열이 바뀔 수 있기 때문이다.
# 예를 들어 replace('2','0')을 한다면 이후 0을 5로 바꿀 때 바뀐 0 또한 포함되므로 먼저 대응되는 문자열로 바꾼 후 다시 숫자로 바꾼 것이다.

rsp = input()
print(solution(rsp=rsp))