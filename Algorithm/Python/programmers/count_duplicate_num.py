def solution(array, n):
    return array.count(n)

array = list(map(int, input().split()))
n = int(input())
print(solution(array=array, n=n))