def solution(sides):
    answer = 0
    
    sides.sort(reverse = True)
    if sides[0] < sides[1] + sides[2] :
        answer = 1
    else :
        answer = 2
    
    return answer

sides = list(map(int, input().split()))
print(solution(sides=sides))