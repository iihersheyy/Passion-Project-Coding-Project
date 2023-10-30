#####################################################################
# Program : String Reverse without in-built function                #
#####################################################################

name = input("\nEnter your string : ")

lenstr = len(name)-1
revstr = ""
while(lenstr >= 0):
    revstr = revstr + name[lenstr]
    lenstr -= 1

print("\nEntered the string : %s" % name)
print("\nReverse the string : %s" % revstr)

print("\n")