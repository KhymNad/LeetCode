# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # dummy head of merged list
        current = dummy     # current pointer to build the new list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining elements (only one of these will run)
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  # return the merged list, skipping the dummy node

        # TIME: O(n)
        # SPACE: O(1)
