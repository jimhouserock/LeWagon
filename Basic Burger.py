#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a poor_calories_counter function which takes three string arguments and returns the total number of calories for the three items of your order.

#your function should make use of a Dictionary (obviously!)
#your function must use our given calorie values! eg:
#poor_calories_counter("McChicken", "French Fries", "Sprite")
#=> 730
#your function should return “item_name not found” if an item is not in the dictionary eg:
#poor_calories_counter("Big Mac", "Salad", "Shrimp Po Boy") 
#=> "Shrimp Po Boy not 

MCD_MENU = {
    "Hamburger":250,
    "Cheese Burger":300,
    "Big Mac":540,
    "McChicken":350,
    "French Fries":230,
    "Salad":15,
    "Coca Cola":150,
    "Sprite":150
}

def poor_calories_counter(x, y, z):
    
    a=MCD_MENU.get(x)
    b=MCD_MENU.get(y)
    c=MCD_MENU.get(z)
    
    calories = a+b+c
    
    return(calories)

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing with Hamburger, Cheese Burger, Big Mac")
if poor_calories_counter("Hamburger", "Cheese Burger", "Big Mac") == 1090:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Big Mac, Salad, Coca Cola")
if poor_calories_counter("Big Mac", "Salad", "Coca Cola") == 705:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with McChicken, French Fries, Sprite")
if poor_calories_counter("McChicken", "French Fries", "Sprite") == 730:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Shrimp, French Fries, Salad")
if poor_calories_counter("Shrimp", "French Fries", "Salad") == 'Shrimp not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")


# In[ ]:




