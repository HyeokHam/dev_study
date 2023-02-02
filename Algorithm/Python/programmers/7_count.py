def solution(array):
    array = str(array)
    ''.join(array)
    return array.count('7')

array = list(map(int, input().split()))
print(solution(array=array))