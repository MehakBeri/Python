'''
Ques and Solution Link- https://app.codility.com/demo/results/trainingXUHBTK-3S7/ 
'''
import unittest

def solution(X, A):
    # o(n) time complexity
    leaf_posn = set(range(1, X+1))
    for idx,i in enumerate(A):
        leaf_posn.discard(i) #does not throw err if elem missing in set
        if not leaf_posn:
            return idx 
    return -1 

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(3,[1]), -1)

    def test_2(self):
        self.assertEqual(solution(5, [1,3,1,4,2,3,5,4]), 6)

if __name__ == "__main__":
    unittest.main()