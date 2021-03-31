# public static int[] reversed (int k, int[] arr)

def reversed(k, arr):
    def revone(ar):
        ar.insert(0, ar.pop())
        return ar

    if (k < 0):
        return 0
    
    if (k == 0 or k % len(arr) == 0):
        return arr

    if (k == 1):
        return revone(arr)
    
    iterations = k % len(arr)

    for i in range(iterations):
        arr = revone(arr)
    
    return arr

somearr = [0, 1, 2, 3]
print(reversed(11, somearr))
