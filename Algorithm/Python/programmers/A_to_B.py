def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0

# 순서를 바꿔서 만들 수 있는지의 판별은 before과 after의 모든 요소가 같아야 순서를 바꾸더라도 after를 만들 수 있다.
# 따라서 before과 after를 정렬한 것은 같아야 한다.

'''
다른 사람 풀이
'''

# def solution(before, after):
#     before = list(before)
#     for i in after:
#         try:
#             del before[before.index(i)]
#         except:
#             return 0
#     return 1

# try - except 문은 파이썬 예외처리 문으로 try영역에서 실행 도중 오류가 발생하면 except 구문을 실행하는 문장이다.
# 위의 문장은 before.index(i) 문장에서 before에 i가 존재하지 않으면 오류를 발생시키므로 except 구문을 실행한다.

before, after = input().split()
print(solution(before=before, after=after))