def solution(array):
    return sorted(array)[len(array) // 2]

array = list(map(int, input().split()))
print(solution(array=array))