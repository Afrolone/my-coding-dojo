import unittest
from ex1.ex1 import findLargest
from ex2.ex2 import encode
from ex3.ex3 import closestToZero
from ex4.ex4 import reversed
from ex5.ex5 import reversePalindrome


class Testing(unittest.TestCase):

    def test_findLargest(self):
        """Linear search"""

        
        arrays = [
                    [6, 3, 8, 7, 15, 25, 33, 22, 12],
                    [9, 2, 1, 5, 15, 65, 73, 12, 52],
                    [0],
                    [],
                    [-9, 2, -1, 5, 15, 65, -73, 12, 52]
                ]
        numbers = []
        for array in arrays:
            numbers.append(findLargest(array))

        self.assertEqual(numbers, [33, 73, 0, None, 65])
    
    def test_encode(self):
        """ encode function test """
        
        strings = [
                    "aaaabbbcccddeeeaaaxxx",
                    "ccccxxeeeeeeyyttmmmhhloppddty",
                    "ppppprrssrtttuvbbbkkkoollllytt"
                ]
        results = []
        for strin in strings:
            results.append(encode(strin))
        self.assertEqual(results, [
            "a4b3c3d2e3a3x3",
            "c4x2e6y2t2m3h2l1o1p2d2t1y1",
            "p5r2s2r1t3u1v1b3k3o2l4y1t2"
        ]) 

    def test_closestToZero(self):

        values = [
            [1,2,3,4,5,6,7,8,9, -1, -2, -3, -4, -5, -6, -7, -8, -9],
            [-3,7,5,-4,-8,-4,-2,5,6,-1,43,-3,-2],
            [],
            None
        ]
        nums = []
        for value in values:
            nums.append(closestToZero(value))
        self.assertEqual(nums, [
            1,
            -1,
            0,
            0
        ]) 

    def test_reversed(self):

        arrs = [
            [0, 1, 2, 3],
            [4,7,2],
            [1,2,3],
        ]

        arrargs = [
            2,
            0,
            11
        ]

        resarrs = []

        for ar in arrs:
            resarrs.append(reversed(arrargs.pop(), ar))
        
        self.assertEqual(resarrs, [
            [1, 2, 3, 0],
            [4, 7, 2],
            [2, 3, 1]
        ])

    def test_reversePalindrome(self):

        sents = [
            "mom and dad went to eye hospital",
            "wow it is next level"
        ]

        resultSents = []

        for sent in sents:
            resultSents.append(reversePalindrome(sent))
        
        self.assertEqual(resultSents, [
            "eye and dad went to mom hospital",
            "level it is next wow"
        ])

if __name__ == '__main__':
        unittest.main()
