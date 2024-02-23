# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:35:43 2020

@author: salam
"""


from time import sleep

print("This is my file to demonstrate best practices")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)
    
if __name__ == "__main__":
    main()