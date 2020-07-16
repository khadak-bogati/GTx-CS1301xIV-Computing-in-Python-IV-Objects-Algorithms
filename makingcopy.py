class Person:
	def __init__(self, name, eyecolor, age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age
class Name:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
myPerson1 = Person(Name("khadak", "Bogati"), "Black", 34)
myPerson2 = Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)
print(myPerson2.eyecolor)
myPerson2.name.firstname = "Surakshya"
print(myPerson1.name.firstname)
print(myPerson2.name.firstname)
