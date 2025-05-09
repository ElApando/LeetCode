""" Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the
 nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

from collections import deque

class TreeNode:
    """Función que permite convertir una lista en un arbol de nodos"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Clase solución"""

    def min_depth(self, root: TreeNode) -> int:
        """La función obtiene la profundidad mínima de la ramificación"""

        if not root:
            return 0

        queue = deque([(root, 1)])

        print(queue)

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))



ls_prove = [[3,9,20,"null","null",15,7],[2,"null",3,"null",4,"null",5,"null",6]]

call = Solution()

for ii in ls_prove:
    print(call.min_depth(ii))

# Finite Incantatem
