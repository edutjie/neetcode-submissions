# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr_head = head
        while curr_head:
            curr_head = curr_head.next
            l += 1

        i = 0
        curr_head = head
        prev = None
        while curr_head:
            if i == (l - n):
                if prev:
                    prev.next = curr_head.next
                else:
                    if head:
                        head = head.next
            else:
                prev = curr_head
            curr_head = curr_head.next
            i += 1

        return head