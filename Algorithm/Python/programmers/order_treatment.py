def solution(emergency):
    emergency_sort = [i for i in sorted(emergency, reverse = True)]
    return [emergency_sort.index(j)+1 for j in emergency]

'''
다른 문제 풀이
'''

# def solution(emergency):
#     return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]

# emergency에서 요소를 하나씩 받아서 해당 요소들을 크기 순으로 정렬한 리스트의 차례를 구한다.
# +1을 해준 이유는 인덱스가 0부터 시작이기 때문이다.

# def solution(emergency):
#     answer = []
#     emer_ls = {e: i + 1 for i, e in enumerate(sorted(emergency)[::-1])}
#     for e in emergency:
#         answer.append(emer_ls[e])
#     return answer

# 딕셔너리 타입으로 만든 다음 키로 응급도 값을 밸류로 순번을 저장하고, 배열에 하나하나씩 넣는다.

emergency = list(map(int, input().split()))
print(solution(emergency=emergency))