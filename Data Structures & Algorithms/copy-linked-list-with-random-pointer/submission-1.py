"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        new_head = None
        new_curr = None
        node_map = dict()
        while curr:
            new = Node(x = curr.val)
            key = f"{curr.val}-{curr.next}-{curr.random}"
            node_map[key] = new
            if new_head and new_curr:
                new_curr.next = new
                new_curr = new_curr.next
            else:
                new_head = new
                new_curr = new
            curr = curr.next

        curr = head
        new_curr = new_head
        while curr and new_curr:
            key = f"{curr.random.val if curr.random else None}-{curr.random.next if curr.random else None}-{curr.random.random if curr.random else None}"
            random_node = node_map.get(key, None) if curr.random else None
            if random_node:
                new_curr.random = random_node
            new_curr = new_curr.next
            curr = curr.next

        return new_head

