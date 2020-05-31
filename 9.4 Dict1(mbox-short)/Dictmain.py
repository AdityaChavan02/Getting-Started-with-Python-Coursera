#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input('Enter the file name\n')
fhand= open(fname)
Dictionary = dict()
for line in fhand:
    line.rstrip()
    if not line.startswith('From: '): continue
    line=line.split()
    Dictionary[line[1]]=Dictionary.get(line[1],0)+1
max_key = None
max_val = None
for key, val in Dictionary.items():
    if max_val is None or val > max_val:
        max_val = val
        max_key = key
print(max_key, max_val)
