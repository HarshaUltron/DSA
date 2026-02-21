# Brute Force
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxlen=0
#         for i in range(0,len(s)):
#             count=1
#             ch=s[i]
#             for j in range(i+1,len(s)):
#                 if(s[j] in ch):
#                     break
#                 else:
#                     ch=ch+s[j]
#                     count+=1
#             maxlen=max(count,maxlen)  
#             print(ch)      
#         return maxlen

# df=Solution()
# print(df.lengthOfLongestSubstring("abcabcbb"))    

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxlen = max(maxlen, right - left + 1)

        return maxlen
   
df=Solution()
print(df.lengthOfLongestSubstring("pwwkew"))        