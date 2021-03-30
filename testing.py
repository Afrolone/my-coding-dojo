import unittest
from ex1.ex1 import findLargest
from ex2.ex2 import encode

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

if __name__ == '__main__':
        unittest.main()
