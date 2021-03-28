
arr1 = [6, 3, 8, 7, 15, 25, 33, 22, 12];
arr2 = [9, 2, 1, 5, 15, 65, 73, 12, 52];
arr3 = [0];
arr4 = [];
arr5 = [-9, 2, -1, 5, 15, 65, -73, 12, 52];


console.log(findLargest(arr1)); // 33
console.log(findLargest(arr2)); // 73
console.log(findLargest(arr3)); // 0
console.log(findLargest(arr4)); // undefined
console.log(findLargest(arr5)); // 65 


function findLargest(numbers) {
    var len = numbers.length;

    console.log(len)

    if (len === 0) {
        return;
    }

    var largest = numbers[0]

    while (len--) {
        if(numbers[len] > largest) {
            largest = numbers[len]
        }
    }
    return largest
}