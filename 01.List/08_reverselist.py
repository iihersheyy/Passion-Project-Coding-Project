#####################################################################
# Program : Get the list from the user and reverse the list without #
#           using any list-reverse built-in function.               #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))

#STEP3 : Reverset the list
results = []
for i in range(0,n):
    results.append(a[n-1-i])

#STEP3 : Print the results
print("\nInputed List is : %s" % a)    
print("\nReverse the list : %s" %results)