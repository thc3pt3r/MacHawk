import csv, json, re, sys, os
import pandas as pd
import numpy as np

# Specify the path to the JSON file containing the fields to extract
fields_file_path = 'field_names.json'
output_file_path = 'matched_lines_005.csv'

def is_fortinet_log(log_file):
    with open(log_file, 'r') as file:
        first_line = file.readline()
        return 'devname=' in first_line

def is_custom_csv(csv_file):
    with open(csv_file, 'r') as file:
        first_line = file.readline()
        return re.search(r"(?i)\bitime=\d+\b", first_line) is not None
        #return re.search(r"(?i)\bdate=\d{4}-\d{2}-\d{2}\b", first_line) is not None

def search_ip_in_log(ip_address, log_file, output_file, fields_file):
    with open(log_file, 'r') as log, open(output_file, 'w', newline='') as output, open(fields_file, 'r') as fields:
        reader = csv.reader(log, delimiter=' ')
        writer = csv.writer(output, delimiter=',')
        field_names = json.load(fields)
        writer.writerow(field_names)

        for row in reader:
            line = ' '.join(row)
            if ip_address in line:
                extracted_fields = {}
                for field in field_names:
                    for item in row:
                        if item.lower().startswith(field.lower() + '='):
                            value = item.split('=')[1]
                            extracted_fields[field] = value
                writer.writerow([extracted_fields.get(field, '') for field in field_names])


def save_custom_search_to_csv(rows, output_file):
    fieldnames = rows[0].keys() if rows else []

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows()
    print(f"Matching rows saved to {output_file}.")

def search_ip_in_directory(ip_address, directory, output_file, fields_file):
    log_files = [f for f in os.listdir(directory) if f.endswith('.log')] + [f for f in os.listdir(directory) if f.endswith('.csv')]

    with open(output_file, 'w', newline='') as output, open(fields_file, 'r') as fields:
        writer = csv.writer(output)
        field_names = json.load(fields)
        writer.writerow(field_names)

        for log_file in log_files:
            log_file_path = os.path.join(directory, log_file)
            if is_custom_csv(log_file_path):
                search_ip_in_custom_csv_02(ip_address=ip_address, csv_file=log_file_path,output_file=output_file, fields_file=fields_file_path)            
            elif is_fortinet_log(log_file_path):
                search_ip_in_log(ip_address, log_file_path, output_file, fields_file)           
            else:
                print('Unrecognized file format for:', log_file)

def search_ip_address(ip_address, input_file, output_file, fields_file):
    if os.path.isdir(input_file):
        search_ip_in_directory(ip_address, input_file, output_file, fields_file)
    elif is_fortinet_log(input_file):
        search_ip_in_log(ip_address, input_file, output_file, fields_file)
    elif is_custom_csv(input_file):
        search_ip_in_custom_csv_02(ip_address=ip_address, csv_file=input_file,output_file=output_file, fields_file=fields_file_path)
    else:
        print('Unrecognized file format.')


def search_ip_in_custom_csv_02(ip_address, csv_file,output_file, fields_file):

    df = pd.read_csv(csv_file, header=None, na_filter=False, engine='python')

    df = df.astype(str)
   
    column_names = df.iloc[0].str.split('=', expand=True)[0].tolist()
    
    srcip_index = column_names.index("srcip")
    dstip_index = column_names.index("dstip")
    print(column_names)
    
    filtered_df = df[df.iloc[:, srcip_index].str.split('=', expand=True)[1] == ip_address] | df[df.iloc[:, dstip_index].str.split('=', expand=True)[1] == ip_address]
    
    with open(fields_file) as f:
        selected_columns = json.load(f)
    
    selected_columns_dict = {col: [] for col in selected_columns}
    
    max_fields = 0
    for _, row in df.iterrows():
        values = row.str.split('=', expand=True)[1].tolist()
        max_fields = max(max_fields, len(values))

        
        values.extend([''] * (max_fields - len(values)))

        for col, value in zip(column_names, values):
            if col in selected_columns_dict:
                selected_columns_dict[col].append(value)
    
    max_length = max(len(values) for values in selected_columns_dict.values())

    
    for col, values in selected_columns_dict.items():
        if len(values) < max_length:
            values.extend([''] * (max_length - len(values)))

    
    filtered_df = pd.DataFrame(selected_columns_dict)

    # Save to a new CSV file
    filtered_df.to_csv(output_file, index=False)


def show_menu():
    print("======= Malicious IP Reverse Searcher - DTT CIR TEAM =======")
    print("1. Search IP on Sigle Log file")
    print("2. Search IP on an entire directory")
    print("3. Search IP on SPIN specific format")
    print("4. Search pandas_test")
    print("5. exit")

    while True:
        try:
            choice = int(input("Please enter the number of choice: "))
            if choice < 1 or choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid Input. Please select and option from the menu.")

    if choice == 1:
        ip_address_to_search = input("Please input the desired IP: ")
        input_path = input("Please input the complete path of the log file: ")
        output_file = ip_address_to_search + "_reversed.csv"        
        search_ip_address(ip_address_to_search, input_path, output_file, fields_file_path)
    elif choice==2:
        ip_address_to_search = input("Please input the desired IP: ")
        input_path = input("Please input the directory path: ")
        output_file = ip_address_to_search + "_reversed.csv"
        search_ip_address(ip_address_to_search, input_path, output_file, fields_file_path)
    if choice == 3:
        ip_address_to_search = input("Please input the desired IP: ")
        input_path = input("Please input the complete path of the log file: ")
        output_file = ip_address_to_search + "_reversed.csv"
        search_ip_in_custom_csv_02(ip_address=ip_address_to_search, csv_file=input_path,output_file=output_file, fields_file=fields_file_path)
    elif choice==4:
        input_csv = input("Please insert csv file: ")
        search_ip_in_custom_csv_02(input_csv,output_file='pandas_result.csv')
    elif choice==5:
        sys.exit(0)
        

if __name__ == '__main__':
    show_menu()
