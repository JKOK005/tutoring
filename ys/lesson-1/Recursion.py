from BinaryTrees import BinaryTree

# Based on https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

def initialize_tree():
	return BinaryTree(
				data 	= 1,

				left 	= BinaryTree(
							data  = 2,
							left  = BinaryTree(
										data  = 4,
										left  = None,
										right = None,	
									),

							right = BinaryTree(
										data  = 5,
										left  = None,
										right = None,	
									),
						),

				right 	= BinaryTree(
							data  = 3,
							left  = None,
							right = None,
						),
			)

def inorder(root):
	if root.get_left() is not None:
		inorder(root = root.get_left())
	
	print(root.get_data())

	if root.get_right() is not None:
		inorder(root = root.get_right())	

def pre_order(root):
	print(root.get_data())

	if root.get_left() is not None:
		pre_order(root = root.get_left())	

	if root.get_right() is not None:
		pre_order(root = root.get_right())	

def post_order(root):
	if root.get_left() is not None:
		post_order(root = root.get_left())	

	if root.get_right() is not None:
		post_order(root = root.get_right())

	print(root.get_data())

if __name__ == "__main__":
	tree = initialize_tree()
	
	print(">>>>>>>>>>> inorder <<<<<<<<<<<")
	inorder(root = tree)

	# print(">>>>>>>>>>> pre_order <<<<<<<<<<<")
	# pre_order(root = tree)

	# print(">>>>>>>>>>> post_order <<<<<<<<<<<")
	# post_order(root = tree)