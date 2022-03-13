'''
Question and Sol: 
'''

import unittest
class Solution:
    def missing_int(self): #pending : write test cases, fix code 
        if sum(A) < 1:
            return 1 
        n = len(A)
        for idx,i in enumerate(A): #set all negative nums & out of range to 0
            if i<0 or i>n:
                A[idx] = 0 
        for i in A: #mark idx as visited by putting a neg sign
            if i>0:
                A[i-1] = -abs(A[i-1])
        print(A)
        for idx,i in enumerate(A): #find which idx not visited
            if i>0:
                print(i)
                return i+1
        return len(A)+1

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(1,1)

if __name__=="__main__":
    unittest.main()