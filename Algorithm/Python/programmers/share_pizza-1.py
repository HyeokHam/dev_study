import math

def solution(n):
    return math.ceil(n/7)

# math 모듈에는 수학에 관련된 많은 함수들이 존재하는데 이 중 내림, 올림 관련된 함수 또한 존재한다.
# 올림 함수는 math.ceil(num)이 있다.
# 내림 함수는 math.floor(num)이 있다.
# 버림 함수는 math.trunc(num)이 있다. 이떄 내림과 버림의 차이는 내림은 소숫점을 없애고 숫자를 하나 내리지만(무조건 아래로 향한다.), 버림은 소수점을 없애기만 한다.(내림을 하더라도 0으로 향한다.)
# 즉 버림 함수 math.trunc(num)은 int(num)과 같은 역할을 한다.
# 반올림 함수는 math 모듈이 아닌 파이썬에 내장된 round(num, 자릿수[default = 0 / 이는 소수 첫째 자리에서 반올림이다.])
# 이때 반올림 함수는 사사오입 원칙을 따른다. 사사오입 원칙은 반올림 대상의 값이 5일 때 앞자리 숫자가 홀수면 올림하고, 짝수면 내림한다.

'''
다른 사람 풀이
'''

# def solution(n):
#     return (n - 1) // 7 + 1

# 수학적인 풀이 방법.. n이 8보다 작으면 n-1 // 7은 0이다. n이 8을 넘어가는 순간 n-1 // 7은 1이 된다.
# 즉 8의 배수만큼 몫이 늘어난다. 이는 문제에서 7명까지는 1판 8명부터 2판 이므로 이를 반영한 것이다.
# 사람 수가 적든 많든 1판은 무조건 있어야 하기 때문에 +1을 해준다.

# def solution(n):
#     answer = 0
#     return (n+6) // 7

# 이 풀이도 위의 풀이와 비슷하다. n이 1이면 n+6이 7이므로 몫이 1이다. n이 8이면 n+6이 14이므로 몫이 2이다.
# 즉 몫을 맞춰준 것이라 생각하면 된다. 1~13까지는 몫이 1이어야 하므로 1 일때 +6을 해줘서 7로 맞춰준 것이다.

# def solution(n):
#     return -(-n//7)

# 해괴한 문제풀이...
# 음수로 나눗셈을 하면 몫에 대해서 내림을 사용한다. 즉 소숫점이 존재한다면 무조건 -1을 한다는 소리이다.
# 이 법칙을 통해서 -n//7로 내림을 시행하고 이후 -를 붙혀 원래 수로 복구하는 방법이다.
# 단 이는 다른 언어에서 호환되지 않을 수 있는데, 이유는 몫에 대한 계산 방법이 다르기 때문이다.
# 예를 들어 C언어는 몫에 대해 버림을 시행하여 -3.999의 값이 -3으로 되지만, 파이썬의 경우 내림을 시행하여 -3.999의 값이 -4가 된다.

# 참고: [C와 Python의 음수 나머지 연산 방법의 차이] https://lecor.tistory.com/16

n = int(input())
print(solution(n=n))