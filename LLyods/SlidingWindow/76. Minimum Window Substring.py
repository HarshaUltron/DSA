# 76. Minimum Window Substring
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


from typing import List
from collections import Counter

class Solution:
    def MinimumWindowSubstring(self,s:str,t:str)->str:
        t_dict={}
        s_dict={}
        res=[-1,-1]
        res_len=float('inf')
        need=len(t_dict)
        have=0
        left=0
        for right in range(0,len(s)):
            char=s[right]
            s_dict[char]=s_dict.get(char,0)+1
            if char in t_dict and s_dict[char]==t_dict[char]:
                have+=1

            while have==need:
                if((right-left+1)<res_len):
                    res_len=right-left+1
                    res=[left,right]
                s_dict[s[left]]-=1
                if s[left] in t_dict and s_dict[s[left]]<t_dict[s[left]]:
                    have-=1

                left+=1
        l,r=res
        return s[l:r+1] if res_len != float('inf') else ""                