#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Implement your simple_calculator function below
#Specs
#Our function should take a single list of strings as an argument, containing our first opperand, followed by an operator and then the 2nd operand. eg:
#simple_calculator(['1', '+', '1' ]) #=> 2
#The function should return 'Please enter valid format: [Operand, Operator, Operand]' for arguments that don’t match the required format
#The funtion should work with the following simple operators +, -, *, /, %, and should return'Please enter a valid operator [ +, -, /, *, % ]' if any other operators are passed
#Assume that the operands are always numeric (floats or integers); no need to validate their data type

def simple_calculator(list):
    
    
    if len(list)>3 or len(list) <3 :
        return("Please enter valid format: [Operand, Operator, Operand]")
    elif str(list[1]) not in "+-/*%":
        return( "Please enter a valid operator [ +, -, /, *, % ]")
    elif list[1]== "+":
        final=int(list[0])+int(list[2])
    elif list[1]=="-":
        final=float(list[0])-float(list[2])
    elif list[1]=="*":
        final=int(list[0])*int(list[2])
    elif list[1]=="/":
        final=int(list[0])/int(list[2])
    elif list[1]=="%":
        final=int(list[0])%int(list[2])
    else: 
        return "Please enter valid format: [Operand, Operator, Operand]"
    return(final)


# In[ ]:




