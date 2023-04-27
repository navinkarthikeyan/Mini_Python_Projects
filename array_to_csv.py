import csv

# Define the array of details
details = [
    ['John', 'Doe', 25, 'Male'],
    ['Jane', 'Doe', 22, 'Female'],
    ['Bob', 'Smith', 30, 'Male'],
    ['Alice', 'Jones', 27, 'Female']
]

# Set the output file path
output_file = 'output.csv'

# Open the output file for writing
with open(output_file, 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['First Name', 'Last Name', 'Age', 'Gender'])

    # Loop through the details array and write each row to the CSV file
    for row in details:
        writer.writerow(row)
