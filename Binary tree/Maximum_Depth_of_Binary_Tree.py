import deque

class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return max(lh,rh) + 1
    
# Optimal solution

class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0

        stack = deque([(root, 0)])
        maxDepth = 0
        while stack:
            node, currentDepth = stack.pop()
            if node.left is None and node.right is None:
                maxDepth = max(maxDepth, currentDepth + 1)
            if node.right:
                stack.append((node.right, currentDepth + 1))
            if node.left:
                stack.append((node.left, currentDepth + 1))
            
        return maxDepth