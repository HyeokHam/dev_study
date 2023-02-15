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

# def solution(score):
#     rank = sorted([sum(s) / 2 for s in score], reverse=True)
#     rankDict = {}
#     for i, r in enumerate(rank):
#         if r not in rankDict.keys():
#             rankDict[r] = i + 1
#     return [rankDict[sum(s) / 2] for s in score]

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
print(solution(score=score))