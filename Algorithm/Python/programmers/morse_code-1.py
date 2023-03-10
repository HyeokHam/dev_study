def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    list_letter = letter.split(' ')
    return ''.join([morse[i] for i in list_letter])

'''
다른 사람 풀이
'''

# def solution(letter):
#     morse = {
#         '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#         '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#         '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#         '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#         '-.--':'y','--..':'z'}
#     return ''.join(morse[i] for i in letter.split(' '))

# 같은 방법의 풀이지만 코드라인의 수를 압축했다.

