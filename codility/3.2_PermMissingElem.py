
#linear solution- https://www.geeksforgeeks.org/find-the-missing-number/ 
#https://app.codility.com/demo/results/trainingT5ZHU4-DBE/ 
def solution(A):
    # o(nlogn)
    n = len(A)
    A.sort()
    for i in range(n):
        if A[i]!=i+1:
            return i+1
    return n+1