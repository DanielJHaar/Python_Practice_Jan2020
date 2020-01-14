#Searches through an email database saved as a .txt. file, and returns a histogram of emails received by hour of day.

name = input("Enter name of file:")
handle = open(name)
counts = dict()
lst = list()
for line in handle:
    words = line.split()
    if len(words) < 3 or words[0] != "From" :
            continue
    time = words[5].split(':')
    hours = time[0]
    lst.append(hours)

for hour in lst:
    counts[hour] = counts.get(hour, 0) + 1

t = sorted(counts.items())
for k, v in sorted(counts.items()) :
    print(k, v)
