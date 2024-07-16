import csv
import periodictable

# Create a list of dictionaries with element information
elements_list = []
for element in periodictable.elements:
    element_info = {
        'Symbol': element.symbol,
        'Name': element.name,
        'AtomicNumber': element.number,
        'AtomicWeight': element.mass,
    }
    elements_list.append(element_info)

# Define the CSV file path
csv_file_path = 'periodic_table.csv'

# Define the CSV column headers
headers = ['Symbol', 'Name', 'AtomicNumber', 'AtomicWeight', 'Category']

# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerows(elements_list)

print(f"CSV file '{csv_file_path}' created successfully.")
