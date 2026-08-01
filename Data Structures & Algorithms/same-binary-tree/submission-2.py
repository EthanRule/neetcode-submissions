# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_order = []
        q_order = []

        self.inOrder(p, p_order)
        self.inOrder(q, q_order)

        if p_order == q_order:
            return True
        return False

    def inOrder(self, node, data):
        if node is None:
            return
        
        self.inOrder(node.left, data)
        if node.val == None:
            data.append(-1)
        else:
            data.append(node.val)
        self.inOrder(node.right, data)
