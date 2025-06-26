# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solved with slow and fast pointers
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next    # slow pointer moves over 1 node
            fast = fast.next.next # fast pointer moves ovr 2 nodes

        # at this point the fast pointer is outside the linked list, returning slow will provide the answer
        return slow

        # TIME: O(n)
        # SPACE: O(1)