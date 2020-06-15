# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, val=0, left=None, right=None):
#			 self.val = val
# 	 		 self.left = left
#	  		 self.right = right
class Solution(object):
	def searchBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		# Compare the value to the root
		current_node = root

		# If the value is equal to the root, return the entire tree
		# If the value is larger than the root, move to the left
		# Otherwise, if value is smaller than the root, move to the right
		# Compare the value to the current node
		# Repeat 2 through 5 until the value is equal to the node
