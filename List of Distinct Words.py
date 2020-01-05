#Prompts the user to input a file. Identifies all words in the file, and creates
#a sorted list of distinct words.

name = input('Enter Filename:')
handle = open(name)
lst = list()
for line in handle:
	words = line.split()
	for word in words:
		if word not in lst:
			lst.append(word)
lst.sort()
print(lst)
