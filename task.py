import csv
import re
def check_condition(string, condition):
    if condition == "Renew":
        return "Renew" in string
    else:
        regex = re.escape(condition)
        return bool(re.search(regex, string, re.IGNORECASE))
def update_data(product_conditions, condition, description, short_description):
    product_conditions[condition]['Description'].append(description)
    product_conditions[condition]['Short Description'].append(short_description)
    product_conditions[condition]['Total'].append(description + " | " + short_description)
data_file_path = '/home/user/Documents/csv-new/sample.txt'  # Update the path to your data file
product_conditions = {
    'New': {'Description': [], 'Short Description': [], 'Total': []},
    'Refurbished': {'Description': [], 'Short Description': [], 'Total': []},
    'Renew': {'Description': [], 'Short Description': [], 'Total': []},
    'Remanufactured': {'Description': [], 'Short Description': [], 'Total': []},
    'Recertified': {'Description': [], 'Short Description': [], 'Total': []}
}
products =[]
# Read the data from the file and update condition data
with open(data_file_path, 'r') as data_file:
    for line in data_file:
        description, short_description = line.strip().split('|~|')
        for condition in product_conditions:
            if check_condition(description, condition) or check_condition(short_description, condition):
                update_data(product_conditions, condition, description, short_description)
                products.append({
                    'desc':description,
                    'shortDesc':short_description,
                    'condition':condition
                })
# Add "New" condition with no data
product_conditions['New'] = {'Description': [], 'Short Description': [], 'Total': []}
products.append({
                    'desc':description,
                    'shortDesc':short_description,
                    'condition':"New"
                })
csv_file = 'sample.csv'
fieldnames = products[0].keys()

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header (field names)
    writer.writeheader()
    
    # Write the data
    writer.writerows(products)

print(f'CSV file "{csv_file}" has been generated.')











