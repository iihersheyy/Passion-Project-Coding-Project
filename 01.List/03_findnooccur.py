#####################################################################
# Program : Find number of occurance  in a list                     #
#####################################################################

#STEP1 : Get the length of the list from the user
n = int(input("\nEnter number of elements in the list : "))

#STEP2 : Get the element of the list
a = []
for i in range(0,n):
    a.append(input("\nEnter List Element : "))

print("\nInputed List is : %s" % a)    

#STEP3 : Find the search string
sstring = input("Enter the string to find occurance : ")

#STEP3 : Find the occurance
count = 0
for i in range(0,n):
    if a[i] == sstring:
        count += 1

print("\n %s - is occured - %s times in %s \n" % (sstring,count, a) )

