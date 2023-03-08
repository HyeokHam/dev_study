import itertools 

def solution(spell, dic):
    spell_dict = [''.join(i) for i in map(list, itertools.permutations(spell))]
    for i in dic :
        if i in spell_dict :
            return 1
    return 2

# spell의 모든 조합을 구해 저장해놓은 spell_dict를 통해 푸는 방식
# 해당 방법은 테스트 케이스 2 에서 1533.72 ms, 263MB의 리소스 소모가 있다. 이유는 spell의 크기가 커지면 커질수록 조합의 개수가 기하급수적으로 늘기 때문이다.
# 따라서 해당 풀이 방법은 좋은 방법은 아닐 것으로 생각한다.

# 해당 풀이 도중 "TypeError: sequence item 0: expected str instance, list found" error가 발생했다.
# 해당 오류는 리스트에 str이 아닌 타입이 존재하면 발생하는 error이다.
# 해당 에러는 ''.join(list(map(list, itertools.permutations(spell))))로 인해 발생한다.
# list(map(list, itertools.permutations(spell))) 코드를 실행했을 경우 이차원 배열 리스트로 반환되는데
# 이차원 배열 리스트는 리스트 안에 스트링이 아닌 리스트가 들어있는 형식이므로 에러가 발생한다.
# 이를 해결하기 위해서는 반복문을 통해 이차원 배열 리스트 안의 리스트를 문자열로 만들고 다시 해당 리스트를 문장열로 만들면 된다.
# 이를 코드로 나타내면 ''.join(''.join(i) for i in list) 이런 형태가 된다.
#   
'''
다른 사람 풀이
'''

# def solution(spell, dic):
#     spell = set(spell)
#     for s in dic:
#         if not spell-set(s): (*수정* if (len(spell)==len(s)) and (not spell-set(s)))
#             return 1
#     return 2

# 집합 자료형의 특성을 이용한 풀이 방법
# spell의 집합과 s의 집합의 차집합이 비어있다면 s가 해당 원소를 모두 가지고 있다는 의미 이므로 1을 반환하며, 아니면 2를 반환한다.
# 다만 해당 풀이에서는 spell 집합에 들어있는 원소가 s 집합에 반복되어 나타나는 경우도 통과로 친다.
# 예를 들어 spell = ['s', 'q', 'l']이고 dic에 "ssqll"이 존재한다면 통과된다. 하지만 문제에서는
# "spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록"이라 하였으므로 코드의 수정이 필요하다.
# 수정은 길이비교를 통해 spell의 길이와 s의 길이가 같은 조건을 추가하면 된다. (위의 수정코드 참고)

# def solution(spell, dic):
#     spell = set(spell) 
#     for i in dic:
#         if spell.issubset(set(i)):
#             return 1 
#     return 2

# 집합 자료형의 특성을 이용한 풀이 방법 2
# 위와 동일하나 다른 집합 연산을 이용했다. 파이썬 내장함수인 A.issubset(B)는 A가 B의 부분 집합이라면 True를 반환하고, 아니면, False를 반환한다.
# 단, 해당 코드는 spell에 존재하는 요소 외에 다른 요소가 추가로 붙은 단어가 dic에 존재할 때 결과값이 "존재한다"고 나온다.

# def solution(spell, dic):
#  (+)spell = sorted(spell)
#     for d in dic:
#         if sorted(d) == sorted(spell):
#             return 1
#     return 2

# 정렬을 통해 단어들을 정렬해 동일한 단어가 존재하는지 비교하는 풀이 방법
# 매 번 정렬을 해야하기 때문에 비효율적이다. 또한 코드를 수정하여 sorted(spell)의 횟수를 한 번으로 줄일 수 있다.
# set이나 다른 모듈들을 모를 때 풀 수 있는 방법

# def is_make(word, spells):
#     for spell in spells:
#         if spell not in word:
#             return False
#     return True

# def solution(spell, dic):
#     return 1 if list(filter(lambda word: is_make(word, spell) , dic)) else 2

# is_make(word, spells)라는 검사하는 함수를 만들어 적용하는 풀이 방법
# lambda 식에서 매개변수 word는 dict에서 꺼내오고 spell은 원래 받은 spell을 사용한다.
# is_make 함수를 통해 spell에 있는 모든 문자열이 존재하는지 확인하고, 하나라도 존재하지 않는다면 False를 반환, 모두 존재한다면 True를 반환한다.
# filter 함수를 통해 is_make 함수가 False라면 2를 True라면 1을 반환한다.
# 개인적으로 가장 마음에 드는 풀이 방법

spell = list(input().split())
dic = list(input().split())
print(solution(spell=spell, dic=dic))