#####################################################################
# Program : Remove duplicate chars from the string(case sensitive)  #
#####################################################################

name = input("\nEnter your string : ")
count = 0

result = ""
for i in name:
    found = 0
    for j in result:
        if i == j:
            found = 1
            break
    if found == 0:
        result = result + i
    
print("\nString1: %s" % name)
print("\nAfter remvoing duplicate char : %s" % result)

print("\n")