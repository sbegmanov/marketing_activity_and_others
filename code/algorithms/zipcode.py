# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:33:26 2020

@author: salam
"""

import openpyxl, zipcodes

wb = openpyxl.load_workbook('')
sheet = wb['sq_temple_orders_addr']

for row in sheet.iter_rows(min_row=1, min_col=41, max_col=43):
    try:
        zp = str(row[0].value)
        while(len(zp) < 5):
            zp = '0' + zp
        print(zp)
        row[0].value = zp
        row[1].value = zipcodes.matching(zip)[0]['lat']
        row[2].value = zipcodes.matching(zp)[0]['long']
    except:
        print('error with zipcode' + zip)
wb.save('')
