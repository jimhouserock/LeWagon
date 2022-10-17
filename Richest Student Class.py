#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""When initializing a Student, you should require 4 additional arguments, the student’s name and the number of bills they own (fives, tens and twenties)
Implement a wealth method on Student. When called it should return the total wealth of the student
Implement a compare method which takes one argument, another student, and returns the name of the richer student
"""

class Student:
    def __init__(self, name, fives, tens, twenties):
         self.name = name
         self.fives = fives
         self.tens = tens
         self.twenties = twenties
        
    def wealth(self):
        total = 5*self.fives + 10*self.tens + 20*self.twenties
        return total
            
    def compare(self,other):
        if self.wealth()>=other.wealth():
            return self.name
        else:
            return other.name




















# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os
from inspect import signature

print("Testing your class setup")
pre_r = "'\e[31m'"
pre_g = "'\e[32m'"
post = "'\e[0m'"
req_args = ['self', 'name', 'fives', 'tens', 'twenties']
req_methods = ['compare', 'wealth']
sig = signature(Student.__init__)
class_args = [param for param in sig.parameters]
class_methods = [method for method in dir(Student)]

if len(class_args) == 5:
    os.system("echo '\e[32mCorrect student class takes 5 arguments\e[0m'")
else:
    os.system("echo '\e[31mIncorrect student class takes 5 arguments \e[0m'")
for arg in req_args:
    if arg in class_args:
        os.system(str('echo ' + pre_g + f"Correct {arg} in Student class" + post))
    else:
        os.system(str('echo ' + pre_r + f"Incorrect {arg} not in Student class" + post))
for method in req_methods:
    if arg in class_args:
        os.system(str('echo ' + pre_g + f"Correct {method} in Student class" + post))
    else:
        os.system(str('echo ' + pre_r + f"Incorrect {method} not in Student class" + post))


one = Student('Amy', 5, 6, 7)
two = Student('Bilbo', 3, 4, 5)
three = Student('Chuck', 2, 3, 4)
four = Student('Diane', 1, 2, 3)
print("Testing your wealth method")
if one.wealth() == 225:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if two.wealth() == 155:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if three.wealth() == 120:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if four.wealth() == 85:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing your compare method")
if one.compare(two) == 'Amy':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if two.compare(one) == 'Amy':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if three.compare(four) == 'Chuck':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")
if four.compare(two) == 'Bilbo':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

if 'advanced_compare' in class_methods:
    print("Testing your advance compare method")
    correct_wealth = ['Amy', 'Bilbo', 'Chuck', 'Diane']
    if one.advanced_compare([two, three, four]) == correct_wealth:
        os.system("echo '\e[32mCorrect\e[0m'")
    else:
        os.system("echo '\e[31mIncorrect\e[0m'")

    if two.advanced_compare([one, three, four]) == correct_wealth:
        os.system("echo '\e[32mCorrect\e[0m'")
    else:
        os.system("echo '\e[31mIncorrect\e[0m'")

    if four.advanced_compare([three, one, two]) == correct_wealth:
        os.system("echo '\e[32mCorrect\e[0m'")
    else:
        os.system("echo '\e[31mIncorrect\e[0m'")


# In[ ]:




