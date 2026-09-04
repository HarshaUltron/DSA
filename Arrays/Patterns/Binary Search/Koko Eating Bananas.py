from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            # calculate hours needed
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                right = mid - 1  # try smaller speed
            else:
                left = mid + 1   # need more speed

        return left