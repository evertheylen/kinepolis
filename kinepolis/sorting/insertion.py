
def insertionsort(l, attr):
    for i in range(1,len(l)):
        #print("i=",i)
        for j in range(0,i):
            #print("  j=",j)
            if l[i].__dict__[attr] < l[j].__dict__[attr]:
                #print("    j=",j,"i=",i)
                # these statements will shift the previously ordered elements to the right,
                tempi = l[i]
                l[j+1:i+1]=l[j:i] # shifting (actually a lot of swaps)
                l[j] = tempi
                break
        #print('             >',l)
    return l
