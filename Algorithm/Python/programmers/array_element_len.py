def solution(strlist):
    answer = []
    for i in strlist :
        answer.append(len(i)) # len() = 문자열 길이 도출
    return answer

strlist = input().split()
print(solution(strlist=strlist))