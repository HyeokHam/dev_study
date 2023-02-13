def solution(array, n):
    pre_distance = abs(array[0]-n)
    distance = 0
    answer = array[0]
    
    for i in range(1, len(array)) :
        distance = abs(array[i]-n)
        if pre_distance > distance :
            pre_distance = distance
            answer = array[i]
        elif pre_distance == distance :
            if answer > array[i] :
                answer = array[i]
    return answer

'''
다른 사람 풀이
'''

# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

# lambda 사용해서 a, n을 매개변수로 받음 a를 정렬하고 정렬 기준은 (abs(x-n), x)
# 여기서 정렬기준을 abs(x-n)으로만 두지 않은 이유는 abs(x-n)이 같을 경우 값이 작은 쪽이 먼저 나오도록 해야하기 때문
# 정렬기준에 따라 정렬된 순번의 0번째를 반환한다.
# 이런거 볼 때마다.. 벽 느낀다..

# def solution(array, n):
#     array.sort(key = lambda x : (abs(x-n), x-n))
#     answer = array[0]
#     return answer

# 위의 식을 풀어서 씀 단, 여기서 정렬 기준이 abs(x-n), x-n으로 되어있는데 이는 연산을 하는 것이 아닌
# 정렬 기준이므로 저 기준에 정렬될 뿐이고 값은 변하지 않는다. (위의 경우도 동일)

array = list(map(int,input().split()))
n = int(input())
print(solution(array=array, n=n))
