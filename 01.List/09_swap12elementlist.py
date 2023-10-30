#####################################################################
# Program : Get the list from the user and swap the first and last  #
#           element of the list.                                    #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))


print("\nBefore Swap the list is : %s" % a)    

#STEP3 : Swap first and last element
t     = a[0]
a[0]  = a[-1] 
a[-1] = t


print("\nAfter swap the first & last element of the list : %s" % a)