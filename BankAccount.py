class BankAccount:
	def __init__(self, name, balance = 0.0):
		self.log("Account Created")
		self.name = name
		self.balance = balance
	def getBalance(self):
		self.log("Checked Current Balance " +str(self.balance))
		return self.balance
	def setBalance(self, newBalance):
		self.log("Add ammount: " + str(newBalance))
		self.balance = newBalance
	def log(self, message):
		myLog = open("Log.txt", "a")
		print(message, file = myLog)
		myLog.close()
myBankAccount = BankAccount("Khadka Bogati")
myBankAccount.setBalance(500.0)
print(myBankAccount.getBalance())
