def solution(n):
    return sum([i for i in range(0, n+1, 2)])

'''
다른 사람 풀이
'''

# def solution(n):
#     return sum(range(0, n+1, 2))

# 굳이 반복문과 리스트컴프리헨션을 통해 리스트를 만들지 않아도 됨

# def solution(n):
#     return sum([i for i in range(2, n + 1, 2)])

# 어차피 짝수만 더하기 때문에 0부터 시작할 필요가 없음

# def solution(n):
#     return 2*(n//2)*((n//2)+1)/2

# 어...음... 수학적인 풀이 방법
# n이 10일 때 2*(10//2)*((10//2)+1)/2 이다. 계산하면 30이다.
# n이 11일 떄 2*(11//2)*((11//2)+1)/2 이다. 계산하면 2로 안나눠 떨어지기 때문에 똑같이 30이다.
# 등차수열을 이용해서 짝수의 합 공식을 사용하면 N(N+1)이다. 여기서 N은 짝수의 개수이므로 짝수의 개수를 알기 위해서는 (n//2)가 필요하다.
# 앞에 2* 와 맨 귀의 /2는 왜 한건지 잘 모르겠다.(아마 공식 그대로 사용해서 그런듯) 테스트해봤을 때는 (n//2)*((n//2)+1)로 해도 문제없이 돌아간다.

n = int(input())
print(solution(solution(n=n)))