#####################################################################
# Program : Substring from the given string                         #
#####################################################################

string1 = input("\nEnter your string : ")
start = int(input("\nEnter start index : "))
end = int(input("\nEnter length : "))


substr = ""
strlen = len(string1)-1
index = 0

while (start <= strlen):

    if index < end: 
        substr = substr + string1[start]
    
    start += 1
    index += 1

print("\nOriginal String : %s" % string1)
print("\nSubstring : %s" % substr)

print("\n")