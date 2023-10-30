#####################################################################
# Program : Find second biggest element in the list                 #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(int(input("\nEnter List Element : ")))

#STEP3 : Initially assign first and second element as the big1,big2

if a[0] > a[1]:
    big1 = a[0]
    big2 = a[1]
else:
    big1 = a[1]
    big2 = a[0]

#STEP#4 : Iterate rest of the element and compare 

for i in range(2,n):
    if big1 < a[i] and big2 < a[i] :
        big2 = big1
        big1 = a[i]
    elif big1 < a[i] and big2 > a[i]:
        big2 = big1
        big1 = a[i]
    elif big1 > a[i] and big2 < a[i]:
        big2 = a[i]

#STEP#4 : Print the results
print("\nBiggest-1 : %s" % big1)
print("\nBiggest-2 : %s" % big2)