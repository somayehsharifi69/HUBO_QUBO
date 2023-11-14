"""
This code was designed to convert the HUBO model into the QUBO model based on formulas (13) and (14) in this paper: 
[https://www.nature.com/articles/s41598-023-36813-x]
"""

from itertools import combinations

def f_3(qqq, c, i):
    w = f'w{i}'
    q = list(qqq)
    q.append(w)
    comb = combinations(q, 2)
    variables = list(comb)
    variables.append((q[0],))
    variables.append((q[1],))
    variables.append((q[2],))
    variables.append((q[3],))
    values = [c, c, c, c, c, c, -c, -c, -c, -c]
    q_dict = dict(zip(variables, values))
    return q_dict

      
def f_4(qqqq, c, i):
    q_f = {}
    q = list(qqqq)
    qqq = q[1:]
    q = q[0]
    qq = f_3(qqq, c, i)
    for k, v in qq.items():
        k_list = list(k)
        k_list = [q] + k_list
        q_f[tuple(k_list)] = v
    q_f[(q,)] = c
    return q_f



q_2_3 = {key: value for key, value in q.items() if len(key) < 4}
i = 1
for k , v in q.items():
    if len(k) == 4:
        q_dict = f_4(k, v, i)
        for kk, vv in q_dict.items():
            if kk not in q_2_3.keys():
                q_2_3[kk] = 0
            q_2_3[kk] = q_2_3[kk] + vv
        i = i+1

q_final = {key: value for key, value in q_2_3.items() if len(key) < 3}

for k , v in q_2_3.items():
    if len(k) == 3:
        q_dict = f_3(k, v, i)
        for kk, vv in q_dict.items():
            if kk not in q_final.keys():
                q_final[kk] = 0
            q_final[kk] = q_final[kk] + vv
        i = i+1
q_final1 = {} 
for k, v in q_final.items():
    if len(k) == 1:
        k_list = list(k)
        k_list = k_list + k_list
        q_final1[tuple(k_list)] = v
    else:
        q_final1[k] = v

q_final1

"""
Converting HUBO model into QUBO model.
Input:
     dictionary of coefficients of HUBO model
Output:
     dictionary of coefficients of QUBO model.
"""