<<<<<<< HEAD
''' This module prints a byline for the company Your Data
    that includes company information and metrics'''

import math
import statistics

# Call main()
def main():
  print(byline)
    
# Company inforation
company_name: str = "Your Data Inc."
count_analyst_clients: int = 10
has_office_building: bool = False
average_analyst_rating: float = 8.5
analysts: list = ["Mark", "Jared", "Debra","Tina","Nathan"]
analyst_rating: list = [8.6,8.4,8.5,8.7,8.3]

# Convert variables to f-strings
analyst_clients_string: str = f"Clients assigned per analyst: {count_analyst_clients}"
office_building_string: str = f"Existence of Office Building: {has_office_building}"
analyst_rating_string: str = f"Average Analyst Rating: {average_analyst_rating}"
analyst_string: str = f"Our Analysts: {analysts}"

# Calculate metrics
smallest= min(analyst_rating)
largest= max(analyst_rating)
total= sum(analyst_rating)
count= len(analyst_rating)
mean= statistics.mean(analyst_rating)
mode= statistics.mode(analyst_rating)
median= statistics.median(analyst_rating)
standard_deviation=statistics.stdev(analyst_rating)

# Turn metrics into f-strings
metrics_string: str = f"""
Descriptive Statistics for European Country's inflation rate:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Define byline string
byline: str = f"""
{company_name}
{analyst_clients_string}
{office_building_string}
{analyst_rating_string}
{analyst_string}
{metrics_string}
"""

#''' Display all output'''
#print(company_name)
#print(analyst_clients_string)
#print(office_building_string)
#print(analyst_rating_string)
#print(analyst_string)
#print(metrics_string)

if __name__ == '__main__':
    main()
=======
''' This module prints a byline for the company Your Data
    that includes company information and metrics'''

import math
import statistics

# Call main()
def main():
  print(byline)
    
# Company inforation
company_name: str = "Your Data Inc."
count_analyst_clients: int = 10
has_office_building: bool = False
average_analyst_rating: float = 8.5
analysts: list = ["Mark", "Jared", "Debra","Tina","Nathan"]
analyst_rating: list = [8.6,8.4,8.5,8.7,8.3]

# Convert variables to f-strings
analyst_clients_string: str = f"Clients assigned per analyst: {count_analyst_clients}"
office_building_string: str = f"Existence of Office Building: {has_office_building}"
analyst_rating_string: str = f"Average Analyst Rating: {average_analyst_rating}"
analyst_string: str = f"Our Analysts: {analysts}"

# Calculate metrics
smallest= min(analyst_rating)
largest= max(analyst_rating)
total= sum(analyst_rating)
count= len(analyst_rating)
mean= statistics.mean(analyst_rating)
mode= statistics.mode(analyst_rating)
median= statistics.median(analyst_rating)
standard_deviation=statistics.stdev(analyst_rating)

# Turn metrics into f-strings
metrics_string: str = f"""
Descriptive Statistics for European Country's inflation rate:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Define byline string
byline: str = f"""
{company_name}
{analyst_clients_string}
{office_building_string}
{analyst_rating_string}
{analyst_string}
{metrics_string}
"""

#''' Display all output'''
#print(company_name)
#print(analyst_clients_string)
#print(office_building_string)
#print(analyst_rating_string)
#print(analyst_string)
#print(metrics_string)

if __name__ == '__main__':
    main()
>>>>>>> 80d139e8a3aa2c74ec9b96b4f4aa942a7f01a59e
