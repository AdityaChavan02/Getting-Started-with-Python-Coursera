#Write a program that categorizes each mail message by which day of the week the commit was done.
#To do this look for lines that start with "From", then look for the third word and keep a running count of all the days of the week.
#At the end of the program print out the contents of your dictionary.
# File: mbox-short.txt

def count_mails(text):
    for line in text:
        line.rstrip()
        if not line.startswith('From '): continue
        List = line.split()
        Dictionary[List[2]] = Dictionary.get(List[2],0)+1

    print(Dictionary)

fname = input("Enter the file name:\n")
fhand = open(fname)

Dictionary = dict()
List = list()
count_mails(fhand)
