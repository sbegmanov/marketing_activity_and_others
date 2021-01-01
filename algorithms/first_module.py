# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:47:58 2020

@author: salam
"""


print("This will always be run")

def main():
    print("First Module's Name: {}".format(__name__))

# if __name__ == '__main__':
#     print("Run directly")
# else:
#     print("Run from Import")

if __name__ == '__main__':
    main()
