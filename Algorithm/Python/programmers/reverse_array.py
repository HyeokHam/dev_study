def solution(num_list):
    return num_list[::-1]

# reverse_string의 배열 버전 하지만 배열 버전이라서 신경써야할 점이 몇 가지 존재한다.

'''
다른 사람 풀이
'''

# def solution(num_list):
#     num_list.reverse()
#     answer = num_list
#     return answer

# 위 코드에서 주의할 점으로 return num_list.reverse()를 할 수 없다.
# 위 코드에서 print(num_list.reverse())를 해보면 None이 출력될 것이다.
# 이유는 list.reverse() 메소드는 단순히 리스트를 섞어줄 뿐 리스트를 따로 반환하지 않기 때문이다.

# def solution(num_list):
#     return list(reversed(num_list))

# 위 코드에서 주의할 점으로 return reversed(num_list)를 할 수 없다.
# return reversed(num_list)를 하게 되면 에러가 발생하는데 이는 reversed() 함수가 리스트를 반환하는 것이 아닌
# reversed 객체 (리스트에서는 listreverseiterator 객체)를 반환하기 때문이다.

# 참고 : [[python] reverse, reversed 차이] https://itholic.github.io/python-reverse-reversed/

num_list = list(map(int, input().split()))
print(solution(num_list=num_list))