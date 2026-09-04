# Given an array arr[], the task is to print the subarray having maximum sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: {7, -1, 2, 3}
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

# Input: arr[] = {-2, -5, 6, -2, -3, 1, 5, -6}
# Output: {6, -2, -3, 1, 5}
# Explanation: The subarray {6, -2, -3, 1, 5} has the largest sum of 7.

from typing import List
class Solution:
    def print_subarray_with_max_sum(arr):
        max_sum = float('-inf')
        curr_sum = 0

        start = 0
        ans_start = 0
        ans_end = 0

        for i in range(len(arr)):
            if curr_sum == 0:
                start = i

            curr_sum += arr[i]

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans_start = start
                ans_end = i

            if curr_sum < 0:
                curr_sum = 0

        return arr[ans_start:ans_end + 1]       
