# Definition for a binary tree node.
from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        rel = []
        q = deque([root])
        while q:
            current_n=len(q)
            for i in range(current_n):
                node = q.popleft()
                if i==current_n-1:
                    rel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return rel
        
        
