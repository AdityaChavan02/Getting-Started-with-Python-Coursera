#Rewrite the program that prompts the user for a list of numbers and prints the max and min of the numbers at the end when the user presses done.
#Write the program to store the numbers in a list and use Max Min functions to compute the value.



List=list()
while True:
    no=input("Enter the no that you so desire:\n")
    if no=='done':
        break
    List.append(no)

print(List)
print("The MAX value is %d",max(List))
print("The MIN value is %d",min(List))
