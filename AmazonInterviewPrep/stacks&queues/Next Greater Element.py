from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        next_greater = {}

        # process nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # remaining elements → no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # build answer
        return [next_greater[num] for num in nums1]