"""
Given the root node of a binary search tree and a value, find the node in the BST where the node's value equals the given value.

Return the subtree rooted with that node.

If such node doesn't exist, return NULL.
"""

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

		while current_node:
			# If the value is equal to the root, return the entire tree
			if current_node.val == val:
				return current_node
			# If the value is larger than the root, move to the right
			elif val > current_node.val:
				new_node = current_node.right
			# Otherwise, if value is smaller than the root, move to the right
			else:
				new_node = current_node.left

			current_node = new_node

# Passed 36/36 tests with runtime beating 80.79% of submissions and memory usage beating 43.02% of submissions