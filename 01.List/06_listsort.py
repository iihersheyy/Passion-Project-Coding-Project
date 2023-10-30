#####################################################################
# Program : Sort the integer list                                   #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(int(input("\nEnter List Element : ")))

print("\nInputed List is : %s" % a)    

#STEP3 : Reverset the list
for i in range(0,n):
    for j in range(i,n):
        if a[i] > a[j]:
            t = a[i]
            a[i] = a[j]
            a[j] = t

#STEP3 : Print the results
print("\nSort the list   : %s" % a)