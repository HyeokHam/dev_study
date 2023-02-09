def solution(n):
    answer = 0
    n_list = map(int, list(str(n)))
    for i in n_list :
        answer += i
    return answer

'''
다른 사람 풀이
'''

# def solution(n):
#     answer = sum(list(map(int,list(str(n)))))
#     return answer

# sum 함수를 통해 리스트에 있는 모든 요소들을 더해줌 -> 반복문 필요 X

# def solution(n):
#     return sum(int(i) for i in str(n))

# 내장 함수를 통해서 형변환 시킨 것이 아닌 반복문을 통해 형변환

# def solution(n):
#     answer = 0
#     while n:
#         n, r = divmod(n, 10)
#         answer += r
#     return answer

# divmod(x, y)함수는 x와 y를 입력받아 나눈 몫과 나머지를 튜플형태로 반환함
# 즉 divmod(x, y) = (x // y, x % y)라 할수 있음
# 한번 나눠지면 n의 값이 10으로 나눠지고 몫을 anwser에 더함, 몫이 0이 되면 반복문이 멈춤
# 1234의 계산과정의 경우 n = 123, r = 4 | n = 12, r = 3 | n = 1, r = 2 | n = 0, r = 1이 된다.

n = int(input())
print(solution(n=n))