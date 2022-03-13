'''
Ques and Sol: https://app.codility.com/demo/results/trainingAP466F-TYX/
'''

import unittest

class Solution:
    def perm_check(self, A):
        # o(n) time and space complexity 
        n = len(A)
        expected = set(range(1, n+1))
        for i in A:
            expected.discard(i)
        if not expected:
            return 1
        return 0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.perm_check([3,2,3,2]), 0) #arr with same sum as n*n+1/2 but not actually a perm

    def test_2(self):
        self.assertTrue(self.sol.perm_check([4,1,3,2]), 1)

    def test_3(self):
        self.assertTrue(self.sol.perm_check([4,1,3,2]), 1)

if __name__=="__main__":
    unittest.main()