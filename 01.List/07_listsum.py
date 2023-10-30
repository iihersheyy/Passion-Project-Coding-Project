#####################################################################
# Program : Sum of all elements of the list                         #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(int(input("\nEnter List Element : ")))


#STEP3 : Reverset the list
sum = 0
for i in range(0,n):
    sum = sum + a[i]

#STEP3 : Print the results
print("\nInputed List is : %s" % a)    
print("\nSum of all elements in the list   : %s\n" % sum)