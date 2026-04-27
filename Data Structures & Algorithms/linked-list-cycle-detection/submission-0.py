# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head

        while cur.next != None:
            if cur.val == -1:
                return True
            else:
                cur.val = -1
            cur = cur.next
        return False