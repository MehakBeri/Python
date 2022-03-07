# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:38:49 2017

@author: Mehak Beri

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
"""

#codility binary gap solution

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# m = len(bin_N) = o(log(N))
# time complexity = o(m)
# space complexity = o(1)
# lc soln= https://leetcode.com/problems/binary-gap/solution/ 

def solution(N):
    # write your code in Python 3.6
    start = -1
    end = -1
    bin_N = bin(N)[2:] #o(m)
    gap = 0
    for j in range(start+1, len(bin_N)): #o(m)
        if bin_N[j] == '1':
            end = j
            gap = max(gap, end-start-1)
            start = j
    return gap
 
def main():
    print(solution(105))
    
if __name__ == '__main__':
  main()