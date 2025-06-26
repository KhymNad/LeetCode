# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head.
        # This helps handle edge cases, like removing the first node.
        dummy = ListNode()
        dummy.next = head

        # Initialize two pointers, both starting at the dummy node.
        behind = ahead = dummy

        # Move the `ahead` pointer n+1 steps forward.
        # This creates a gap of n nodes between `ahead` and `behind`.
        for _ in range(n + 1):
            ahead = ahead.next

        # Move both pointers forward together until `ahead` reaches the end.
        # Since `ahead` is n+1 ahead of `behind`, `behind` will stop just before the target node.
        while ahead:
            behind = behind.next
            ahead = ahead.next

        # Skip the target node by pointing `behind.next` to the node after it.
        behind.next = behind.next.next

        # Return the new head of the list (which might have changed if head was removed).
        return dummy.next

        # TIME: O(n), n is length of linked list
        # SPACE: O(1)

