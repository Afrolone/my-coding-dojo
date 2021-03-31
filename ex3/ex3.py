def closestToZero(numbers):
    ## TODO
    if numbers is None:
        return 0
    ln = len(numbers)
    if ln == 0:
        return 0
    
    closest = numbers[0]
    for number in numbers:
        if abs(number) < abs(closest):
            closest = number
        if abs(number) == abs(closest):
            if number > closest:
                closest = number
    return closest


test1 = [1,2,3,4,5,6,7,8,9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
test2 = [-3,7,5,-4,-8,-4,-2,5,6,-1,43,-3,-2]
test3 = []
test4 = None

print(closestToZero(test1))
print(closestToZero(test2))
print(closestToZero(test3))
print(closestToZero(test4))

