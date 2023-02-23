n = int(input())

for i in range(1, n+1) :
    print('*'*i)

'''
다른 사람 풀이
'''

# print('\n'.join('*' * (i + 1) for i in range(int(input()))))
# '구분자'.join은 리스트에 있는 요소들을 합쳐 구분자를 더해 합쳐 하나의 문자열로 만들어 주는 역할을 함
# 여기서 '*' * (i + 1) for i in range(int(input())) 이 부분에서 ['*', '**', '***',...]와 같은 리스트가 형성됨
# 이러한 리스트를 '\n'을 구분자 삼아 문자열로 만들어 줌

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(i):
#         print('*', end = '')
#     print()

# 흔히 우리가 생각하는 다른 언어에서의 별찍기
# 이중 for loop를 이용해서 해결하는 풀이 방법