#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function roman_to_int It should take one argument, a string, and convert it into its corresponding integer eg:

#roman_to_int(‘IV’) #=> 4
#roman_to_int(‘XVI’) #=> 16
#roman_to_int(‘MI’) #=> 1001
#Hint - you might consider including 4/40/400 and 9/90/900 in your dictionary 😉

ROMAN_1NUM = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
ROMAN_2NUM = {
    "IV":4,
    "IX":9,
    "XL":40,
    "CD":400,
    "XC":90,
    "CM":900
}

def roman_to_int(roman):
    
    final= 0
    temp = roman.upper()
    count = 0

    
    
    for count in range(0,len(temp)):
        #print (count)
        #print(temp[count:count+2])
        if roman[count:count+2] in ROMAN_2NUM.keys():
            final = final + ROMAN_2NUM[roman[count:count+2]]
            temp=(temp.replace(roman[count:count+2],""))
            count = count + 1
            #print(temp)
            #print(count)
            #print (final)
     
    #print(temp)
    #print (str(final)+" first loop")

    for count in range(0, len(temp)):
        #print (temp[count:count+1])
        if temp[count:count+1] in ROMAN_1NUM.keys():
            final = final + ROMAN_1NUM[temp[count:count+1]]
            temp=(temp.replace(temp[count:count],""))
            #print (temp)
    #print (temp)
    return (final)

# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")
import os

print("Testing with 4")
if roman_to_int("IV") == 4:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 12")
if roman_to_int("XII") == 12:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 14")
if roman_to_int("XIV") == 14:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 19")
if roman_to_int("XIX") == 19:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 49")
if roman_to_int("XLIX") == 49:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 78")
if roman_to_int("LXXVIII") == 78:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 79")
if roman_to_int("LXXIX") == 79:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with 101")
if roman_to_int("CI") == 101:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing 499")
if roman_to_int("CDXCIX") == 499:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing 1006")
if roman_to_int("MVI") == 1006:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("Testing with 1989")
if roman_to_int("MCMLXXXIX") == 1989:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")


    
    
    
    


# In[ ]:




