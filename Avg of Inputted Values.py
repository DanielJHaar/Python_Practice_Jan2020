#Input numeric values and press done when complete.
#Calculates the sum of the values, the number of values entered, and the average.


num = 0
tot = 0.0
while True :
	sval = input('Enter a number: ')
	if sval == 'done' :
		break
	try:
		fval = float(sval)
	except:
		print('Invalid input')
		continue
	print(fval)
	num = num + 1
	tot = tot + fval
print('ALL DONE')
print('Sum of entries: ', tot)
print('Number of entries: ', num)
print('Average: ', tot/num)
