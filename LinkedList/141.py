# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # this follows the tortoise and hare algorithm (Slow and Fast pointer) (Floyd's cycle-finding algorithm)
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            # make sure fast and fast.next is a node so that we can move fast over twice
            fast = fast.next.next
            slow = slow.next    # everytime fast moves over twice, slow moves over once

            if slow is fast:
                # if slow and fast are ever the same, them a cycle exists
                return True

        # no cycle exists
        return False

        # TIME: O(n)
        # SPACE: O(1)