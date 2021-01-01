# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:18:17 2020

@author: salam_000
"""

import os

def child():
    print('\nA new child', os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" %pids)
        reply = input("q for quit /c for new fork")
        if reply == 'c':
                  continue
        else:
                  break
parent()