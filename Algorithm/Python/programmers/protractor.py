def solution(angle):
    return 1 if angle < 90 else 2 if angle == 90 else 4 if angle == 180 else 3

# if문 한 줄로 쓰기 연습, 단 위와 같이 if - elif - else 문 같은 경우 한 줄로 쓰면 가독성이 안 좋다.

'''
다른 사람 풀이
'''

# def solution(angle):
#     answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
#     return answer

# ... 어 음... 발상력의 차이... 위의 식을 풀이하자면 
# 예각일 때는 90으로 나눈 몫이 존재하지 않는다 즉 (angle // 90) 이 부분이 0이다. 또한 나머지는 90보다 크게 되므로 (angle % 90 > 0) 부분이 True이므로 1이다.
# 따라서 0 * 2 + 1 * 1 이므로 예각일 떄 1이다.
# 직각일 떄는 90으로 나눈 몫이 1이고, (angle % 90 > 0)가 False 이므로 0이다. 따라서 1 * 2 + 0 * 1 이므로 2이다.
# 둔각일 때는 90으로 나눈 몫이 1이고, (angle % 90 > 0)가 True 이므로 1이다. 따라서 1 * 2 + 1 * 1 이므로 3이다.
# 평각일 때는 90으로 나눈 몫이 2이고, (angle % 90 > 0)가 False 이므로 0이다. 따라서 2 * 2 + 1 * 0 이므로 4이다.

angle = int(input())
print(solution(angle=angle))