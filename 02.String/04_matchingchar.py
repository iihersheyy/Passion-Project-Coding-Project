#####################################################################
# Program : Number of matching chars                                #
#####################################################################

name1 = input("\nEnter your string1 : ")
name2 = input("\nEnter your string2 : ")

count = 0

result = []

for i in name1:
    for j in name2:
        if (i == j):
            result.append(i)
            break 

print("\nString1: %s" % name1)
print("\nString2: %s" % name2)
print("\nMatching characters between String1, String2 : %s" %result)

print("\n")