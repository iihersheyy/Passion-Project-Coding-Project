my_list=[]
while(1):
   my_input = input("Enter the elements of the list [00 to exit] : ")
   if my_input == "00":
      break 
   else:
      my_list.append(int(my_input))

print("Inputed List is : %s " % my_list)

#Step#1 : Sorting the array 

for i in range(len(my_list)):
    for j in range(i,len(my_list)) :
        if my_list[i] > my_list[j] :
            t = my_list[i] 
            my_list[i] = my_list[j]
            my_list[j] = t

print("Inputed List after sorting : %s " % my_list)

#Step#2 : Getting the searching element #
my_find = int(input("Enter the element to search in the given list : "))

#Step#3 : Binary search #

low = 0 
high = len(my_list)-1

found=0
while (low <= high ):

    mid = (low + high ) // 2

    if my_list[mid] == my_find:
        print("%s is FOUND at %s index" % (my_find,mid))
        found=1
        break 
    elif my_list[mid] < my_find :
        low = mid + 1
    else:
        high = mid - 1

if found == 0:
   print("\n%s is NOT-FOUND in %s list" %(my_find,my_list))
 