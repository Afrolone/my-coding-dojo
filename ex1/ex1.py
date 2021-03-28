def findLargest(numbers):
    if len(numbers) != 0:

        largestNumber = numbers[0]
        for number in numbers:
            if number > largestNumber:
                largestNumber = number

        return largestNumber
    else:
        return None
