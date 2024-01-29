''' This project is to fetch data from the web, process it using 
    appropriate Python collections, and write the processed data to files.'''

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

"""
Writes text data to a file.

Parameters:
folder_name (str): The name of the folder where the file will be saved.
filename (str): The name of the file to write the data to.
data (str): The text data to write into the file.

Output:
A text file containing the provided data is saved to the specified location.
"""
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # Use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

"""
Writes binary data to an Excel file.

Parameters:
folder_name (str): The name of the folder where the file will be saved.
filename (str): The name of the file to write the data to.
data (bytes): The binary data (content of an Excel file) to write into the file.

Output:
An Excel file containing the provided data is saved to the specified location.
"""
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # Use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

"""
    Writes text data to a CSV file.

    Parameters:
    folder_name (str): The directory name where the file will be saved.
    filename (str): The name of the CSV file to be written.
    data (str): The text data to write to the CSV file.

    Output:
    Writes the provided data to a CSV file at the specified location.
"""
def write_csv_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # Use pathlib to join paths
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

"""
Writes text data to a JSON file.

Parameters:
folder_name (str): The directory name where the file will be saved.
filename (str): The name of the JSON file to be written.
data (str): The text data to write to the JSON file.

Output:
Writes the provided data to a JSON file at the specified location.
"""
def write_json_file(folder_name, filename, data):
    file_path = Path(folder_name).joinpath(filename) # Use pathlib to join paths
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")

"""
Fetches text data from a URL and writes it to a text file.

Parameters:
folder_name (str): The directory name where the file will be saved.
filename (str): The name of the text file to be written.
url (str): The URL to fetch the text data from.

Output:
Fetches data from the URL and writes it to a text file.
"""
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

"""
    Fetches data from a given URL and writes it to an Excel file.

    Parameters:
    folder_name (str): The directory name where the Excel file will be saved.
    filename (str): The name of the Excel file to be written.
    url (str): The URL to fetch the Excel data from.

    Output:
    Fetches data from the URL and writes it to an Excel file at the specified location.
"""
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

"""
Fetches data from a given URL and writes it to a CSV file.

Parameters:
folder_name (str): The directory name where the CSV file will be saved.
filename (str): The name of the CSV file to be written.
url (str): The URL to fetch the CSV data from.

Output:
Fetches data from the URL and writes it to a CSV file at the specified location.
"""
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

"""
Fetches data from a given URL and writes it to a JSON file.

Parameters:
folder_name (str): The directory name where the JSON file will be saved.
filename (str): The name of the JSON file to be written.
url (str): The URL to fetch the JSON data from.

Output:
Fetches data from the URL and writes it to a JSON file at the specified location.
"""
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

"""
Processes a text file to extract word count statistics and writes them to a file.

Parameters:
folder_name (str): The directory name where the text file is located.
filename (str): The name of the text file to process.
results (str): The name of the file where the results will be written.

Output:
Processes the text file and writes word count statistics to the results file.
"""
def prs_txt_data(folder_name, filename, results):
    # Read file
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
   
    # Writeable version of file
    w_text_data = open(Path(folder_name).joinpath(results), 'w')
    w_text_data.write(word_stats)

    w_text_data.close()

"""
Processes an Excel file to calculate statistics for a specified column and writes them to a file.

Parameters:
folder_name (str): The directory name where the Excel file is located.
filename (str): The name of the Excel file to process.
results (str): The name of the file where the results will be written.

Output:
Processes the Excel file and writes statistics for the specified column to the results file.
"""
def prs_excel_data(folder_name, filename, results):
    # Read file
    excel_data_df = pd.read_excel(Path(folder_name).joinpath(filename))

    column = excel_data_df['Units Sold'].astype(int)

    # Writeable version of file
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

"""
Processes a CSV file to calculate sum of numeric columns and writes them to a file.

Parameters:
folder_name (str): The directory name where the CSV file is located.
filename (str): The name of the CSV file to process.
results (str): The name of the file where the results will be written.

Output:
Processes the CSV file and writes the sum of numeric columns to the results file.
"""
def prs_csv_data(folder_name, filename, results):
    # Read file
    csv_data = csv.reader((open(Path(folder_name).joinpath(filename), 'r')), delimiter= ',')
    column_sums = None
    is_first_row = True 

    for row in csv_data:
        if is_first_row:
            # Skip the first row
            column_sums = (0,) * (len(row) - 1)  # Exclude the "Index" column
            is_first_row = False
            continue

        # Convert height and weight to integers
        height = int(float(row[1]))
        weight = int(float(row[2]))
        column_sums = tuple(sum_value + value for sum_value, value in zip(column_sums, [height, weight]))

    # Writeable version of file
    w_csv_data = open(Path(folder_name).joinpath(results), 'w')
    w_csv_data.write('People Statistics: \n')
    for header, sum_value in zip(["Height(Inches)", "Weight(Pounds)"], column_sums):
        w_csv_data.write(f'Sum of {header}: {sum_value}\n')

    w_csv_data.close()

"""
Processes a JSON file to calculate and write statistics of numeric values.

Parameters:
folder_name (str): The directory name where the JSON file is located.
filename (str): The name of the JSON file to process.
results (str): The name of the file where the results will be written.

Output:
Processes the JSON file and writes calculated statistics to the results file.
"""
def prs_json_data(folder_name, filename, results):
    try:
        # Read file
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

        # Writeable version of file
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

if __name__ == "__main__":
    main()