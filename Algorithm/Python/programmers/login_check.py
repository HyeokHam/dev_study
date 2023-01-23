import numpy as np
# def solution(id_pw, db):
    
#     answer = ''
#     db_dic = dict(db)
#     key = ''
#     id_temp = id_pw[0]
#     pw_temp = id_pw[1]
    
#     while db_dic :
#         if id_temp in db_dic :
#             if pw_temp == dict[id_temp] :
#                 answer = 'login'
#                 break
#             else :
#                 answer = 'wrong pw'
#                 break
#         else :
#             answer = 'fail'
#             break
    
#     return answer

def solution(id_pw, db):
    
    answer = ''
    db_dic = dict(db)
    key = ''
    id_temp = id_pw[0]
    pw_temp = id_pw[1]
    
    if id_temp in db_dic :
        if pw_temp == db_dic[id_temp] :
            answer = 'login'
        else :
            answer = 'wrong pw'
    else :
        answer = 'fail'
    
    return answer

db = np.array(input().split()).reshape(-1,2)
id_pw = np.array(input().split())

print(solution(id_pw=id_pw, db=db))