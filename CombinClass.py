class Person:
	def __init__(self, name, eyecolor, age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age
class Name:
	def __init__(self, firtname, lastname):
		self.firtname = firtname
		self.lastname = lastname
myPerson = Person(Name("khadak", "bogati"), "brown", 30)
print(myPerson.name.firtname)
print(myPerson.name.lastname)
print(myPerson.eyecolor)
print(myPerson.age)
