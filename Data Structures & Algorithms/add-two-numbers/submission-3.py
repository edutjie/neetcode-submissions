# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mult = 1
        total = total2 = 0

        while l1 or l2:
            if l1:
                total += l1.val * mult
                l1 = l1.next
            
            if l2:
                total += l2.val * mult
                l2 = l2.next
            
            mult *= 10

        if total == 0:
            return ListNode(0)
        
        head = res = ListNode(0)
        while total % 10 or total != 0:
            curr_num = total % 10
            res.next = ListNode(curr_num)
            res = res.next
            total //= 10

        return head.next