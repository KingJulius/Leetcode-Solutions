# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        curr = root
        count = 0
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right
        
        return count
            