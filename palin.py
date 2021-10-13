
# Program to illustrate
# the use of user-defined functions

################ palindrome  string ###############################
string = input("enter a letter\n")
if(string==string[::-1]):
    print(string,"is a palindrome string")
else:
    print(string,"is not a palindrome string")