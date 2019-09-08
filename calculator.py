

def class_checker ():
	numb = input('Enter a number: ')
	try:
		if '.' in numb:
			return float(numb)
		else:
			return int(numb)
	except ValueError:
		print ("Not a number! Please try again")
		return class_checker()

first_num = class_checker()
operator = input('Enter operator (+ or -): ')
second_num = class_checker()

if operator == '+':
	print (first_num + second_num)
elif operator == '-':
	print (first_num - second_num)