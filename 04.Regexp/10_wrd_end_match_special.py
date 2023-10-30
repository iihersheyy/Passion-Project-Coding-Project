#Problem : Words ending with special characters list

#My_string = Welcome to python programming, procedures are simple
#Special string = e
#output >> Welcome are simple

my_string = "Welcome to python programming, procedures are simple"
sp_string = "e"

for i in my_string.split():
    if(i[-len(sp_string)].lower() == sp_string.lower()):
        print(i)