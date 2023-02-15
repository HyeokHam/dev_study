def solution(numlist, n):
    return sorted(numlist, key = lambda numlist : (abs(numlist-n), -numlist))

# (abs(numlist-n), -numlist)이 부분에서 두 번째 원소가 numlist가 아니라 -numlist인 이유는
# 전제 정렬이 오름차순이기 때문에 더 큰 수를 먼저 정렬해야하는 두 번째 요소는 오름차순이 아닌 내림차순이 되어야 한다
# 여기서 - 를 붙여줌으로 두 번째 요소는 내림차순으로 정렬되는 효과를 낸다.

numlist = list(map(int, input().split()))
n = int(input())
print(solution(numlist=numlist, n=n))