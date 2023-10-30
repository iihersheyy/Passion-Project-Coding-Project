#####################################################################
# Program : Length of the string                                    #
#####################################################################

name = input("\nEnter your string : ")
count = 0

for i in name:
    count += 1

print("\nEntered the string : %s" % name)
print("\nLength of the string without using built-in : %s" % count)

print("\n")