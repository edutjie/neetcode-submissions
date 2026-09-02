# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the midle to end
        res = head
        tail = slow
        prev_tail = None
        while tail:
            tmp = tail.next
            tail.next = prev_tail
            prev_tail = tail
            tail = tmp
        tail = prev_tail

        while head and tail and tail.next:
            tmp1, tmp2 = head.next, tail.next
            head.next = tail
            tail.next = tmp1
            tail = tmp2
            head = tmp1