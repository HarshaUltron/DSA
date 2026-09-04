class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1

            # skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    
df=Solution()
print(df.isPalindrome("A man, a plan, a canal: Panama"))

#Brute Force
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            #print(ch.isalnum())
            if ch.isalnum():
                
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]

df=Solution()
print(df.isPalindrome("A man, a plan, a canal: Panama"))

# Time Complexity

# Traversing string → O(n)

# Reversing string → O(n)

# ✅ Overall TC
# 𝑂
# (
# 𝑛
# )
# O(n)
# 	​

# 🧠 Space Complexity

# New string cleaned → O(n)

# Reversed string → O(n)

# ✅ Overall SC
# 𝑂
# (
# 𝑛
# )
# O(n)
# 	​

