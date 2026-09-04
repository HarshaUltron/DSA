from typing import List
from collections import Counter

class Solution:
    def longest(self,s:str):
        left=0
        n=len(s)
        hashmap={}
        max_len=0
        for right in range(0,n):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            if hashmap[s[right]]>1:
                while hashmap[s[right]]>1:
                    max_len=max(max_len,len(hashmap))
                    hashmap[s[left]]-=1
                    if(hashmap[s[left]]==0):
                        del hashmap[s[left]]
                    left+=1
            
                
        return max_len             

df=Solution()
print(df.longest("pwwkew"))    