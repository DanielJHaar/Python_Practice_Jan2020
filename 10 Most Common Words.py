#Prompts the user to input a file. Identifies the 10 most common words in the file and their respective frequency.  
#Prints these top 10 most common words in descending order.
name = input("Enter file:")
handle = open(name)
counts=dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)
