#####################################################################
# Program : Find given string is a Palindrome                     #
#####################################################################

name = input("\nEnter your string : ")

strlen = len(name)-1
strrev =""

for i in range(strlen,-1,-1):
    strrev = strrev + name[i]

if name == strrev:
    print("%s - is a palindrome" % (name))
else:
    print("%s - is not a palindrome" % (name))


print("\n")