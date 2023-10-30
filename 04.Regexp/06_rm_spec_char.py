#Problem : Remove all special characters from the given string 

import re

my_string = "Welcome! How re you? Keep going....$"

# Removing all special characters
print(''.join(re.findall('[^?!$.]',my_string)))

#Remove numbers
my_string ="I am at my age 16"
print(''.join(re.findall('\D',my_string)))

