#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Code a manual_shuffle function:

#The function should take one argument, a list, and return a new list with all the items of your original list in a new, randomized order
#Do Not use any built in list methods to manipulate the order such as sort()
#Do Not use the built in shuffle method in python’s random library (let’s do it the hard way). But you might find some other helpful methods in there, we imported the random library for you at the top of the file 😉
#Hint: You should not makes changes to the original List, the copy method will come in handy. One approach could be to create a new empty array B, and until A is empty, randomly select an index in A, append the element in A at that index into B, then delete that index in A. Proceed until A is empty. B should contain the new shuffled array!
    
    
import random
from random import randrange, sample

def manual_shuffle(lis):

    final=[]
    lis_copy=lis.copy()
    
    while len(lis_copy)>0:
        final.append(lis_copy.pop(randrange(len(lis_copy))))
        
    return final

