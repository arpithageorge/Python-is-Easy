
def Prime(n):
	if n > 1:
		for i in range(2,n):
			if (n%i) == 0:
				print(n)
				break
		else:
			print ("Prime")


for l in range(1,101):
	if l == 1:
		print(l)
	elif l%15 == 0:
		print("FizzBuzz")
	elif l%3 == 0:
		print("Fizz")
	elif l%5 == 0:
		print("Buzz")
	else:
		Prime(l)