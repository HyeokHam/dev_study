def solution(my_string):
    answer = ''.join(sorted(my_string.lower()))
    return answer

# sorted 함수는 정렬된 새로운 리스트를 return 하고 원본에는 영향을 주지 않음,
# sort 메소드는 원본을 정렬하고 return이 없음 또한 list.sort()로 존재함 따라서 string에는 사용 불가
# join 함수는 구분자.join(리스트)로 사용하며 리스트에 존재하는 원소를 구분자를 넣어 문자열로 합쳐줌

my_string = input()
print(solution(my_string=my_string))