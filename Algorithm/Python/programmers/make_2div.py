def solution(num_list, n):
    return [num_list[i:i+n] for i in range(0, len(num_list), n)]

'''
다른 사람 풀이
'''

# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):
#         answer.append(num_list[i:i+n])
#     return answer

# step을 n으로 설정해서 슬라이싱을 실행해 하는 풀이방법
# n이 2라고 생각하면 step이 2이므로 [0:2] [2:4] ... 이런식으로 슬라이싱 된다.
# n이 3이라고 생각하면 step이 3이므로 [0:3] [3:6] ... 이런식으로 슬라이싱 된다.

# import numpy as np
# def solution(num_list, n):
#     li = np.array(num_list).reshape(-1,n)
#     return li.tolist()

# numpy 모듈을 사용한 풀이방법
# reshape(row(행), col(열))을 메소드를 통해 array이를 재배열해 리스트화 시키는 풀이방법
# 여기서 '-1'이라는 의미는 변경된 배열의 '-1' 위치의 차원은 "원래 배열의 길이와 남는 차원으로 부터 추정" 된다는 의미이다.
# 즉 reshape(-1, n)은 열의 개수에 맞게 행을 맞춰준다. n이 2이면 [[1, 2],[3, 4],[5, 6]...]식의 2열에 맞게 행이 맞춰진다.
# 또한 매개변수의 개수는 차원의 수가 된다. 즉 reshape(a, b, c)이면 3차원 배열이 형성된다.

# def solution(num_list, n):
#     answer = []
#     for i in range(len(num_list)//n) :
#         answer.append(num_list[i*n:(i+1)*n])
#     return answer

# 첫 번째 풀이에서의 step을 단순한 나눗셈으로 표현한 방법
# step은 단순히 순번을 뛰어넘기 때문에 step의 반복횟수는 len(num_list)//n이 된다.
# num_list[i*n:(i+1)*n] 또한 순번을 뛰어넘는 것을 수식으로 표현해 슬라이싱 한 것이다.
# i가 0일 때, num_list[0:1*n], i가 1일 때, num_list[1*n:2*n]

num_list = list(map(int, input().split()))
n = int(input())
print(solution(num_list=num_list, n=n))