#Problem : Find a word index in the given string 
#Example : Given string : "Hello World, you are good, Welcomes you"
#Find word : you
#Output : 13 16, 36 39

my_string = "Hello World, you are good, Welcomes you"
find_str = "you"

for i in range(len(my_string)):
    if my_string[i:i+len(find_str)] == find_str:
        print(i,i+len(find_str))