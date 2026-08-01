# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(l1.val + l2.val)
        cur = answer

        l1 = l1.next
        l2 = l2.next

        while l1 != None and l2 != None:
            cur.next = ListNode(l1.val + l2.val)
            
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
            
        return answer


