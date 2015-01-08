
def mergesort(l, attr):
    #print('mergesort: got',l)
    if len(l)<=1:
        return l
    
    mid=len(l)//2
    l[:mid] = mergesort(l[:mid], attr)
    l[mid:] = mergesort(l[mid:], attr)
    
    #print('now merge',l[:mid]," and ",l[mid:])

    _merge(l, attr, l[:mid], l[mid:])
    #print('returning',l)
    return l


def _merge(thelist, attr, first, second):
    # thelist will contain the sorted (total) list. first and second are both sorted lists on their own.
    i=0
    j=0
    while i<len(first) and j<len(second):
        #print('first[i] is',first[i],' second[j] is',second[j],'  i,j=',i,j)
        if first[i].__dict__[attr] < second[j].__dict__[attr]:
            #print('   --> inserting first[i] on place ',i+j)
            thelist[i+j] = first[i]
            i+=1
        else:
            #print('   --> inserting second[j] on place ',i+j)
            thelist[i+j] = second[j]
            j+=1
    
    # fill in the rest of thelist, if needed
    if i<len(first):
        #print('filling up thelist starting from ',i+j, ' with first:',first,' but only ',first[i:])
        thelist[i+j:] = first[i:]
        
    if j<len(second):
        #print('filling up thelist starting from ',i+j, ' with second:',second,' but only ',second[j:])
        thelist[i+j:] = second[j:]
