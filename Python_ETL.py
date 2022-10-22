# Pre-requisites:
# Use Data library for file creation and python functional programming.
# Allowed to use inbuilt python functions
# 1. Create a 1 million record in csv file with the following records with auto generated column and
# values
# 2. FirstName, MiddleName, LastName, Address Postalcode and fill the values
# 3. Dynamically create additional columns city, state and postal code and split the address to all
# these 3 columns
# 4. Create a final output back to csv file.


#library to generate fake names and addresses.
from faker import Faker
#https://faker.readthedocs.io/en/
import pandas as pd
from geopy.geocoders import Nominatim
def create_dataframe(nrows= int(1e6)):
    fake = Faker()
    df = pd.DataFrame({'FirstName': [fake.first_name() for i in range(nrows)],
                      'MiddleName': [fake.first_name() for i in range(nrows)],
                      'LastName': [fake.last_name() for i in range(nrows)],

                      'Postalcode': [fake.zipcode_in_state() for i in range(nrows)]
                      
                      })

    zip_country = pgeocode.Nominatim('us')
    df = df.assign(State = zip_country.query_postal_code(df['Postalcode'].to_list()).state_name,
                    City = zip_country.query_postal_code(df['Postalcode'].to_list()).place_name)
    df.to_csv('your save location')
    return df


create_dataframe()
#%%
# import pgeocode
# data = pgeocode.Nominatim('US')
# print(data.query_postal_code("97749"))
#%%

#%%
# Question 3:
# Prerequisite:
# 1. Use data libraries, python standard libraries for efficient coding,
# 2. Time and space complexities to consider while coding this program.
# 3. Apply python design principles as needed(Explain which principle is used and why)
# Write a python program to validate the below scenario
# 1. Create a 1000 record csv files with id,name,salary
# 2. Create a same 1000 records with json file with same values
# a. Except change couple of rows of records with values changed.
# 3. Write a program to find the differences and print the difference in a separate csv file output
# 4. Add bonus of 1500 to the salary for the salary equals to 10000 and 2000 for the salary between
# 10,000 – 15000 and 3000 for the salary > 15000
# 5. Write the output back to csv file.


import string
import random
import numpy as np
import pandas as pd
from faker import Faker

#to generate id's
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def data_process(nrows= 1000):
    fake = Faker()
    df = pd.DataFrame({'ID': np.array([id_generator() for i in range(1*nrows)]),
                'FirstName': [fake.name() for i in range(nrows)],
                'Salary': [np.random.randint(5000, 25000) for _ in range(nrows)]}
                )
    df.to_csv('your saving location')
    df.to_json(r'your saving location')
    return df

def read_and_compare():
    #1.Create a 1000 record csv files with id,name,salary
    read_csv = pd.read_csv(r"your saving location", index_col = None)

    read_json = pd.read_json(r"your saving location")

    #2. Create a same 1000 records with json file with same values
    #I changed index 0 7K49GP and First Name Johnson Johson and salary 6054
    compare_files = pd.merge(read_csv, read_json, on=['ID', 'FirstName', 'Salary'], how='outer', suffixes=['', '_'], indicator=True)

    #3. Write a program to find the differences and print the difference in a separate csv file output    
    compare_files_out = compare_files[compare_files._merge != "both"] 
    compare_files_out.to_csv('your saving location')
    

    #4 Add bonus of 1500 to the salary for the salary equals to 10000 and 2000 for the salary between 10,000 – 15000 and 3000 for the salary > 15000
    read_csv['Bonus'] = np.where(read_csv['Salary'] <= 10000,
                                            1500,
                        np.where((read_csv['Salary'] > 10000) & (read_csv['Salary'] <= 15000),
                                        2000,
                        np.where(read_csv['Salary'] > 15000,
                                          3000, "No_Bonus")))  
    #5 
    read_csv.to_csv('your saving location')


    return read_csv



#data_process()
read_and_compare()
