""" 112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

from typing import Optional

class TreeNode:
    """
        Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
        Soluición
    """
    def has_path_sum(self, tr_root: Optional[TreeNode], in_target_sum: int) -> bool:
        """ Encuentra la ruta que es igual a númeo objetivo

        La logica del ejercicio es bastante sencilla, dado que se va restando los 
        numeros que tienen los nodos al número objetivo hasta llegar a cero, corroborando de esta 
        manera que la ruta seleccionada es la buscada

        Parameters:
            - tr_root *(TreeNode)* - Es el árbol binario que contiene la estructura a evaluar
            - in_target_sum *(int)* - Número objetivo 
        Returns:
            - *(bool)* - Valor boleano de las expresión 

        """

        if not tr_root:
            return False

        if not tr_root.left and not tr_root.right:
            return tr_root.val == in_target_sum

        in_target_sum -= tr_root.val

        return  self.has_path_sum(tr_root.left, in_target_sum) or self.has_path_sum(tr_root.right,
                                                                                     in_target_sum)

# Finite Incatatem
