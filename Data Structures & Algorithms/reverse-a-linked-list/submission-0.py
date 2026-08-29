# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        lst = lst[::-1]

        lstNode = None
        headRes = None
        for i, v in enumerate(lst):
            if lstNode == None:
                lstNode = ListNode(v, None)
                headRes = lstNode
            else:
                lstNode.next = ListNode(v, None)
                lstNode = lstNode.next

        return headRes