#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Our function should take a list of any size containing meals and individual dish items, eg:
#orders = ["French Fries", "Happy Meal", "Sprite", "Best Of McChicken"]
#advanced_calories_counter(orders)
#=> 1575
#Our function should still return ‘item_name not found’ if the dish is not available


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

MEAL = {
    "Happy Meal":"Cheese Burger, French Fries, Coca Cola",
    "Best Of Big Mac":"Big Mac, French Fries, Coca Cola",
    "Best Of McChicken":"McChicken, Salad, Sprite"
}


def advanced_calories_counter(mealMenu):
    
    final_cal=0
    count = 0 
    
    #print (len(mealMenu))
    for i in mealMenu:
        if i in MCD_MENU:
            final_cal = final_cal + poor_calories_counter(i)
        elif i in MEAL:
            #print (meal_counter(i))
            final_cal = final_cal + meal_counter(i)
        else:
            return (i+" not found")
            
            #print((list(MEAL.items()))[count][0])
           
        #for x in MEAL.items():
        count = count + 1
    return (final_cal)
    
    

def poor_calories_counter(x):
    
    calories=MCD_MENU.get(x)

    return(calories)
    

def meal_counter(x):
    
    total=0
    if x == "Happy Meal":
         total = poor_calories_counter("Cheese Burger")+poor_calories_counter("French Fries")+poor_calories_counter("Coca Cola")
    
    elif x == "Best Of Big Mac":
        total = poor_calories_counter("Big Mac")+poor_calories_counter("French Fries")+poor_calories_counter("Coca Cola")
      
    elif x == "Best Of McChicken":
        total = poor_calories_counter("McChicken")+poor_calories_counter("Salad")+poor_calories_counter("Sprite")
    return total




# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing with the lot")
if advanced_calories_counter(['Happy Meal', 'Best Of Big Mac', 'Best Of Royal Cheese']) == 'Best Of Royal Cheese not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with Big Mac, French Fries, Happy Meal, Coca Cola")
if advanced_calories_counter(["Big Mac", "French Fries", "Happy Meal", "Coca Cola"]) == 1600:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Best Of Big Mac, Salad, Happy Meal, Sprite")
if advanced_calories_counter(["Best Of Big Mac", "Salad", "Happy Meal", "Sprite"]) == 1765:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Happy Meal, McChicken")
if advanced_calories_counter(["Happy Meal", "McChicken"]) == 1030:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Fish and Chips, Salad")
if advanced_calories_counter(["Fish and Chips", "Salad"]) == 'Fish and Chips not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")


# In[ ]:




