test1 = [1,2,3,4,5,6,7,8,9, -1, -2, -3, -4, -5, -6, -7, -8, -9];
test2 = [-3,7,5,-4,-8,-4,-2,5,6,-1,43,-3,-2];
test3 = [];
test4 = null;
test5 = undefined;

console.log(clozestToZero(test1)); // 1
console.log(clozestToZero(test2)); // -1
console.log(clozestToZero(test3));
console.log(clozestToZero(test4));
console.log(clozestToZero(test5));

function clozestToZero(numbers) {
    if (numbers === null || numbers === undefined){
        return 0;
    }

    len = numbers.length;
    if (len === 0){
        return 0;
    }
    
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