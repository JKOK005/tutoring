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


if __name__ == "__main__":
	class_obj = MyFirstClass(number = 100)
	print("Variable in my class is {0}".format(class_obj.variable))

	class_obj.first_method()
	class_obj.second_method(x = 10, y = "hello world")
	class_obj.third_method(10, "Asd", message = "Learning how to build classes")