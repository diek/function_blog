import collections


fname = raw_input("Enter file name: ")
if not fname:
    fname = "mbox-short.txt"

email_count = collections.defaultdict(int)

with open(fname) as fh:
    for line in fh:
        if line.startswith('From '):
            values = line.split()
            email_count[values[1]] += 1

max_key = 0
for name, key in email_count.items():
    if key > max_key:
        max_key = key
        max_email = name
print max_email + " " + str(max_key)
