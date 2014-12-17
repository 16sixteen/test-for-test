class A(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
		print "A"

class B(A):
	def __init__(self, username, password):
		print "B"
		A.__init__(self, username, password)

class C(A):
	def __init__(self, username, password):
		print "C"
		A.__init__(self, username, password)

if __name__ == "__main__":
	c = C("langge", "jiahao")
	print c.username, c.password
	print c
