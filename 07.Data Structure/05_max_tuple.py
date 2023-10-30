#Problem : Max element in a tuple 

test_list = [(2, 4), (6, 7), (5, 331), (6, 10), (8, 7)]

max = 0
for i,j in test_list:
    if (i>=j) and (i>=max):
        max=i 
    elif (j>=max):
        max=j

print("Max element of tuple is : %d" %max)