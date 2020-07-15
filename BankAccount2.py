class BankAccount:
	def __init__(self, name, balance = 0.0):
		self.log("Account Created")
		self.name = name
		self.balance = balance
	def getBalance(self):
		self.log("Balance checked at "+ str(self.balance))
		return self.balance
	def deposit(self, amount):
		self.balance += amount
		self.log("+" + str(amount) + ":" +str(self.balance))
	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ":" +str(self.balance))
	def log(self, message):
		myLog = open("Log.txt", "a")
		print(message, file=myLog)
		myLog.close()
myBankAccount = BankAccount("Khadka Bogati")
myBankAccount.deposit(400.0)
print(myBankAccount.getBalance())
myBankAccount.withdraw(150)
print(myBankAccount.getBalance())
