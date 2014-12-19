
def bubblesort(l, attr):
    print("buuble", l)
    for maxloc in range(len(l),1,-1): # the '-1' makes this range go reversed
        for i in range(1,maxloc): # skipping first element in range, but it is evaluated in l[i-1]
            if l[i-1].__dict__[attr] > l[i].__dict__[attr]:
                l[i-1], l[i] = l[i], l[i-1] # swap
        # print('             >',l)
    print("buuble", l)
    return l