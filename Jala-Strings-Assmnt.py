#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
1. Different ways creating a string
2. Concatenating two strings using + operator
3. Finding the length of the string
4. Extract a string using Substring
5. Searching in strings using index()
6. Matching a String Against a Regular Expression With matches()
7. Comparing strings
8. startsWith(), endsWith() and compareTo()
9. Trimming strings with strip()
10. Replacing characters in strings with replace()
11. Splitting strings with split()
12. Converting integer objects to Strings
13. Converting to uppercase and lowercase

'''


# In[1]:


#Different ways to create a  string

str1 = 'Ram'
print(str1)  # Output: Hello


# In[2]:


str3 = '''This is
a multi-line
string'''
print(str3)


# In[3]:


num = 123
str4 = str(num)
print(str4)        # Output: '123'
print(type(str4))  # Output: <class 'str'>
    


# In[4]:


#Concatenating two strings using + operator

Str1="Seetha"
Str2="Rama"


print(Str1+Str2)


# In[5]:


##Finding the length of the string

print(len(Str1))


# In[6]:


##Extract a string using Substring


Str1="Hare Rama Hare Krushna"

str2=Str1[:9]
print(str2)


# In[7]:


#Searching in strings using index()

text = "Welcome to Python programming"

# Search for "Python"
position = text.index("Python")
print("Index of 'Python':", position)


# In[8]:


#Matching a String Against a Regular Expression With matches()
import re

pattern = r"[A-Za-z]+"
text = "HelloWorld"

# Check if entire string matches the pattern
if re.fullmatch(pattern, text):
    print("Match found!")
else:
    print("No match.")


# In[9]:


#Comparing strings

str1 = "Apple"
str2 = "Banana"
str3 = "Apple"

print(str1 == str2)  # False
print(str1 == str3)  # True
print(str1 != str2)  # True


print("Apple" < "Banana")   # True
print("Orange" > "Mango")   # True


str1 = "Python"
str2 = "python"

print(str1.lower() == str2.lower())      # True
print(str1.casefold() == str2.casefold())  # Best for international text


# In[10]:


import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
print(locale.strcoll("ä", "z"))  # Considers language rules


# In[ ]:


#startsWith(), endsWith() and compareTo()
text = "Python Programming"

print(text.startswith("Python"))  # True
print(text.startswith("program")) # False (case-sensitive)

print(text.endswith("ming"))     # True
print(text.endswith("Program"))  # False

str1 = "apple"
str2 = "banana"

if str1 == str2:
    result = 0
elif str1 < str2:
    result = -1
else:
    result = 1

print(result)  # Output: -1


# In[12]:


def compareTo(str1, str2):
    """
    Mimics Java's compareTo() method.
    Returns:
        0  if str1 == str2
       <0  if str1 < str2
       >0  if str1 > str2
    """
    min_len = min(len(str1), len(str2))
    
    for i in range(min_len):
        if str1[i] != str2[i]:
            return ord(str1[i]) - ord(str2[i])
    
    return len(str1) - len(str2)


# In[13]:


print(compareTo("apple", "apple"))    # 0
print(compareTo("apple", "banana"))   # negative value (e.g., -1)
print(compareTo("banana", "apple"))   # positive value (e.g., 1)
print(compareTo("app", "apple"))      # negative value (shorter string)


# In[14]:


#Trimming strings with strip()

text = "   Hare Rama   "
trimmed = text.strip()
print(trimmed)  
print(text.lstrip())  
print(text.rstrip())


# In[17]:


#Replacing characters in strings with replace()

text = "Python is fun. Python is powerful."
updated = text.replace("Python", "Java")
print(updated)


# In[18]:


#Splitting strings with split()
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  



# In[ ]:


#Converting integer objects to Strings
num = 123
str_num = str(num)
print(str_num)         # Output: '123'
print(type(str_num))   # Output: <class 'str'>


# In[19]:


#Converting integer objects to Strings
num = 789
str_num = "{}".format(num)
print(str_num)         



# In[22]:


#Converting to uppercase and lowercase

stri="rama krushna vedavyasa"

Str_u=stri.upper()
Str_l=Str_u.lower()
print(Str_u)
print(Str_l)


# In[23]:


a = "Python"
b = "python"

print(a.lower() == b.lower())      # True
print(a.casefold() == b.casefold())  # Best for international text


# In[24]:


text = "welcome to python"
print(text.title())  # Output: Welcome To Python


# In[ ]:




