def solution(array, height):
    return sorted(array+[height], reverse = True).index(height)

# def solution(array, height):
#     array.append(height)
#     array.sort(reverse=True)
#     return array.index(height)

# def solution(array, height):
#     return sorted(array.append(height), reverse = True).index(height)

# 위 코드는 실패코드이다. 이유는 list.append()의 반환값을 고려하지 않았기 때문
# list.append()의 반환값은 list가 아닌 None이다. 따라서 위의 코드를 실행하면 오류가 발생한다.

'''
다른 사람 풀이
'''

# def solution(array, height):
#     return sum(1 for a in array if a > height)


# 해당 코드의 시간복잡도는 O(n)이다. sort의 시간 복잡도는 O(nlog n)이므로 sorting한 것보다 시간복잡도는 낮다(짧다).
# sum() 함수는 리스트의 모든 값을 더하는 함수로 알고있었는데 위의 sum()에는 리스트가 존재하지 않는 것 같아
# 1 for a in array if a > height 이 부분이 리스트로 반환이 되나 확인해보았다.
# print(type(1 for a in array if a > height)) |  출력 결과 : # <class 'generator'>
# 확인 결과 반환값이 list타입이 아닌 generator타입이다.
# 제너레이터(generator) 객체는 여러 개의 데이터를 미리 만들어 놓지 않고 필요할 때마다 즉석에서 하나씩 만들어 낼 수 있는 객체를 의미한다.
# 즉 제너레이터는 반복자(iterator)와 같은 역할을 하는 함수이다. 제너레이터는 yield 키워드를 통해 만들어 낼 수 있다.
# return 키워드와 yield 키워드의 차이점은 return 키워드는 모든 결과 값을 메모리에 올려놓아야 하는 반면, yield 키워드는 결과 값을 하나씩 메모리에 올려놓는다.

# 제너레이터와 yield 키워드는 따로 공부해서 정리가 필요할 듯 하다.
# 참고 : https://www.google.com/search?q=python+generator+object&rlz=1C5CHFA_enKR1034KR1034&sxsrf=AJOqlzUAvjb0u7QkZC_6y7SiPpgfM9kZPg:1676974551965&ei=15n0Y9i-OpDj2roPt9GriAc&start=0&sa=N&ved=2ahUKEwiYht6Dsab9AhWQsVYBHbfoCnE4HhDy0wN6BAgNEAQ&biw=855&bih=958&dpr=2


array = list(map(int, input().split()))
height = int(input())
print(solution(array=array, height=height))