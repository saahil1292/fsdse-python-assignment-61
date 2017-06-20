def solution(list_of_nums):
    dic1 = {'ODD': 0, 'EVEN': 0}
    for elem in list_of_nums:
        if (elem % 2 == 0):
            dic1['EVEN'] += 1
        else:
            dic1['ODD'] += 1
    return dic1
