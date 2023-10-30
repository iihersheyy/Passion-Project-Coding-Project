#Problem : In the given string, swap n,n+1 characters 
#Example : Welcome >>> eWlcome,eWclome,eWclmoe 

my_string = "Welcome"
new_string = ""
output = []

for i in range(0,len(my_string),2):
    try:
        n_element = my_string[i]
        np1_element = my_string[i+1]
        rest_element = my_string[i+2:]
        output += [new_string+np1_element+n_element+rest_element]
        new_string = new_string+np1_element+n_element
    except Exception as e:
        continue

print(output)
        