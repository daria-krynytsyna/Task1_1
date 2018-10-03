

def sum_3_5(number):

    res = [x for x in range(1, number) if ((x % 3 == 0) or (x % 5 == 0))]
    #print(res)
    print(sum(res))


sum_3_5(10000000)