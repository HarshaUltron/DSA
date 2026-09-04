class Solution:
    def longestKSubstr(self, s, k):
        count={}
        left=0
        right=0
        max_len=0
        for right in range(0,len(s)):
            count[s[right]]=count.get(s[right],0)+1
            while len(count)>k:
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
            if(len(count)==k):
             max_len=max(max_len,(right-left)+1)
        return max_len if max_len>0 else -1
        
        