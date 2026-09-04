class Solution:
    def longestKSubstr(self,s, k):
        count = {}
        left = 0
        max_len = -1
    
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
    
            # shrink if more than k distinct chars
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
    
            # check exactly k distinct
            if len(count) == k:
                max_len = max(max_len, right - left + 1)
    
        return max_len
        