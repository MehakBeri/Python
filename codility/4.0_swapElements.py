'''
Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 <= ai, bi <= m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them.

Link- https://www.geeksforgeeks.org/find-a-pair-swapping-which-makes-sum-of-two-arrays-same/ (similar question), https://codility.com/media/train/2-CountingElements.pdf

Input: A[] = [4, 1, 2, 1, 1, 2], B[] = [3, 6, 3, 3]
Output: {1, 3} 
'''
from collections import Counter
import unittest

def slow_solution(A, B, m):
    '''
    The simplest method is to swap every pair of elements and calculate the
    totals. Using that approach gives us O(n^3) time complexity. A better approach is to calculate
    the sums of elements at the beginning, and check only how the totals change during the swap
    operation. time complexity= O(n^2)
    '''
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False

def fast_solution(A, B, m): #any number in A or B does not exceed m
    '''
    O(n + m): The best approach is to count the elements of array A and calculate
    the difference d between the sums of the elements of array A and B.
    For every element of array B, we assume that we will swap it with some element from
    array A. The difference d tells us the value from array A that we are interested in swapping,
    because only one value will cause the two totals to be equal. The occurrence of this value can
    be found in constant time from the array used for counting.


    let x be elem from A to be swapped with y from B to make sum equal
    sum_a - x + y = sum_b + x - y
    sum_a - sum_b = 2(x-y)
    -d = 2(x-y), where x=A[i] and y=B[j] for some i and j indexes
    the diff gotta be divisible by two. 
    '''
    n = len(A) #both A and B of same length
    sum_a = sum(A)
    sum_b = sum(B)
    d = sum_b - sum_a
    if d%2 == 1:
        return False
    d = d//2 
    count = Counter(A) #space O(m), time O(m)
    # print(count)
    for i in range(n): #time O(n)
        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0: #first condition as A[i] falls in [0,m]; second to check if elem in A in O(1)
            return True
    return False 

def medium_solution(A,B):
    '''
    make target=(sum_a - sum_b)//2 because of math in fast_solution(). then sort A and B, then traverse 
    such that if sum_a - sum_b < target then move pointer in A , else move pointer in B to a bigger number to make dif smaller
    time complexity = o(nlogn + mlogm), where n=len(A) and m=len(B)
    space compelexity = o(1)
    '''
    sum_a = sum(A)
    sum_b = sum(B)
    target = sum_a - sum_b
    if target%2 == 1:
        return False
    target = target//2 
    A.sort()
    B.sort()
    i=0
    j=0
    while i<len(A) and j<len(B):
        diff = A[i] - B[j]
        if diff == target:
            return True
        if diff < target:
            i += 1
        else:
            j += 1
    return False


class TestSolution(unittest.TestCase):

    def test_slow_solution(self):
        self.assertTrue(slow_solution([4, 1, 2, 1, 1, 2], [3, 6, 3, 3], 6), "True solution")

    def test_fast_solution(self):
        self.assertTrue(fast_solution([4, 1, 2, 1, 1, 2], [3, 6, 3, 3], 6), "True solution")

    def test_fast_solution_false(self):
        self.assertFalse(fast_solution([4, 1, 2, 1], [3, 6, 3, 3], 6), "False solution")

    def test_medium_solution(self):
        self.assertTrue(medium_solution([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]), "True solution")

if __name__ == "__main__":
    unittest.main()