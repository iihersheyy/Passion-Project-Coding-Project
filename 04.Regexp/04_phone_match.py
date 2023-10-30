#Problem : Find the phone number in the given string (Format xxx-xxx-xxxx)

import re
my_string = "My mobile number is 123-456-7891"

#pattern = "\d\d\d-\d\d\d-\d\d\d\d"
pattern = "\d{3}-\d{3}-\d{3}"

result = re.search(pattern,my_string)
print(result)
print(result.span())
print(result.group(0))
