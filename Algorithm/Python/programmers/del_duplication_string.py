def solution(my_string):
    return ''.join(list(dict.fromkeys(my_string)))


# 중복 제거 방식으로는 set 자료형을 활용하는 방법과 dict 자료형을 활용하는 방법이 있다.
# set 자료형 : set 자료형은 원소의 중복을 허락하지 않는다 다만 순서가 없는 자료형이기 때문에 원소의 순서가 중요하다면 사용하지 말자.
# dict 자료형 : dict 자료형의 key는 중복을 허락하지 않는다. 따라서 dict.fromkeys()메소드를 사용해서 key로 만들어 중복을 제거한다.
# 이 방법은 원소의 순서가 변하지 않으므로 원소의 순서를 보존하며 중복을 제거할 때 사용된다.
# 이 외에도 for 문을 사용해서 중복을 제거하는 방법이 있다.

'''
다른 사람 풀이
'''

# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))

# dict 자료형을 통한 중복 제거 방식 list로 바꿀 필요가 없음을 보여줌

# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer+=i
#     return answer

# 하나하나 꺼내서 검사하고 넣는 방식

my_string = input()
print(solution(my_string=my_string))