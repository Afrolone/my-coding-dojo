
arr1 = [6, 3, 8, 7, 15, 25, 33, 22, 12];
arr2 = [9, 2, 1, 5, 15, 65, 73, 12, 52];
arr3 = [0];
arr4 = [];
arr5 = [-9, 2, -1, 5, 15, 65, -73, 12, 52];

console.log(findLargest(arr1));
console.log(findLargest(arr2));
console.log(findLargest(arr3));
console.log(findLargest(arr4));
console.log(findLargest(arr5));

function findLargest(numbers) {
    var len = numbers.length;

    if (len === 0 || len === null) {
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