#####################################################################
# Program : Count occurance of each character                       #
#####################################################################

string1 = input("\nEnter your string : ")

string2 = string1 

count = []
for i in string1:
    c = 0
    for j in string2:
        if (i == j):
            c+=1
    count.append(c)

print("\nString1 : %s" % string1)
for (i,j) in zip(string1,count):
    print("\n %s - occurred %s times" % (i,j))

print("\n")