from typing import List

class Solution:
    def Longest_Repeating_Character_Replacement(self,s:str,k:int)-> int :
        count={}
        left=0
        right=0
        max_len=0
        max_freq=0
        
        for right in range(0,len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])
            while ((right-left+1)-max_freq>k):
                count[s[left]]-=1
                left+=1
            max_len=max(max_len,(right-left)+1)    
        return max_len

df=Solution()
print(df.Longest_Repeating_Character_Replacement("ABAB",2))        