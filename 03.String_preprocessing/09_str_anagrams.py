#Problem : Find the given string is Anagram or not ?
# Example : a word, phrase, or name formed by rearranging the letters of another, 
# such as cinema, formed from iceman.

#str1 = "A decimal point"
#str2 = "Im a dot in place"

str1 = "did2"
str2 ="dd22"

str11 = str1
str22 = str2

str1 = str1.replace(" ","").lower()
str2 = str2.replace(" ","").lower()

char_count = {}
u_str1 = []
u_str2 = []
s1_count = {}
s2_count = {}

# If str1 and str1 length is not match -- is not an anagram 

if len(str1) != len(str2):
    print("%s - and -  %s : are not an Anagram" % (str11,str22))
else:
    #Getting the unquie character is str1 and str2 to count
    for i in range(len(str1)):
        if str1[i] not in u_str1 :
            u_str1.append(str1[i])
    for i in range(len(str2)):
        if str2[i] not in u_str2 :
            u_str2.append(str2[i])

    #Getting the unquie character count is str1 and str2 
    for i in range(len(u_str1)):
        c = 0
        for j in range(len(str1)):
            if u_str1[i] == str1[j]:
                c += 1
        s1_count[u_str1[i]] = c 

    for i in range(len(u_str2)):
        c = 0
        for j in range(len(str2)):
            if u_str2[i] == str2[j]:
                c += 1
        s2_count[u_str2[i]] = c 


    print("String1 : Unique character count")
    for i in s1_count.keys():
        print(i + "=" + str(s1_count[i]))
    print("String2 : Unique character count")
    for i in s2_count.keys():
        print(i + "=" + str(s2_count[i]))

    flag = 0

    #Compare str1, str2 characters are common
    if s1_count.keys() == s2_count.keys() :
        for i in s1_count.keys():
            #Comparing the character frequence are matching or not ?
            if s1_count[i] != s2_count[i]:
                print(str1 + " and " + str2 + " -- " + " is NOT a anagram")
                flag=1

        if flag != 1:
            print(str11 + " and " + str22 + " -- " + " is a anagram")

    else:
        print(str1 + " and " + str2 + " -- " + " is NOT a anagram")
                

