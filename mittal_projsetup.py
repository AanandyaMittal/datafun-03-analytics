''' This module provides functions for creating a series of project folders. '''
import math
import statistics
import pathlib
import time

#import module with company byline
import mittal_utils

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f'Byline: {mittal_utils.byline}')

    # Create folders for a range (e.g. years)
    create_folders_for_range(start=2018, end=2023)

    # Create folders given a list
    folder = ['analyst-Mark', 'analyst-Jared', 'analyst-Debra','analyst-Tina','analyst-Nathan']
    create_folders_from_list(folder)

    # Create folders using comprehension
    folder = ['Mark', 'Jared', 'Debra','Tina','Nathan']
    prefix = 'analyst-'
    create_prefixed_folders(folder, prefix)

    # Create folders periodically using while
    duration = 8  # duration in seconds
    create_folders_periodically(duration)

    # Call function and test these options
    specialties = [
      "restaurants", 
      "furniture", 
      "cookware", 
      "electronics", 
      "stationary", 
    ]
    create_folders_from_list(specialties, to_lower=True, delete_spaces=True)


'''
Create folders for a range of years.

Parameters:
- start (int): The starting year.
- end (int): The ending year.
'''
def create_folders_for_range(start, end):
    for year in range(start,end+1):
        folder_path = pathlib.Path(str(year))
        folder_path.mkdir(exist_ok=True)


'''
Create folders based on a list of folder names.

Parameters:
- folder_list (list): A list of folder names.
- to_lower (bool): Convert folder names to lowercase if True. Default is True.
- delete_spaces (bool): Remove spaces from folder names if True. Default is True.
'''
def create_folders_from_list(folder_list,to_lower=True,delete_spaces=True):
    for folder in folder_list:
        if (to_lower == True):
            new_folder = folder.lower()
        if (delete_spaces==True):
            new_folder = folder.replace(" ","")
        folder_path = pathlib.Path.cwd().joinpath(new_folder)
        folder_path.mkdir(exist_ok=True)
        

'''
Create folders with a prefix.

Parameters:
- folder_list (list): A list of folder names.
- prefix (str): The prefix to add to each folder name.
'''
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        new_folder = f"{prefix}{folder}"
        folder_path = pathlib.Path.cwd().joinpath(new_folder)
        folder_path.mkdir(exist_ok=True)


'''
Create folders periodically with a timestamp as the folder name.

Parameters:
- duration (int): The time interval in seconds between folder creation.
'''
def create_folders_periodically(duration):
    while True:
        time.sleep(duration)
        new_folder = f"folder_{time.time()}"  # Use a timestamp as folder name
        folder_path = pathlib.Path.cwd().joinpath(new_folder)
        folder_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    main()