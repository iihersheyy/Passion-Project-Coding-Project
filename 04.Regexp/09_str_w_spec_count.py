#Problem : String starting with special characters list

#My_string = Welcome to python programming, procedures are simple
#Special string = pr
#output >> programming procedures

my_string = "Welcome to python programming, procedures are simple"
sp_string = "pr"

for i in my_string.split():
    if(i[:len(sp_string)].lower() == sp_string.lower()):
        print(i)