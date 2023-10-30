#####################################################################
# Program : Number of Vowels in a given string                      #
#####################################################################

name = input("\nEnter your string : ")
count = 0

for i in name:
    if (i == 'a' or i =='e' or i == 'i' or i == 'o' or i =='u' or \
        i == 'A' or i =='E' or i == 'I' or i == 'O' or i =='U'):
        count +=1 

print("\nString1: %s" % name)
print("\nNo of vowels in the given string : %s" % count)

print("\n")