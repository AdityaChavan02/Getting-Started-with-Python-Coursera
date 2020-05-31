#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter the File name\n')
fhand = open(fname)
hours=dict()
lst=[]
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '): continue                   # lines starting with 'From '
    line = line.split()

    hour=line[5].split(':')                                     # we are not splitting the list here, we are splitting an element in the list
    hours[hour[0]]=hours.get(hour[0],0)+1

for k,v in hours.items():                                       # we split the hours list into items of key value pair
    lst.append((k,v))                                           # and append it to a new list that will be used to print the output

lst.sort()

for k,v in lst:                                                 # output
    print(k,v)
