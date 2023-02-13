# def solution(array, n):
#     pre_distance = abs(array[0]-n)
#     distance = 0
#     answer = array[0]
    
#     for i in range(1, len(array)) :
#         distance = abs(array[i]-n)
#         if pre_distance > distance :
#             pre_distance = distance
#             answer = array[i]
#         elif pre_distance == distance :
#             if answer > array[i] :
#                 answer = array[i]
#     return answer

'''
다른 사람 풀이
'''

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

# lambda 사용해서 a, n을 매개변수로 받음 a를 정렬하고 정렬 기준은 (abs(x-n), x) 튜플임
# 따라서 a, n에는 튜플 (abs(x-n), x)의 0번째 요소가 들어감

array = list(map(int,input().split()))
n = int(input())
# print(solution(array=array, n=n))
print(solution(a=array, n=n))