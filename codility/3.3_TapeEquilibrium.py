# wrong with test cases: https://app.codility.com/demo/results/trainingX5X3CF-9CC/ , right: https://app.codility.com/demo/results/training5VS7K9-7GB/ 
def solution(A):
    # time o(n); space o(1)
    sum_l = A[0]
    sum_r = sum(A[1:])
    min_s = abs(sum_l - sum_r)
    for i in range(1, len(A)-1):
        sum_l += A[i]
        sum_r -= A[i]
        min_s = min(abs(sum_l - sum_r) , min_s)
    return min_s