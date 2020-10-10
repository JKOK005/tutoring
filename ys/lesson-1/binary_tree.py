import os

class BinaryTree(object):
	ID 		= None
	char 	= None
	left 	= None
	right 	= None

	def __init__(self, ID: int, char: str = None, left: 'BinaryTree' = None, right: 'BinaryTree' = None):
		self.ID 	= ID
		self.char 	= char
		self.left 	= left
		self.right 	= right

	def get_character(self):
		return self.char

	def get_id(self):
		return self.ID

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_char(self, char: str):
		self.char = char

	def set_left(self, left_node: 'BinaryTree'):
		self.left = left_node

	def set_right(self, right_node: 'BinaryTree'):
		self.right = right_node

def build_binary_tree(file: str) -> 'BinaryTree':
	bin_tree_map = {}

	with open(file) as f:
		lines = f.readlines()
		lines = list(map(lambda x: x.replace("\n", ""), lines))

		for each_line in lines[1:]:
			[ID, char, left_id, right_id]  	= each_line.split(" ")
			[ID, left_id, right_id] 		= list(map(lambda x: int(x), [ID, left_id, right_id]))

			left_node = right_node = None

			if left_id in bin_tree_map:
				left_node = bin_tree_map[left_id]
			elif left_id is not 0:
				left_node = BinaryTree(ID = left_id)
				bin_tree_map[left_id] = left_node

			if right_id in bin_tree_map:
				right_node = bin_tree_map[right_id]
			elif right_id is not 0:
				right_node = BinaryTree(ID = right_id)
				bin_tree_map[right_id] = right_node			

			if ID in bin_tree_map:
				# Set the values of the node
				node = bin_tree_map[ID]
				node.set_char(char = char)
				node.set_left(left_node = left_node)
				node.set_right(right_node = right_node)

			else:
				root = BinaryTree(ID = ID, char = char, left = left_node, right = right_node)
				bin_tree_map[ID] = root

		[root_id, _, _, _] = lines[1].split(" ")
		return bin_tree_map[int(root_id)]

def pre_order(root):
	# To be filled in
	pass	 

if __name__ == "__main__":
	tree_file = os.path.join(os.getcwd(), "resources/binary_tree_input_1.txt")
	tree = build_binary_tree(file = tree_file)
	inorder(root = tree)