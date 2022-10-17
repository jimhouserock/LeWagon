#!/usr/bin/env python
# coding: utf-8

# In[2]:


""" Get the winning combination

Update the Cat class by placing the self keyword where needed
No new methods are needed
The class is correct when you run the file and see the following print out in the terminal:
"My 1 year old cat weighs 5 pounds and is brown.  Come back in a few years and see how he is doing"
--------------------10 years later----------------------
"My 10 year old cat now weighs 20 
"""


class Cat:
    def __init__(self):
        self.age = 1
        self.color = 'brown'
        self.weight = 5

    def age_10_years(self):
        self.age = self.age + 10

    def gain_weight(self):
        self.weight = self.weight+ 20

    def turn_grey(self):
        self.color = 'grey'


# Do not modify the code below:
cat = Cat()
print(f"My {cat.age} year old cat weighs {cat.weight} pounds and is {cat.color}.  Come back in a few years and see how he is doing.")


cat.age_10_years()
cat.gain_weight()
cat.turn_grey()
print("--------------------10 years later----------------------")
print(f"My {cat.age} year old cat now weighs {cat.weight} pounds and is {cat.color}")


# In[ ]:




