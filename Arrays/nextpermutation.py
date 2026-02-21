# 💡 Problem Definition

# Given a list of numbers nums, find the next lexicographically greater permutation of the numbers.

# If no such permutation exists (i.e., it’s the largest possible), rearrange into the lowest (sorted ascending) order.

# Example:

# Input:  [1, 2, 3]
# Output: [1, 3, 2]

# Input:  [3, 2, 1]
# Output: [1, 2, 3]

# 🪓 1. Brute Force (O(n! × n))
# 🔹 Idea

# Generate all permutations,
# sort them lexicographically,
# and find the next one after the given nums.

# 🔹 Code
from itertools import permutations

def nextPermutation(nums):
    perms = sorted(list(permutations(nums)))
    for i in range(len(perms)):
        if list(perms[i]) == nums:
            if i + 1 < len(perms):
                return list(perms[i + 1])
            else:
                return list(perms[0])  # last permutation → smallest

# ⚙️ Complexity
# Metric	Value
# Time	O(n! × n)
# Space	O(n! × n)

# Totally impractical except for very small n (like ≤ 6).

# ⚙️ 2. Better Approach (O(n²))
# 🔹 Idea

# Find the next permutation manually using logic:

# For every permutation, generate the next by swapping and sorting tail.

# This version is still inefficient because sorting the suffix repeatedly costs O(n log n) or rebuilding the sequence costs O(n²).

# Let’s jump to the truly optimal version.

# ⚡ 3. Optimal Solution (O(n) Time, O(1) Space)
# 💡 Intuition (very important)

# Think of the array as digits forming a number.
# We want to make the next greater number with the same digits.

# Steps:

# Find pivot (i) — the first index from right where nums[i] < nums[i+1].

# This is where the descending order breaks.

# If none found → array is in descending order (last permutation).

# Find successor (j) — the smallest element greater than nums[i] to the right of it.

# Swap nums[i] and nums[j].

# Reverse the part right of i to make it the smallest possible sequence.

# 🔹 Code



class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse suffix
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums


df=Solution()
print(df.nextPermutation([2,1,3,4,5,0,0]))









# 🔹 Example Walkthrough

# nums = [1, 2, 3]

# 1️⃣ Find decreasing from right:
# i = 1 because 2 < 3

# 2️⃣ Find just larger:
# j = 2 because 3 > 2

# 3️⃣ Swap → [1, 3, 2]

# 4️⃣ Reverse suffix (only 1 element, stays same)

# ✅ Output → [1, 3, 2]

# 🔹 Another Example

# nums = [3, 2, 1]

# No i found (already descending)
# → Reverse entire array → [1, 2, 3]

# ✅ Output → smallest permutation.

# ⚙️ Complexity
# Metric	Value	Reason
# Time	O(n)	One right-to-left scan + one reverse
# Space	O(1)	In-place modifications
# ✅ Summary
# Approach	Time	Space	Notes
# Brute Force	O(n! × n)	O(n! × n)	Generate all permutations
# Better	O(n²)	O(1)	Repeated swaps/sorts
# Optimal	✅ O(n)	✅ O(1)	Standard algorithm (used in LeetCode #31)