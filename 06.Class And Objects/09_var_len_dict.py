#Problem : Sending Variable length keyword argument to a fuction 

def get_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")

print("calling get_info with 3 argements")
get_info(name="Harshatha", age=16, city="CA")
print("calling get_info with 2 argements")
get_info(name="Harshatha", age=16)
print("calling get_info with 1 argement")
get_info(name="Harshatha")
