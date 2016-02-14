name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst =list()
for line in handle:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] !="From" : continue
    a = words[1]
    lst.append(words[1])
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0)+1
bigcount= None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount

    
