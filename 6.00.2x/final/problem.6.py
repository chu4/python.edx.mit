from itertools import product
import numpy as np
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    list_all_comb =list(product(range(2), repeat=len(choices)))
    choices = np.array(choices)
    
    for i in range(len(list_all_comb)):
        list_all_comb[i]=np.array(list_all_comb[i])
    
    list_all_comb_mult=list_all_comb*choices
    
    list_tup_sum_res = []
    
    for i in range(len(list_all_comb_mult)):
        list_tup_sum_res.append((sum(list_all_comb_mult[i]),list_all_comb[i]))
        


    list_res = []
    while list_res==[]:
        for i in list_tup_sum_res:
            if i[0]==total:
                list_res.append(i)
        total-=1
    list_res = sorted(list_res, key=lambda tup: sum(tup[1])) 
    return list_res[0][1]

print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3],5))
print(find_combination([1,1,1,9],4))
print(find_combination([4, 6, 3, 5, 2], 10))