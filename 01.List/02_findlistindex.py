#####################################################################
# Program : Find the index of the element in the list               #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))

print("\nInputed List is : %s" % a)    

#STEP3 : Find the search string
sstring = input("\nFind the searching string : ")

#STEP3 : Reverset the list
found="0"
loc=-1
for i in range(0,n):
    if a[i] == sstring:
        loc=i
        found = "1"
        exit     

if found =="1":
    print("\nFOUND :%s in %s\n" %(sstring,loc))
else:
    print("\n NOT-FOUND :%s in %s\n" % (sstring,a) )

