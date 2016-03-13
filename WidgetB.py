class WidgetB (object):

	def __init__ (self):
		self.next_account_id = 0;
		self.account_dict = {};
		#constructor
		pass
	def __del__ (self):
		# destructor
		self.next_account_id = 0;
		self.account_dict.clear
		pass

	def addAccount (self):
		id = self.next_account_id
		account = "Account #"+str(id)
		self.account_dict[id] = account
		self.next_account_id += 1
		return (id,account)

	def getNumAccount (self):
		return len (self.account_dict)

	def getAccount (self, id):
		if id in self.account_dict:
			return self.account_dict[id]
		else:
			message = "ID "+str(id)+" does not exist"
			raise RuntimeError, message


