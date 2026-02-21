# Union two arrays without duplicates

a= [1, 2, 3, 4, 5]
b= [1, 2, 3, 6, 7]
a=a+b
print(list(set(a)))

arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]

#Optimal

### 🔑 Idea: Two-pointer approach

# If both arrays are **sorted**, we can traverse them like merge step in merge-sort.

# ---

# ### Algorithm

# 1. Have two pointers `i=0` for `a`, `j=0` for `b`.
# 2. Compare `a[i]` and `b[j]`:

#    * If `a[i] < b[j]`: add `a[i]`, move `i++`.
#    * Else if `a[i] > b[j]`: add `b[j]`, move `j++`.
#    * Else: they’re equal → add once, move both.
# 3. After one list ends, copy remaining elements from the other.
# 4. While adding, check last inserted element to avoid duplicates.

# ---

### ✅ Optimal Code

class Solution:
    def findUnion(self, a, b):
        n, m = len(a), len(b)
        i, j = 0, 0
        union = []

        while i < n and j < m:
            if a[i] < b[j]:
                if not union or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if not union or union[-1] != b[j]:
                    union.append(b[j])
                j += 1
            else:
                if not union or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
                j += 1

        while i < n:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i += 1

        while j < m:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1

        return union


### ⏳ Time Complexity

# * Each element in both arrays is traversed once


# O(n+m)


# ### 💾 Space Complexity

# * Only output list (`union`), no extra DS


# O(n+m) \quad (\text{just the result itself, so extra space } O(1))


# ---

# ✅ This is the **most optimal solution** for union of two sorted arrays.
# If arrays are **unsorted**, you’ll first need to sort them (`O((n+m) log(n+m))`).


