"""
@author: Mehak Beri

Question- rotate array by k places 
Link- https://app.codility.com/demo/results/training64MKHP-T7Q/ , https://app.codility.com/demo/results/trainingHEVC6C-69W/ 
Solutions - https://www.geeksforgeeks.org/array-rotation/ 
"""

def solution(A, K):
    # write your code in Python 3.6

    # todo: time = o(len(A)) and const space
    # Euclid’s Algorithm: It is an efficient method for finding the GCD(Greatest  Common Divisor) of two integers. The time complexity of this algorithm is O(log(min(a, b))
    # juggling algorithm linear solution- https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm 
    n = len(A)
    if K==0 or K==n or n<=1 or (K>n and K%n==0): #elem at original position
        return A
    k = K%n
    d = n-k #for right rotation replace k by n-k
    for i in range(gcd(n,k)):
        curr_i = i
        tmp = A[i] #first in section
        while True:
            nxt_i = curr_i + d
            if nxt_i >= n :
                nxt_i = nxt_i - n
            if nxt_i == i : #back to original
                break 
            A[curr_i] = A[nxt_i]
            curr_i = nxt_i
        A[curr_i] = tmp 
    return A 

def gcd(n,k):
    if k==0:
        return n
    return gcd(k, n%k)


    # time = o(len(A)*K)
    # space = o(1)
    # n = len(A)
    # if K==0 or K==n or n<=1 or (K>n and K%n==0): #elem at original position
    #     return A
    # k = K%n
    # for i in range(k): #o(k)
    #     tmp = A.pop()
    #     A.insert(0, tmp) #o(n)
    # return A

    ###########
    # time = o(len(A))
    # space = o(len(A))
    ##########
    # b = [i for i in A] #copy A
    # for idx,e in enumerate(A):
    #     new_idx = (idx + K)%n
    #     b[new_idx] = e 
    # return b 

