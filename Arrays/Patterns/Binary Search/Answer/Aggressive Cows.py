class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()

        left = 1
        right = stalls[-1] - stalls[0]

        def canPlace(distance):
            cows = 1
            last = stalls[0]

            for stall in stalls[1:]:
                if stall - last >= distance:
                    cows += 1
                    last = stall

                    if cows == k:
                        return True

            return False

        while left <= right:
            mid = left + (right - left) // 2

            if canPlace(mid):
                # Distance works → try a larger distance
                left = mid + 1
            else:
                # Distance doesn't work → try smaller
                right = mid - 1

        return right