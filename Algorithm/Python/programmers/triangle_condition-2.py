def solution(sides):
    return len([i for i in range(max(sides)-min(sides)+1, sides[0]+sides[1])])

# def solution(sides):
#     return sum(sides) - max(sides) + min(sides) - 1

# sum(sides)를 하면 두 변을 모두 더하는 값이 나온다. 알려지지 않은 변을 x라고 하자
# 먼저 max(sides)의 값이 가장 긴 변이라고 생각하면, min(sides) + x > max(sides) 이어야 한다.
# 또한 x 가 가장 긴 변이라고 생각한다면 sum(sides) > x 이어야 한다. 또한 x가 가장 긴 변이므로 max(sides) < x 인 조건을 만족하는 수를 찾아야 한다.
# 첫 번째 조건에서 부등식을 정리하면 x > max(sides) - min(sides), 두 번째 max(sides) < x < max(sides) + min(sides)(sum(sides))이다. 이 두가지 조건을 정리하면
# 부등식이 max(sides) - min(sides) < x < max(sides) + min(sides), 여기서 max(sides) < max(sides) - min(sides) 이기 때문에 생략된다. 

# def solution(sides):
#   return 2 * min(sides) - 1
# 위의 식을 조금 바꾸면 sum(sides) = max(sides) + min(sides)

# def solution(sides):
#     sides.sort()
#     L1 = len([i for i in range(1, sides[1]) if i+sides[0]>sides[1]])
#     L2 = len([i for i in range(sides[1], sides[0]+sides[1])])
#     return L1+L2

# 작은 수를 앞으로 보내기 위해서 sort()를 시행한다. 알려지지 않은 변을 x라고 하고, sides[0](min), sides[1](max)
# L1 = [i for i in range(1, sides[1]) if i+sides[0] > sides[1]]을 해석하면 sides[0](min) + 1 < x < sides[1](max) - 1 이다.
# 즉 L1은 sides[1]이 가장 긴 변일 때의 요소의 개수를 구하는 방법이다.
# L2 = [i for i in range(sides[1], sides[0]+sides[1])]을 해석하면 sides[1](max) < x < sides[0]+sides[1](min+max) 이다.
# 즉 L2는 x가 가장 긴 변일 때의 요소의 개수를 구하는 방법이다.
# L1과 L2를 더하면 모든 조건을 충족하는 요소의 개수를 구할 수 있다.

sides = list(map(int, input().split()))
print(solution(sides=sides))