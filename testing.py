import unittest
from first.first import findLargest

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
        


if __name__ == '__main__':
        unittest.main()
