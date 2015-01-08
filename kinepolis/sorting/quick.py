
def quicksort(l, attr):
    if len(l) <= 1:
        return l
    
    pivot = l[0]
    smaller = []
    greater = [] # or equal
    
    for el in l[1:]:
        if el.__dict__[attr] < pivot.__dict__[attr]:
            smaller.append(el)
        else:
            greater.append(el)
    
    smaller = quicksort(smaller, attr) 
    greater = quicksort(greater, attr)
    sortedl = smaller + [pivot] + greater
    # again, replace the actual array
    for i in range(len(l)):
        l[i] = sortedl[i]
    return l
