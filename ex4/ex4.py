def reversed(k, arr):
    def revone(ar):
        ar.insert(0, ar.pop())
        return ar

    if (k < 0):
        return arr
    
    if (k == 0 or k % len(arr) == 0):
        return arr

    if (k == 1):
        return revone(arr)
    
    iterations = k % len(arr)

    for i in range(iterations):
        arr = revone(arr)
    
    return arr
