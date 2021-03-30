test1 = [1,2,3,4,5,6,7,8,9, -1, -2, -3, -4, -5, -6, -7, -8, -9];
test2 = [-3,7,5,-4,-8,-4,-2,5,6,-1,43,-3,-2];

console.log(clozestToZero(test1)); // 1
console.log(clozestToZero(test2)); // -1

function clozestToZero(numbers) {
    if (numbers === null || numbers === 0){
        return 0;
    }

    len = numbers.length;
    clozest = numbers[(len-1)];

    while(len--){
        if(Math.abs(numbers[len]) < Math.abs(clozest)) {
            clozest = numbers[len];
        }
        if(Math.abs(numbers[len]) === Math.abs(clozest)) {
            clozest = (numbers[len] > clozest) ? numbers[len] : clozest;
        }
    }
    return clozest;
}