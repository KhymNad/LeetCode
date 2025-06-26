# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        # While the current pointer is whithin the linked list
        while cur:
            # intuition is to have 3 pointers a current pointer that points to the node that is being flipped, and a previous pointer to point to the provious node that the current node will link to and a temp pointer that points to the next node in the linked list after cur that will be flipped
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

        # TIME: O(n)
        # SPACE: O(1) - recursive solutiuon would have O(n) because the recursve call stack would end up being the length of the list