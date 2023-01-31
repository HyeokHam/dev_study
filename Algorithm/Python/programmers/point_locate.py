def solution(dot):
    answer = 0
    
    if dot[0] > 0 and dot[1] > 0 :
        answer = 1
    elif dot[0] < 0 and dot[1] > 0 :
        answer = 2
    elif dot[0] < 0 and dot[1] < 0 :
        answer = 3
    else :
        answer = 4
    # elif dot[0] > 0 and dot[1] < 0 :
    #   answer = 4
    # else :
    #   answer = -1 # x 축과 y 축에 위에 있는 점은 -1 처리
    return answer

# python 에는 &&, || 대신 and, or로 사용
# & = Binary AND, | = Binary OR, ^ = Binary XOR

'''
다른 사람 풀이
'''
# def solution(dot):
#     quad = [(3,2),(4,1)]
#     return quad[dot[0] > 0][dot[1] > 0]

# list 안에 튜플 추가 가능 | 튜플 : list와 거의 동일하나 한번 넣은 요소를 변경할 수 없다.
# 사실상 quad는 이중리스트로 봐도 무방
# dot[0] > 0, dot[1] > 0 부분에서 True = 1, False = 0로 값이 도출
# 따라서 [1(양수)][1(양수)]은 quad의 두 번째 요소의 두 번째 요소를 가르키므로 1이 결과로 나온다.
# 나머지도 이하 동일하다. 

# def solution(dot):
#     a, b = 1, 0
#     if dot[0]*dot[1] > 0:
#         b = 1
#     if dot[1] < 0:
#         a = 2
#     return 2*a-b

# 이건 어떻게 이렇게 생각한건지 미스터리하다. 수학적으로 푼 것 같은데 모르겠다.

dot = list(map(int, input().split()))
print(solution(dot=dot))