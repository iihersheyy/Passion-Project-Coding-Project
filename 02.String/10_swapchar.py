#####################################################################
# Program : Number of Vowels in a given string                      #
#####################################################################

name = input("\nEnter your string : ")
swapfrom = input("\nEnter from_Swap character : ")
swapto = input("\nEnter to_Swap character : ")

count = 0
result =""

for i in name:
    if (i == swapfrom):
        result = result + swapto
    else:
        result = result + i

print("\nString1: %s" % name)
print("\nSwap_From: %s" % swapfrom)
print("\nSwap_To: %s" % swapto)

print("\nAfter swap, Result : %s" % result)

print("\n")