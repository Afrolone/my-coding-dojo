function reverse(arr, k) {
    function revone(ar){
        ar.unshift(ar.pop());
        return ar;
    }

    if (k < 0) {
        return arr;
    }

    if (k === 0 || k % arr.length === 0) {
        return arr
    }

    if (k === 1) {
        return revone(arr)
    }

    var iterations = k % arr.length
    
    for(i = 0; i < iterations; i++){
        arr = revone(arr)
    }
    return arr;
}

somearr = [0, 1, 2, 3];
somearr1 = [4,7,2];
somearr2 = [1,2,3];

console.log(reverse(somearr, 1));
console.log(reverse(somearr1, 2));
console.log(reverse(somearr2, 0));