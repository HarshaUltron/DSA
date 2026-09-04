class Solution:
    def minDaysBloom(self, nums, m, k):
        n = len(nums)

        # Impossible to make m bouquets
        if n < m * k:
            return -1

        left = min(nums)
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            bouquets = 0
            consecutive = 0

            for rose in nums:
                if rose <= mid:
                    consecutive += 1

                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0

            if bouquets >= m:
                # mid works, try fewer days
                right = mid - 1
            else:
                # mid doesn't work, need more days
                left = mid + 1

        return left