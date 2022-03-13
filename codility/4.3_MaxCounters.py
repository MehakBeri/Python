'''
Question and Sol:https://app.codility.com/demo/results/trainingM92U8U-TV3/ 
'''

import unittest
class Solution:
    def max_counters(self, N, A):
        # use lazy write to get o(n+m) time complexity; space=o(n)
        # as soon as there is a max-counter command, store the value of
        # max_ctr when the command occured in variable curr_max. Now, when you receive next command-
        # check if the counter being incremented would have been affected with the previous max-counter command, if yes, then update it. once it has been updated its value will be less than equal to the value stored in curr_max
        # once all commands executed once, go over counters again to ensure there is no counter which never got updated after the last time curr_max was set due to a max-counter command
        max_ctr = 0
        curr_max = 0 #value of previous max counter op
        ctrs = [0] * N
        for i in range(len(A)):
            if A[i] >= 1 and A[i] <= N: #increase(X) op
                if ctrs[A[i] - 1] < curr_max: #lazy update
                    ctrs[A[i] - 1] = curr_max   
                ctrs[A[i]-1] += 1
                max_ctr = max(max_ctr, ctrs[A[i]-1]) 
            if A[i] == N+1: #max-counter op
                curr_max = max_ctr
        for idx,ctr in enumerate(ctrs):
            if ctr < curr_max:
                ctrs[idx] = curr_max
        return ctrs

    def max_counters_slow(self, N, A):
        # time complexity= o(n*m); space complexity= o(n)
        max_ctr = 0
        ctrs = [0] * N
        for i in range(len(A)):
            if A[i] >= 1 and A[i] <= N:
                ctrs[A[i]-1] += 1
                max_ctr = max(max_ctr, ctrs[A[i]-1])
            if A[i] == N+1:
                ctrs = [max_ctr]*N
        return ctrs

class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.max_counters(5, [3,4,4,6,1,4,4]), [3,2,2,4,2])

if __name__=="__main__":
    unittest.main()