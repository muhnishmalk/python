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
# Read the data from the file and update condition data
with open(data_file_path, 'r') as data_file:
    for line in data_file:
        description, short_description = line.strip().split('|~|')
        for condition in product_conditions:
            if check_condition(description, condition) or check_condition(short_description, condition):
                update_data(product_conditions, condition, description, short_description)
# Add "New" condition with no data
product_conditions['New'] = {'Description': [], 'Short Description': [], 'Total': []}
# Write the condition data to a CSV file
csv_file_path = 'condition_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(['Condition', 'Description', 'Short Description', 'Total'])
    for condition, data in product_conditions.items():
        description_data = '\n'.join(data['Description'])
        short_description_data = '\n'.join(data['Short Description'])
        total_data = '\n'.join(data['Total'])
        csv_writer.writerow([condition, description_data, short_description_data, total_data])
print("Condition data including 'New' added and migrated to 'condition_data.csv'.")

React

Reply










