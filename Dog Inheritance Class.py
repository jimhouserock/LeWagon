#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""We have created a Dog class with one instance method: bark
Create a new class GermanShepherd which inherits the bark method from its parent class

For example, the code below should work:

german_shepherd = GermanShepherd()
german_shepherd.bark()    # => "woo
"""

class Dog:
    def bark(self):
        print("woof woof")
# Do not modify the code above

class GermanShepherd (Dog):
    pass  
        



# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print('Testing your class Inheritance')
if len(GermanShepherd.__mro__) == 3:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print('Testing your class has access to a bark method')
method_list = [func for func in dir(GermanShepherd()) if callable(getattr(GermanShepherd(), func))]
if 'bark' in method_list:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print('Testing your class inherited the bark method')
if 'bark' not in GermanShepherd.__dict__.keys():
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")


# In[ ]:




