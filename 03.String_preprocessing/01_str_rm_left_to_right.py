#Problem : In the given string, remove the character from left to right & right to left

my_string = "Welcome"

print("Remove characters from right to left")
for i in range(len(my_string)):
    print(my_string[i:])


print("Remove characters from left to right")
for i in range(len(my_string)+1):
    print(my_string[:i])
