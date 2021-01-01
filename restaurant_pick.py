# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:16:56 2020

@author: salam
"""


import random

restaurantList = ['baloco', 'clover', 'sweetgreens', 'dig inn']

#print(restaurantList[random.randint(0,2)])

def pickRestaurant():
    print(restaurantList[random.randint(0, len(restaurantList)-1)])

def addRestaurant(name):
    restaurantList.append(name)

def removeRestaurant(name):
    restaurantList.remove(name)

def listRestaurant():
    for restaurant in restaurantList:
        print(restaurant)
    
while True:
    print('''
          
          [1] - List restaurant
          [2] - Add restaurant
          [3] - Remove restaurant
          [4] - Pick restaurant
          [5] - Exit
          
          ''')
    selection = input('Please select an aption: ')
    
    if selection == '1':
        print('')
        listRestaurant()
    elif selection == '2':
        inName = input('Type name of the restaurant: ')
        addRestaurant(inName)
    elif selection == '3':
        inName = input('Type name of the restaurant to remove: ')
        removeRestaurant(inName)
    elif selection == '4':
        pickRestaurant()
    elif selection == '5':
        print('Run again')
        break