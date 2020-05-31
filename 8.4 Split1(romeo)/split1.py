#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.

fname = input('Enter the File name:\n')
fhand = open(fname)
words=[]                                            #Need to initialize the list before using
text=fhand.read()
text=text.split()
print(text)
try:                                                #try block
    for word in text:
        if word not in words:                       # If word not in words then the element gets added to the list
            words.append(word)
        else:
            continue
except:
    print('Something is wrong')
words.sort()                                        #function can be used without equating to a variable
print(words)
