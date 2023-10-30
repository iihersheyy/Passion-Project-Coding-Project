#####################################################################
# Program : Create a sub-list from the given list                   #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))


#STEP3 : Get start & length of the sub-list 
start = int(input("\nEnter the start index : "))
end = int(input("\nEnter the Length : "))

#STEP3a : Error handling
if start > n or end > n :
    print("\nError : Start/End Index should be less the length actual list")
    print("\nError : Actual List : %s" % a)
    exit()

#STEP4 : Get the sub-list
sublist = []
index = 0 
while (index <= end):
    if (start+index) <= end:
        print("\nhit!")
        sublist.append(a[start+index])
    index+=1

print("\nOriginal List : %s" % a)    
print("\nSub-list Start & End Index from the orginal List : %s,%s" % (start,end))    
print("\nSub-list List : %s" % sublist)    