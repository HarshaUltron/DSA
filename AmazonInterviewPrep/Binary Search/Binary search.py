def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums




from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums=bubble_sort(nums)
        # Step 2: Binary Search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Example
obj = Solution()
print(obj.search([5, 2, 8, 1, 9], 8))

# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         nums.sort()  # O(n log n)

#         left, right = 0, len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return -1


# obj = Solution()
# print(obj.search([5, 2, 8, 1, 9], 8))