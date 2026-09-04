class Solution:
    def findPages(self, nums, m):
        n = len(nums)

        # Not enough books for every student
        if n < m:
            return -1

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left) // 2

            students = 1
            pages = 0

            for book in nums:
                if pages + book > mid:
                    students += 1
                    pages = book
                else:
                    pages += book

            if students <= m:
                # mid works, try a smaller maximum
                right = mid - 1
            else:
                # mid is too small
                left = mid + 1

        return left