from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count=Counter(s)
        t_count=Counter(t)

        print(t_count)
        for key in t_count:
            if(key not in s_count or t_count[key]!=s_count[key]):
                return False
        return True

df=Solution()
print(df.isAnagram(s = "anagram", t = "nagaram"))        




        