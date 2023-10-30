import csv

csv_fname = "data.csv"

try:
    with open(csv_fname, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Read and process the header row
        header = next(csv_reader)
        print("CSV Header:", header)

        # Process and print each row of data
        for row in csv_reader:
            name, age, location = row  # Assuming the columns are in this order
            print(f"Name: {name}, Age: {age}, Location: {location}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
