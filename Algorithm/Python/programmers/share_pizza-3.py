def solution(slice, n):
    return (n - 1) // slice + 1

# def solution(slice, n):
#     return (n + (slice-1)) // slice

# share_pizza-1 문제와 똑같은 풀이 대신 피자조각의 개수를 따로 입력할 수 있게 했다.
# 하지만 상수에서 변수로 바뀌었을 뿐 풀이 방법은 달라지지 않았으니 share_pizza-1과 방식은 똑같다.

slice, n = map(int, input().split())
print(solution(slice=slice, n=n))