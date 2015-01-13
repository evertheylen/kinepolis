
def selectionsort(l, attr):
    for i in range(0,len(l)):
        smallest=i
        for j in range(i+1,len(l)):
            if l[j].__dict__[attr] < l[smallest].__dict__[attr]:
                smallest=j
        l[i], l[smallest] = l[smallest], l[i] # swap
        
        #print('             >',l)
        
    return l
