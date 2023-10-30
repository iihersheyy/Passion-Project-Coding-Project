#Problem : Find the specific patter with specific ending 
#Find the number at end of the word.
import re
my_string = " 4 is divisible by 2 but not 3 also 5 ada4"

print(re.findall("\d$", my_string))

#Find the capitial letters

print(re.findall("[A-Z]","Welcome to Pythong Programming"))

#Find the upper and lower letters

print(re.findall("[A-Za-z]","Welcome to year 2024"))

#Find the upper, lower letters and numberes

print(re.findall("[A-Za-z0-9]","Welcome to year 2024"))