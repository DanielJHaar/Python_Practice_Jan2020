#Searches through an email txt file.  Identifies and parses all sender email addresses.
#Returns most frequent email address, along with it's count.

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    # Guardian in a compound statement, the first condition must be met before continuing
    if len(words) < 3 or words[0] != 'From' :
        continue
    #for each word identified in each line.  If not seen before, assign to list with value of 1.  Otherwise add 1 to count.
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1

#Parses through list of words and filters for those with the '@' symbol
bigcount = None
bigword = None
for word,count in counts.items():
    if "@" not in word :
        continue
    else:
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

print(bigword, bigcount)
