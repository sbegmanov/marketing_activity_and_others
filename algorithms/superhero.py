# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:13:40 2020

@author: salam_000
"""

class Person(object):
    def __init__(self, name):
        self.name = name
        
    def reveal_identity(self):
        print( "My name is {}".format(self.name))
      
        
class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
        
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print ("... And i am {}".format(self.hero_name))
        
        
corey = Person('Corey')
corey.reveal_identity()
print(corey)

wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()
print(wade)
