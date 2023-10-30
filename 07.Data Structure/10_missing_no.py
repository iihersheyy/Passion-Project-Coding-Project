#Problem : Missing number 
#To find a missing number in a list of numbers from 1 to N, where one number is missing

def find_missing_number(nums, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2

    # Calculate the actual sum of the given list of numbers
    actual_sum = sum(nums)

    # The missing number is the difference between the expected and actual sums
    missing_number = expected_sum - actual_sum

    return missing_number

# Example usage
numbers = [1, 2, 3, 5]  # One number is missing in this list
n = 5  # The range of numbers is from 1 to 5

missing_number = find_missing_number(numbers, n)
print(f"The missing number is: {missing_number}")