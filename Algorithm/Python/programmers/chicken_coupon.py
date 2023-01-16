def solution(chicken):
    answer = 0  # service_chicken
    coupon = chicken
    
    while coupon >= 10 :
        answer += coupon // 10
        coupon = (coupon // 10) + (coupon % 10) # (coupon % 10) : remain_coupon
    return answer

chicken = int(input())
service_chicken = solution(chicken)
print(f"Service Chicken : {service_chicken}")

'''
Failure

def solution(chicken):
    chicken += 1
    coupon = chicken
    service_chicken = 0
    while coupon >= 10:
        service_chicken += coupon // 10
        remain_coupon = coupon % 10
        coupon = coupon // 10 + remain_coupon
    return service_chicken
'''
