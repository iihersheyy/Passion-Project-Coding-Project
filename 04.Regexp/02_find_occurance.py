#Problem : Find number of occurance of a string from the given string
#Given String : Welcome to Fremont, Fremont is a big city
#Search String : Fremont
#Output : 2

import re

results = re.findall("Fremont","Welcome to Fremont. Fremont is a big city")
print(results)
print(len(results))