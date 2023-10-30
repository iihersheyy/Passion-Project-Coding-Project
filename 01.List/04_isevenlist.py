#####################################################################
# Program : Find even numbers from the list                         #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(int(input("\nEnter List Element : ")))


#STEP3 : Find EVEN from the list
results = []
for i in range(0,n):
    if a[i]%2 == 0 :
        results.append(a[i])

print("\nInputed List is : %s" % a)    
print("\nEven numbers in the list : %s" % results)