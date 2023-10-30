#Problem : In the given string, circularly swap
#Example : Welcome >>> elcomeW, lcomeWe, comeWel, omeWelc, meWelco, eWelcom, Welcome

my_string = "Welcome"

for i in range(len(my_string)+1):
    print(my_string[i:]+my_string[:i])
