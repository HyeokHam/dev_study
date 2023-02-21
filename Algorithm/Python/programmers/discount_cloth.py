def solution(price):
    return int(price*0.8) if price >= 500000 else int(price*0.9) if price >= 300000 else  int(price*0.95) if price >= 100000 else price

'''
다른 사람 풀이
'''

# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():
#         if price >= discount_price:
#             return int(price * discount_rate)

# dictionary 타입을 이용해 할인 받는 가격과 퍼센트를 저장하고 dict.items()를 통해 key와 value 쌍을 불러왔다.

# def solution(price):
#     if price>=500000:
#         price = price *0.8
#     elif price>=300000:
#         price = price *0.9
#     elif price>=100000:
#         price = price * 0.95
#     return int(price)

# 내 코드와 비슷한 코드.. if-elif-else 문은 내 코드 처럼 한줄로 작성하면 가독성이 좋지 않으니 실무에서는 저렇게 작성하지 말자..

price = int(input())
print(solution(price=price))