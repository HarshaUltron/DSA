# Given an array and a number k, find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times. 

# Examples : 

# Input  : arr[] = {-1, 10, 20}, k = 2
# Output : 59
# After concatenating array twice, we get {-1, 10, 20, -1, 10, 20} which has maximum subarray sum as 59.

# Input  : arr[] = {-1, -2, -3}, k = 3
# Output : -1

from typing import List
def Maxsubarraysumwithrepeatedconcatenations(arr:list[int], k : int):
    m_sum=float('-inf')
    curr_sum=0
    for p in range(0,k):
        for i in range(0,len(arr)):
            curr_sum+=arr[i]
            m_sum=max(m_sum,curr_sum)
            if(curr_sum<0):
                curr_sum=0

    return m_sum        

# Optimal
def kadane(arr):
    curr = arr[0]
    best = arr[0]

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        best = max(best, curr)

    return best


def max_subarray_k_concat(arr, k):
    if k == 1:
        return kadane(arr)

    total_sum = sum(arr)

    prefix_max = float('-inf')
    s = 0
    for x in arr:
        s += x
        prefix_max = max(prefix_max, s)

    suffix_max = float('-inf')
    s = 0
    for i in range(len(arr)-1, -1, -1):
        s += arr[i]
        suffix_max = max(suffix_max, s)

    if total_sum > 0:
        return suffix_max + prefix_max + (k-2)*total_sum
    else:
        return max(
            kadane(arr),
            suffix_max + prefix_max
        )