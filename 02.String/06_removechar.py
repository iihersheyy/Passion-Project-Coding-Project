#####################################################################
# Program : Remove chars from the given starting                    #
#####################################################################

name = input("\nEnter your string : ")
remchar = input("\nEnter char to remove : ")


lenstr = len(name)-1
index = 0
resultstr = ""

while(index <= lenstr):
   if remchar != name[index]:
    resultstr = resultstr + name[index]
   
   index+=1

print("\nEntered the string : %s" % name)
print("\nTrim the letter    : %s" % remchar)
print("\nAfter trimmed the string : %s" % resultstr)

print("\n")