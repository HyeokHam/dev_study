def solution(i, j, k):
    return ''.join(list(map(str, range(i, j+1)))).count(str(k))

'''
다른 사람 풀이
'''

# def solution(i, j, k):
#     answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
#     return answer

# 리스트 컴프리헨션을 통해 리스트화 한 다음 sum() 함수로 모두 더하는 방식

# def solution(i, j, k):
#     return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))

# 위와 똑같은 방식 단 map과 lambda 함수를 이용해서 모두 더하는 방식

i, j, k = map(int, input().split())
print(solution(i=i, j=j, k=k))