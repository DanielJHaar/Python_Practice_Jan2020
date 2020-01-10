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

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1

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
