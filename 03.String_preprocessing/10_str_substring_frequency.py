#Problem : Find the frequence of sub-strings in the given strings
# Example : Hello World, Hello Fremont, Hello my dear friend, famil and friend. 
# Output : Hello = 3 , World=1, Fremont=1, friend=2, etc.,

str1 = "Hello World, Hello Fremont, Hello my dear friend, famil and friend"

u_str1 = []

#Replace special characters with ""

str1 = str1.replace(",","")
str1 = str1.replace(".","")

#Find the unique words
for i in str1.split():
    if i not in u_str1 :
        u_str1.append(i)

substr = {}
#Count number of unqiue worlds from the given string
for i in u_str1:
    c=0
    for j in str1.split():
        if i == j :
            c += 1
    substr[i] = c

print(substr)