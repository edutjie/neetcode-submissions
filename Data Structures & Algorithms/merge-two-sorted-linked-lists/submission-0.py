# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        head = None
        prev = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                
                if prev:
                    prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                if not head:
                    head = list2

                if prev:
                    prev.next = list2
                prev = list2
                list2 = list2.next

        while prev and list1:
            prev.next = list1
            prev = list1
            list1 = list1.next

        while prev and list2:
            prev.next = list2
            prev = list2
            list2 = list2.next

    


        return head
