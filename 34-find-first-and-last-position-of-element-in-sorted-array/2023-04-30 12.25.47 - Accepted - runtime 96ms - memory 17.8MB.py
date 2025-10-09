class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [find_first(nums, target), find_last(nums, target)]



def find_first(A, x):
    p = 0
    r = len(A)
    while p < r:
        q = (p + r) // 2
        if x < A[q]:
            r = q
        elif x > A[q]:
            p = q + 1
        else:
            ## x == A[q]
            if p < q and A[q - 1] == A[q]:
                r = q
            else:
                return q
    return -1

def find_last(A, x):
    p = 0
    r = len(A)
    while p < r:
        q = (p + r) // 2
        if x < A[q]:
            r = q
        elif x > A[q]:
            p = q + 1
        else:
            ## x == A[q]
            if q < r - 1 and A[q + 1] == A[q]:
                p = q
            else:
                return q
    return -1

