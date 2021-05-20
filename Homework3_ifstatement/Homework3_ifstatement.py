def compare(a,b,c):
	if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
		return True
	else:
		return False
print(compare(1,1,2))
print(compare(1,2,2))
print(compare(2,1,2))
print(compare(1,2,3))
print(compare(6,6,"5"))