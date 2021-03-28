def findLargest(numbers):
    if len(numbers) != 0:

        largestNumber = numbers[0]
        for number in numbers:
            if number > largestNumber:
                largestNumber = number

        return largestNumber
    else:
        return None

# doh! python doesn't actually have arrays!
arr1 = [6, 3, 8, 7, 15, 25, 33, 22, 12]
arr2 = [9, 2, 1, 5, 15, 65, 73, 12, 52]
arr3 = [0]
arr4 = []
arr5 = [-9, 2, -1, 5, 15, 65, -73, 12, 52]

#print(findLargest(arr1)) # 33
#print(findLargest(arr2)) # 73
#print(findLargest(arr3)) # 0
#print(findLargest(arr4)) # None
#print(findLargest(arr5)) # 65
