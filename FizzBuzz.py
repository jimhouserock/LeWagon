#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function fizz_buzz which takes a single number as an argument, and returns a list of numbers from 1 to that number, but replaces some of them according to these rules:

#If the number is divisible by 3, then replace it with ‘Fizz’
#If the number is divisible by 5, then replace it with ‘Buzz’
#If the number is divisible by both 3 and 5, then replace it with ‘FizzBuzz’
#e.g.

#fizz_buzz(7)
# => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]

def fizz_buzz(num):
   final=[]
   
   for i in range(1,num+1):
       #print (i)
       if i%3 == 0 and i%5 == 0:
            final.append("FizzBuzz")
       elif i%3==0:
            final.append("Fizz")
       elif i%5==0:
            final.append("Buzz")
       else:
            final.append(i)
    
   return(final)


# In[ ]:




