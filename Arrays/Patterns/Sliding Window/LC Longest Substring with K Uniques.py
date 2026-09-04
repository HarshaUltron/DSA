

# Longest Substring with K Uniques
# Difficulty: MediumAccuracy: 34.65%Submissions: 288K+Points: 4
# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1. 

# Examples:

# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.










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
        