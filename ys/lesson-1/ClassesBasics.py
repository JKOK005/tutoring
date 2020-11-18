"""
This lesson plan introduces the basics of classes

We will cover:
1) Components of a class
	- Class name declaration
	- Inheritance
	- Class method definition
	- Class variable field

2) Instantiating a class object
"""
class MyFirstClass(object):
	variable = None

	def __init__(self, number: int):
		self.variable = number

	def first_method(self):
		"""
		Note: 
		- Method does not have parameter defined
		- Method MUST have `self`
		"""
		print("First method called")
		return

	def second_method(self, x: int, y: str) -> int:
		"""
		Note:
		- Method takes in x as an Integer and y as a String
		- Method returns Integer 
		- This is only for declaration. Python does not enforce the rule that x must be an Int.
		"""
		print("second method called with {0}, {1}".format(x, y))
		return

	def third_method(self, *args, **kwargs) -> None:
		"""
		Note:
		- What are args & kwargs?
		"""
		print("third method called with {0}, {1}".format(args, kwargs))
		return

# class MySecondClass(object):
# 	def first_method(self):
# 		"""
# 		Note: 
# 		- Method does not have parameter defined
# 		- Method MUST have `self`
# 		"""
# 		print("First method called")
# 		return

class Human():
	name 	= None
	height 	= None
	age	 	= None

	def __init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
		return 

	def get_name(self):
		return self.name

	def get_height(self):
		return self.height

	def get_age(self):
		return self.age

	def my_info(self):
		# def get_name(self):
		# 	return "asd"

		# def get_height():
		# 	return 1

		# def get_age():
		# 	return 100

		# name - height - age
		return "{0} - {1} - {2}".format(self.get_name(), self.get_height(), self.get_age())

if __name__ == "__main__":
	# class_obj = MyFirstClass(number = 100)
	# print("Variable in my class is {0}".format(class_obj.variable))

	# class_obj.first_method()
	# class_obj.second_method(x = 10, y = "hello world")
	# class_obj.third_method(10, "Asd", message = "Learning how to build classes")

	johan = Human(name = "johan", height = 180, age = 30)
	fahmi = Human(name = "fahmi", height = 180, age = 25)
	print(johan.my_info())
	print(fahmi.my_info())



