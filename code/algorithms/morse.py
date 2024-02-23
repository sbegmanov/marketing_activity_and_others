# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:43:18 2020

@author: salam_000
"""

import re


def morse(text):
    encrypt = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 
            'D': '-..', 'E': '.', 'F': '..-.', 
            'G': '--.', 'H': '....', 'I': '..', 
            'J': '.---', 'K': '-.-', 'L': '.-..', 
            'M': '--', 'N': '-.', 'O': '---', 
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 
            'S': '...', 'T': '-', 'U': '..-', 
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ': '.....'
            }
    decrypt = {value: key for key, value in encrypt.items()}
    
    if re.match(r'(\s|-|\.) +', text):
        return ' '.join(decrypt[i] for i in text.split())
    return ' '.join(encrypt[i] for i in text.upper())
print(morse('shaxi'))
"""
import sys
if __name__ == "__main__":
    print(morse(sys.argv[0])) """
    
"""Running the script directly from the console, it will be the main program.
   In this case, to pass the argument to the morse function and print result 
   is wanted. To import the more function in another Python file, no need to
   to run this part of code. sys.arg[0] contains the file name (morse.py)"""