from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    

# 🧠 Why does this ALWAYS work?

# Let’s think mathematically:

# Suppose list has n nodes
# Fast moves 2 steps each time
# Slow moves 1 step

# After k steps:

# slow moved = k
# fast moved = 2k

# When fast reaches end:

# 2k ≈ n
# → k ≈ n/2

# 👉 So slow is at:

# n/2 → middle    