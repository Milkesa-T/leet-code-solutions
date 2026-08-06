# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        ptr2 = head
        while list1 and list2:
            if list1.val <= list2.val:
                ptr2.next = list1
                list1 = list1.next
            else:
                ptr2.next=list2
                list2=list2.next
            ptr2=ptr2.next
        if list1:
            ptr2.next=list1
        else:
            ptr2.next=list2
        return head.next

        