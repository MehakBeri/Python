"""
@author: Mehak Beri

Question- odd occurences in array
Link- https://app.codility.com/demo/results/training6HXJVA-4RP/
Solution explanation - https://leetcode.com/problems/single-number/discuss/1771720/C%2B%2B-EASY-SOLUTIONS-(SORTING-XOR-MAPS-(OR-FREQUENCY-ARRAY))
"""

def solution(A): #time= o(n), space=o(1)
    # write your code in Python 3.6
    v = A[0]
    for i in range(1,len(A)):
        v = v^A[i]
    return v