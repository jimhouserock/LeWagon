#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Complete the class Dessert:

create instance variables for name and calories
create an instance method healthy which returns a bool. A dessert instance with fewer than 200 calories would be considered healthy
create an instance method delicious which returns a bool. All dessert instances should return True
Create the class JellyBean:

JellyBean should be a child of the Dessert class
JellyBean should take three arugments - name, calories, flavor
Keep your init method DRY with super()
JellyBean’s delicious method should return the default set in the parent class, unless its flavor is black licorice, which is not delicious
"""

class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
	
    def healthy(self):
        if self.calories<200:
            return True
        else:
            return False

    def delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self,name,calories, flavor):
        super().__init__(name,calories)
        self.flavor=flavor
        
    def delicious(self):
        if self.flavor =="black licorice":
            return not(super().delicious)
        else:
            return super().delicious
    
    
        
        


        
	



    
    
    
    
    



print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print('Testing your Dessert methods')
healthy_des = Dessert('cupcake', 100)
unhealthy_des = Dessert('cake', 300)
if healthy_des.healthy():
    os.system("echo '\e[32mCorrect, healthy if under 200 calories\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, should be healthy if under 200 calories\e[0m'")
if not unhealthy_des.healthy():
    os.system("echo '\e[32mCorrect, not healthy if over 200 calories\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, should not be healthy if over 200 calories\e[0m'")
if healthy_des.delicious():
    os.system("echo '\e[32mCorrect, Dessert is always delicious\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, Dessert is always delicious\e[0m'")
if unhealthy_des.delicious():
    os.system("echo '\e[32mCorrect, Dessert is always delicious\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, Dessert is always delicious\e[0m'")



print('Testing your JellyBean methods')
delicious_des = JellyBean('yummy', 100, 'cherry')
gross_des = JellyBean('disgusting', 300, 'black licorice')
if delicious_des.healthy():
    os.system("echo '\e[32mCorrect, healthy if under 200 calories\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, should be healthy if under 200 calories\e[0m'")
if not gross_des.healthy():
    os.system("echo '\e[32mCorrect, not healthy if over 200 calories\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, should not be healthy if under 200 calories\e[0m'")
if delicious_des.delicious():
    os.system("echo '\e[32mCorrect, most flavors are delicious\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, only black licorice is not delicious\e[0m'")
if not gross_des.delicious():
    os.system("echo '\e[32mCorrect, black licorice is not delicious\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, black licorice is not delicious\e[0m'")


print('Testing your JellyBean class Inheritance')
import dis
def list_method_calls(fn):
    methods = []
    bytecode = dis.Bytecode(fn)
    instrs = list(reversed([instr for instr in bytecode]))
    for ix, instr in enumerate(instrs):
        if instr.opname=="CALL_FUNCTION":
            load_method_instr = instrs[ix + instr.arg + 1]
            methods.append(load_method_instr.argval)
    return methods
init_calls = list_method_calls(JellyBean.__init__)
delicious_calls = list_method_calls(JellyBean.delicious)
if len(JellyBean.__mro__) == 3:
    os.system("echo '\e[32mCorrect, JellyBean has a parent class\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, JellyBean does not inherit from a parent class\e[0m'")
if 'healthy' not in JellyBean.__dict__.keys():
    os.system("echo '\e[32mCorrect, JellyBean inherits the healthy method\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, JellyBean should inherit the healthy method\e[0m'")
if 'super' in init_calls:
    os.system("echo '\e[32mCorrect, JellyBeans __init__ method is DRY the healthy method\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, JellyBeans __init__ method should inherit from Dessert\e[0m'")
if 'super' in delicious_calls:
    os.system("echo '\e[32mCorrect, JellyBeans delicious method inherits from Dessert\e[0m'")
else:
    os.system("echo '\e[31mIncorrect, JellyBeans delicious method should inherit from Dessert\e[0m'")


# In[ ]:




