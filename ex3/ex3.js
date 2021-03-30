test1 = [1,2,3,4,5,6,7,8,9, -1, -2, -3, -4, -5, -6, -7, -8, -9];
test2 = [-3,7,5,-4,-8,-4,-2,5,6,-1,43,-3,-2];
test3 = [];
test4 = null;
test5 = undefined;

console.log(closestToZero(test1)); // 1
console.log(closestToZero(test2)); // -1
console.log(closestToZero(test3));
console.log(closestToZero(test4));
console.log(closestToZero(test5));

function closestToZero(numbers) {
    if (numbers === null || numbers === undefined){
        return 0;
    }

    len = numbers.length;
    if (len === 0){
        return 0;
    }

    closest = numbers[(len-1)];

    while(len--){
        if(Math.abs(numbers[len]) < Math.abs(closest)) {
            closest = numbers[len];
        }
        if(Math.abs(numbers[len]) === Math.abs(closest)) {
            closest = (numbers[len] > closest) ? numbers[len] : closest;
        }
    }
    return closest;
}