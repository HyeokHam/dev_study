def solution(num, total):
    answer = []
    result_mid = total // num # 중앙값 지정
    num_mid = (num - 1) // 2 # 숫자 개수의 중간
    back_num = result_mid # 중앙값에서 -1 씩 함
    front_num = result_mid # 중앙값에서 +1 씩 함
    
    answer.append(result_mid)
    for i in range(0, num_mid):
        back_num -= 1
        answer.append(back_num)
    for j in range(num_mid+1, num):
        front_num += 1
        answer.append(front_num)
    answer.sort() # 오름차순 정렬
    
    return answer
'''
다른 사람들의 풀이
'''

# def solution(num, total):
#     return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)] # 오직 리스트 컴프리헨션과 계산만을 사용한 코드
# (total - (num * (num - 1) // 2)) // num 이 부분이 처음 시작 부분을 구하는 공식인 것 같다.

# def solution(num, total):
#     answer = []
#     var = sum(range(num+1)) 
#     diff = total - var 
#     start_num = diff//num # 위 3줄은 시작점 구하는 공식 왜 그런지는 잘 모르겠다.
#     answer = [i+1+start_num for i in range(num)] # 리스트 컴프리헨션 : 리스트 안에 for문 포함, if문도 포함가능
#     return answer


num, total = map(int,input().split())
print(solution(num=num, total=total))

