# 438. Find All Anagrams in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

















from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        t_count = Counter(p)
        window = {}

        have = 0
        need = len(t_count)

        left = 0
        res = []

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                have += 1

            # keep window size == len(p)
            if (right - left + 1) > len(p):
                if s[left] in t_count and window[s[left]] == t_count[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1

            # check valid anagram
            if have == need:
                res.append(left)

        return res
    
from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict=Counter(p)
        s_dict={}
        res=[]
        left=0
        for right in range(0,len(s)):
            char=s[right]
            s_dict[char]=s_dict.get(char,0)+1
            while(right-left+1 > len(p)):
                s_dict[s[left]]-=1
                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]
                left+=1

            if(s_dict==p_dict):
              res.append(left)     

        return res             


            