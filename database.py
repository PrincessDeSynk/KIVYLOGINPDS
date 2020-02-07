
class Database():
	def __init__(self):
		pass

	def create(self, filename):
		self.filename = filename+'.txt'
		f= open(self.filename,'a')

		f.close()
	def datainput(self,name,password,email):
		self.name = name
		self.password = password
		self.email = email
		f = open(self.filename,'a')
		f.write(self.name+"\n")
		f.write(self.password+"\n")
		f.write(self.email+"\n")
		f.close()	
		
	def check(self,name,password):
		self.n = name
		self.p = password
		f= open(self.filename,'r')
		while(True):
			name =(f.readline())
			pas = (f.readline())
			email =(f.readline())
			name = name[:len(name)-1]
			pas = pas[:len(pas)-1]
			email = email[:len(email)-1]
			if name =="":
				f.close()
				return [0,"",""]
			di = {"name": name,"pa" : pas}
			if di["name"]==self.n and di["pa"]==self.p:
				f.close()
				return [1,name,email]
