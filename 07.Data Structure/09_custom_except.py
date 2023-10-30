#Problem : Custom Exception Example . Raising the exception if the value of a is not greation 10 

class ValueNOTGreaterThan10(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"ERROR : {value} is not greater than 10")

a=4
if a >= 10 :
    print("PASS : A is greater than 10")
else:
    raise ValueNOTGreaterThan10(a)

