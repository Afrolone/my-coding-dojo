def closestToZero(numbers):
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
