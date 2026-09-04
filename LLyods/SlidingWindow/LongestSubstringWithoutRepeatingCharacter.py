class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        max_len=0
        cnt=set()
        for right in range(0,len(s)):
            while s[right] in cnt:
                cnt.remove(s[left])
                left+=1
            cnt.add(s[right])
            max_len=max(max_len,(right-left)+1)
        return max_len if max_len > 0 else 0    
        