# def solution(lines):
#     answer = 0
#     drow_lines = [[i for i in range(lines[j][0],lines[j][1]+1)] for j in range(3)]
    
#     print(f"drow_lines :{drow_lines}")
    
#     ol_lines = [list(set(drow_lines[0]) & set(drow_lines[1])), list(set(drow_lines[0]) & set(drow_lines[2])), list(set(drow_lines[1]) & set(drow_lines[2]))]
    
#     print(f"ol_lines1 : {ol_lines}")
    
#     ol_lines = sorted(list(dict.fromkeys(sum([i for i in ol_lines if len(i) >= 2], []))))
    
#     print(f"ol_lines2 : {ol_lines}")
    
#     if len(ol_lines) < 2:
#         return 0
#     else :
#         return len(ol_lines)-1

# [[1, 10], [2, 3], [4, 5]]와 같이 겹치는 선분이 [2, 3, 4, 5]인 경우 각각해서 길이는 2이지만 위 코드는 3을 반환함

def solution(lines):
    answer = 0
    drow_lines = [[i for i in range(lines[j][0],lines[j][1])] for j in range(3)]
    ol_lines = [list(set(drow_lines[0]) & set(drow_lines[1])), list(set(drow_lines[0]) & set(drow_lines[2])), list(set(drow_lines[1]) & set(drow_lines[2]))]
    ol_lines = sorted(list(dict.fromkeys(sum([i for i in ol_lines], []))))
    return len(ol_lines)

# 결국 못풀어서 다른 사람 풀이 참고해서 풀었다... 이런게 벽인가?
# 어차피 원소 하나를 선분의 길이 1로 보고 원소들을 집어넣기 때문에 무조건 원소가 2개 이상일 필요가 없다.
# 0레벨 치고는 어려운 문제 나중에 다시 한 번 더 풀어봐야겠다.

'''
다른 사람 풀이
'''

# def solution(lines):
#     sets = [set(range(min(l), max(l))) for l in lines]
#     return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# set(range(min(l), max(l))) for l in lines) 이 부분을 set(range(l[0], l[1]) for l in lines) 로 바꿀 수 있다.
# 여기서 의문인게 range(min(l), max(l))을 하면 선분의 끝부분의 숫자가 1 작다
# 예를 들면 [1, 10] 일 때 [1, 2, 3, 4, 5, 6, 7, 8, 9] 가 반환되며 10은 포함되지 않는다. 또한 이는 총 9개의 원소를 지니고 있다.
# 왜 이렇게 했나 추측을 하자면 range(min(l), max(l)+1)을 해서 교집합을 했을 때 원소가 1개 나오는 경우가 존재한다.
# 예를 들면 [1, 10]과 [10, 11]과 같이 교집합을 하면 공통적으로 10이 포함되므로 {10}만 나오기 때문에 이는 선분으로 볼 수 없다.
# 이러한 경우를 방지하기 위해 선분의 끝 부분은 포함하지 않았다. 또한 이것이 문제되지 않는 이유는 원소 하나당 선분 길이 1로 생각하기 떄문이다.
# 따라서 원소의 끝 - 원소의 처음이 아닌 원소의 길이를 반환한다.  

lines = [list(map(int, input().split())) for _ in range(3)]
print(solution(lines=lines))