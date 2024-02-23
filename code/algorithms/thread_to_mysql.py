# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:34:19 2020

@author: salam_000
"""

from threading import Thread
import urllib
import re
import MySQLdb

login_info = open("threads/login.txt").read()
login_info = login_info.split()

host = login_info[0]
user = login_info[1]
password = login_info[2]

#conn = MySQLdb.connect(host="mysql.cars.com", user="chrisreeves", 
                       #passwd="florida128", db="stock_data")
conn = MySQLdb.connect(host=login_info[1], user=login_info[1], 
                       passwd=login_info[2], db="stock_data")
def the(ur):
    base = "http://finance.yahoo.com/q?s="+ur
    regex = '<span id="yfs_184_'+ur.lower()+'">(.+?)</span>'
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(base).read()
    results = re.findall(pattern, htmltext)
    print("the price of " +str(ur)+ " is " +str(results[0]))
    
symbolslist = open("threads/symbols.txt").read()
symbolslist = symbolslist.replace("", "").split(",")

print(symbolslist)

threadlist = []

for u in symbolslist:
    t = Thread(target=th, args(u,))
    t.start()
    threadlist.append(t)
    
for b in threadlist:
    b.join()