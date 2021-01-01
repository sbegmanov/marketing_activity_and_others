# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:57:55 2020

@author: salam
"""
"""
if you want to reuse functionality  from your code, define the logic in 
functions outside the main() and call those functions within main()
"""

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    data = "Data from the web"
    return data

def write_data_to_database(data):
    print("Writing data to a database")
    print(data)
    
def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == "__main__":
    main()