def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    my_list = L
    allsub=[]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            allsub.append(sub)
            n += 1
    newlst = allsub[:]

    # for i in allsub:
    #     check = True
    #
    #     for n in i:
    #         if n<0:
    #             check = False
    #     if check:
    #         newlst.remove(i)

    sums=[]
    for i in newlst:
        sums.append(sum(i))
    sums.sort()



    return sums[-1]

print(max_contig_sum([1,2,-3,4]))





    #
    # [3, 4, -1, 5, -4]
    # # 3 + 4 - 1 + 5 = 11
    #
    # [3, 4, -8, 15, -1, 2]
    # # 15 - 1 + 2 = 16
    #