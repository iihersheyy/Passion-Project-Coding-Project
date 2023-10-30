#Problem : In the given string, replacing each chaacter with a-z
#Example : Welcome >>> aelcome,belcome,celcome..... 

my_string = "Welcome"
alpha = "abcdefghijklmnopqrstuvwxyz"

output = []
new_string = ""
for i in range(len(my_string)+1):
    new_1 = my_string[:i]
    new_2 = my_string[i:]
    for j in range(len(alpha)):
        if len(new_1)!=0 :
            print(new_1[0:len(new_1)-1]+alpha[j]+new_2)
    print("\n")    