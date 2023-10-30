#####################################################################
# Program : Remove duplicate & find unique element in the list      #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))


#STEP3 : Find the duplication
results = []
for i in range(0,n):
    duplicate = 0
    for j in range(0,len(results)):
        if a[i] == results[j]:
            duplicate = 1
            break 
    if duplicate == 0 :
        results.append(a[i])

print("\nInputed List is : %s" % a)    
print("\nAfter trimmed duplicate : %s" % results)
