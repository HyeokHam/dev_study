def solution(s1, s2):
    answer = 0
    for i in s1 :
        if i in s2 :
            answer += 1
    return answer

'''
다른 사람 풀이
'''

# def solution(s1, s2):
#     return len(set(s1)&set(s2));

# set 자료형은 흔히 수학에서 생각하는 집합이라 생각하면 된다.
# 순서가 없고, 집합 안에서의 값은 유일하다.(예를 들어 3 같은 원소가 중복되어 3, 3이 되지 않는다.)
# 또한 튜플과 다르게 변경할 수 있는 객체이다. 내부 원소로 다양한 자료형을 동시에 가질 수 있지만, 쉽게 변경할 수 있는 (list 등) 과 같은 객체는 가질 수 없다.
# 집합의 연산에는 |(합집합), &(교집합), -(차집합), ^(대칭 차집합;합집합-교집합)이 있다
# 여기서는 s1과 s2를 집합으로 변경시켜 s1과 s2의 교집합의 길이를 반환했다.

s1 = input().split()
s2 = input().split()
print(solution(s1=s1, s2=s2))