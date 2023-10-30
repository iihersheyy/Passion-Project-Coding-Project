
a=[]
while(1):
   my_input = input("Enter the elements of the list [00 to exit] : ")
   if my_input == "00":
      break 
   else:
      a.append(my_input)

print("Inputed List is : %s " % a)
my_find = input("Enter the element to search in the given list : ")

fail=1
for lement in a:
   if lement == my_find:
      print("\n%s is FOUND in %s list" %(my_find,a))
      fail=0
      break
   
if fail == 1:
   print("\n%s is NOT-FOUND in %s list" %(my_find,a))
      

