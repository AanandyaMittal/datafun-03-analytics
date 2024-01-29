import csv
import pathlib 
from io import StringIO
from pathlib import Path
import io
import requests
import urllib3
import pandas as pd
import json

import mittal_projsetup
import mittal_utils

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS='ALL:@SECLEVEL=1'

def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: {mittal_utils.company_name}")

    txt_url = 'https://example-files.online-convert.com/document/txt/example.txt'

    csv_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv' 

    excel_url = 'https://go.microsoft.com/fwlink/?LinkID=521962' 
    
    json_url = 'https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    prs_txt_data(txt_folder_name,'data.txt', 'results_txt.txt')
    prs_csv_data(csv_folder_name,'data.csv', 'results_csv.txt')
    prs_excel_data(excel_folder_name,'data.xls', 'results_xls.txt')
    prs_json_data(json_folder_name,'data.json', 'results_json.txt')


def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

#Process Text Data: Process text with lists and sets
def prs_txt_data(folder_name, filename, results):
    # read file
    text_data = open(Path(folder_name).joinpath(filename), 'r').read() 

    words = text_data.split()
    set_words = [word.lower() for word in words]  # Converting all words to lowercase

    word_stats = f"Word Statistics: \n"  # Total word count
    word_stats += f"Word count: {len(words)}\n"  # Total word count
    word_stats += f"Unique word count: {len(set(set_words))}\n"  # Unique word count using a set for calculation

    # Counting frequency of each word in the list
    for word in set(set_words):
        frequency = set_words.count(word)
        word_stats += f"Frequency of '{word}': {frequency}\n"
   
    # writeable version of file
    w_text_data = open(Path(folder_name).joinpath(results), 'w')
    w_text_data.write(word_stats)

    w_text_data.close()

#Process Excel Data: Extract and analyze data from Excel files
def prs_excel_data(folder_name, filename, results):
    # read file
    excel_data_df = pd.read_excel(Path(folder_name).joinpath(filename))

    column = excel_data_df['Units Sold'].astype(int)

    # writeable version of file
    w_excel_data = open(Path(folder_name).joinpath(results), 'w')
    w_excel_data.write('Units Sold Statistics:\n')
    w_excel_data.write(
            f'Mean: {column.mean()}\n'
            f'Median: {column.median()}\n'
            f'Mode: {column.mode()}\n'
            f'Min: {column.min()}\n'
            f'Max: {column.max()}\n'
        )

    w_excel_data.close()

#Process CSV Data: Process CSV files with tuples
def prs_csv_data(folder_name, filename, results):
    # read file
    csv_data = csv.reader((open(Path(folder_name).joinpath(filename), 'r')), delimiter= ',')
    column_sums = None
    is_first_row = True  # Flag for the first row (headers)

    for row in csv_data:
        if is_first_row:
            # Skip the first row (headers) and initialize column sums
            column_sums = (0,) * (len(row) - 1)  # Exclude the "Index" column
            is_first_row = False
            continue

        # Exclude the "Index" column and sum the rest
        # Convert height and weight to integers
        height = int(float(row[1]))
        weight = int(float(row[2]))
        column_sums = tuple(sum_value + value for sum_value, value in zip(column_sums, [height, weight]))

    # writeable version of file
    w_csv_data = open(Path(folder_name).joinpath(results), 'w')
    w_csv_data.write('People Statistics: \n')
    for header, sum_value in zip(["Height(Inches)", "Weight(Pounds)"], column_sums):
        w_csv_data.write(f'Sum of {header}: {sum_value}\n')

    w_csv_data.close()

#Process JSON Data: Process JSON data with dictionaries
def prs_json_data(folder_name, filename, results):
    try:
        # read file
        json_data = json.load(open(Path(folder_name).joinpath(filename), 'r'))

        if len(json_data) == 0:
            raise ValueError("The JSON file is empty.")

        # Calculating sepal count, averages
        sepal_count = len(json_data)
        sepal_length_avg = sum(sepal["sepalLength"] for sepal in json_data) / sepal_count
        sepal_width_avg = sum(sepal["sepalWidth"] for sepal in json_data) / sepal_count

        # Preparing human-readable text with only count, average length, and average width
        sepal_info = (f"Total Sepal Count: {sepal_count}\n"
                        f"Average Sepal Length: {sepal_length_avg}\n"
                        f"Average Sepal Width: {sepal_width_avg}\n")

        # writeable version of file
        w_json_data = open(Path(folder_name).joinpath(results), 'w')
        w_json_data.write('Sepal Statistics: \n')
        w_json_data.write(sepal_info)

        w_json_data.close()

    except json.JSONDecodeError:
        print("Failed to decode JSON. Please check the file format.")
    except FileNotFoundError:
        print(f"The file {filename} was not found in {folder_name}.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# conditional execution
if __name__ == "__main__":
    main()