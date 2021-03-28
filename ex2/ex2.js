teststr1 = "aaaabbbcccddeeeaaaxxx";
teststr2 = "ccccxxeeeeeeyyttmmmhhloppddty";
teststr3 = "ppppprrssrtttuvbbbkkkoollllytt";

console.log(encode(teststr1)); // a4b3c3d2e3a3x3
console.log(encode(teststr2)); // c4x2e6y2t2m3h2l1o1p2d2t1y1
console.log(encode(teststr3)); // p5r2s2r1t3u1v1b3k3o2l4y1t2

console.log(encode1(teststr1)); // a4b3c3d2e3a3x3
console.log(encode1(teststr2)); // c4x2e6y2t2m3h2l1o1p2d2t1y1
console.log(encode1(teststr3)); // p5r2s2r1t3u1v1b3k3o2l4y1t2

function encode(plainText) {

    lastLetter = plainText.charAt(0);
    occs = [];
    occs.push({
        [lastLetter]: 0
    });
    finalString = "";
      
    for (var i = 0; i < plainText.length; i++) {
        if (plainText.charAt(i) === lastLetter) {
            occs[occs.length - 1][lastLetter] += 1;
        } else {
            finalString = finalString + lastLetter + occs[occs.length - 1][lastLetter];
            lastLetter = plainText.charAt(i);
            occs.push({
                [lastLetter]: 1
            });
        }
    }
    finalString = finalString + lastLetter + occs[occs.length - 1][lastLetter];
    return finalString;
}


// code I found on the internet
function encode1(plainText){
    finalString = "";
    var s= plainText.match(/([a-zA-Z])\1*/g)||[];
    s.map(function(itm){
        finalString = finalString + itm.charAt(0) + itm.length;
    });
    return finalString;
}
