class Solution:
    def subarraysWithKDistinct(self, s: str, k: int) -> int:
        return self.atMostK(s, k) - self.atMostK(s, k - 1)

    def atMostK(self, s, k):
        count = {}
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            # key insight
            res += (right - left + 1)

        return res
    
  