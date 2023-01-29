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

num, total = map(int,input().split())
print(solution(num=num, total=total))