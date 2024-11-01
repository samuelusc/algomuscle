# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            if not node:
                return "#"
            
            left = serialize(node.left)
            right = serialize(node.right)

            subTree = left + "," + right + "," + str(node.val)

            freq = hashmap.get(subTree, 0) + 1
            hashmap[subTree] = freq

            if freq == 2:
                res.append(node)

            return subTree
        res = []
        hashmap = {}
        serialize(root)
        return res