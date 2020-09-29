"""
This lesson plan introduces the concepts for building a binary tree

We will cover:
1) Definitions of a binary tree
	- Max depth of a balanced binary tree

2) Building binary trees

3) Traversal over trees
	- Pre-order & Post-order
"""

class BinaryTree(object):
	data 	= None
	left 	= None
	right 	= None

	def __init__(self, data: int, left: "BinaryTree", right: "BinaryTree"):
		self.data 	= data
		self.left 	= left
		self.right 	= right

	def get_data(self) -> int:
		return self.data

	def get_left(self) -> "BinaryTree":
		return self.left

	def get_right(self) -> "BinaryTree":
		return self.right

if __name__ == "__main__":
	"""
	Lets build the tree

			1
		   / \
	     2     3
	    / \   / \ 
	   4   N N   5
	"""

	root 	= BinaryTree(
				data 	= 1,

				left 	= BinaryTree(
							data  = 2,
							left  = BinaryTree(
										data  = 4,
										left  = None,
										right = None,	
									),

							right =None,
						),

				right 	= BinaryTree(
							data  = 3,
							left  = None,

							right = BinaryTree(
										data  = 5,
										left  = None,
										right = None,	
									),
						),
			)