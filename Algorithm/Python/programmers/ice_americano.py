def solution(money):
    return divmod(money, 5500)

'''
다른 풀이
'''

# def solution(money):
#     return [money // 5500, money % 5500]

money = int(input())
print(solution(money=money))