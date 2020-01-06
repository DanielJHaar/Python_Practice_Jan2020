largest = None
smallest = None
#Make an empty list before the loop starts
numlist = list()
#User input function, that creates a list of inputted values
while True :
	inp = input('Enter a number: ')
	if inp == 'done' :
		break
	try:
		fval = float(inp)
		numlist.append(fval)
	except:
		print('Invalid input')
		continue

# find largest value in list
for value in numlist :
	if largest is None :
		largest = value
	elif value > largest :
		largest = value

# find smallest value in list
for value in numlist :
	if smallest is None :
		smallest = value
	elif value < smallest :
		smallest = value
print("Maximum is", largest)
print("Minimum is", smallest)
