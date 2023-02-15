def solution(score):
    means = [sum(i)/2 for i in score]
    means_sort = sorted(means, reverse=True)
    return [means_sort.index(i)+1 for i in means]

'''
다른 사람 풀이
'''

# def solution(score):
#     a = sorted([sum(i) for i in score], reverse = True)
#     return [a.index(sum(i))+1 for i in score]

# 짠 코드와 비슷한 코드 단, 여기서는 어차피 과목의 개수가 같으니 /2를 할 필요가 없고
# 평균을 구하지 않고 바로 index를 통해 순서를 알아냈다.
# 여기서 유의할 점은 index 함수는 중복된 값이 존재할 때 더 앞의 index를 반환한다는 것이다.

# def solution(score):
#     rank = sorted([sum(s) / 2 for s in score], reverse=True)
#     rankDict = {}
#     for i, r in enumerate(rank):
#         if r not in rankDict.keys():
#             rankDict[r] = i + 1
#     return [rankDict[sum(s) / 2] for s in score]

# 위와 같이 rank부분은 같다. 이후 enumerate를 통해 i에는 등수가 r에는 점수가 들어간다
# if문을 통해 rankDict에 점수가 키인 값이 있는지 검사 후 없다면 해당 키에 등수를 value로 넣는다.
# 이후 해당 평균 값을 키로 하는 리스트를 형성한다.
# 요약하면 dict 타입을 사용해서 점수를 키로 등수를 값으로 대입한 후 원래 평균에 맞게 등수로 리스트화 했다.

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
print(solution(score=score))