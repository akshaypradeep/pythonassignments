#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function for arithmetic operators(+,-,*,/)


a=10
b=20
c=30

print("Addition operation:",a+b)
print("Subtraction operation:", c-b)
print("Multiplication operation:", a*b)
print("Divison operation:", c/b)


# In[4]:


#Write a method for increment and decrement operators(++, --)
a=10
b=20

a+=1
b-=1
print("increment operation:", a)
print("Decrement operation:", b)


# In[5]:


#Write a program to find the two numbers equal or not.

a=10
b=20

if a==b:
    print("a and b are equal")
else:
    print("a and b are not equal")


# In[ ]:


#Program for relational operators (<,<==, >, >==)

def relational_operators(a, b):
    print(f"{a} < {b} :", a < b)
    print(f"{a} <= {b} :", a <= b)
    print(f"{a} > {b} :", a > b)
    print(f"{a} >= {b} :", a >= b)

# Example usage
a = 10
b = 20

relational_operators(a, b)


# In[7]:


#5. Print the smaller and larger number

def larger_smaller(a,b):
    if a<b:
        print("a is smaller number")
    elif a>b:
        print("a is larger number")
    else:
        print("a & b both are equal")
        
        
larger_smaller(10,5)        


# In[8]:


def larger_smaller(a, b):
    if a < b:
        print(f"{a} is smaller than {b}")
    elif a > b:
        print(f"{a} is larger than {b}")
    else:
        print(f"{a} and {b} are equal")

# Example usage
larger_smaller(10, 5)


# In[ ]:


#Loops


# In[11]:


#Write a program to print “Bright IT Career” ten times using for loop


for i in range(1,11):
    print(i,"Bright IT Career")


# In[20]:


#Write a java program to print 1 to 20 numbers using the while loop.
n=1;
while(n<=20):
     print(n,end=", ") 
     n+=1   


# In[21]:


#Program to equal operator and not equal operators

def equal_not_equal(a, b):
    if a == b:
        print(f"{a} is equal to {b}")
    else:
        print(f"{a} is not equal to {b}")

# Example usage
equal_not_equal(10, 10)
equal_not_equal(10, 5)


# In[22]:


#Write a program to print the odd and even numbers.
def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Example usage
odd_even(7)
odd_even(8)



# In[23]:


#Write a program to print largest number among three numbers.

def largest_among_three(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is the largest number")
    elif b >= a and b >= c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")

# Example usage
largest_among_three(10, 25, 15)



# In[24]:


#Write a program to print even number between 10 and 20 using while


def even_numbers_while():
    number = 10
    while number <= 20:
        if number % 2 == 0:
            print(number)
        number += 1

# Example usage
even_numbers_while()


# In[ ]:


#Write a program to print 1 to 10 using the do-while loop statement.

def print_1_to_10():
    number = 1
    while True:
        print(number)
        number += 1
        if number > 10:
            break

# Example usage
print_1_to_10()


# In[27]:


#Write a program to find Armstrong number or not
def is_armstrong(number):
    # Convert number to string to find number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate sum of digits each raised to the power of num_digits
    sum_of_powers = 0
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits

    # Compare sum with original number
    if sum_of_powers == number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is NOT an Armstrong number.")

# Example usage
is_armstrong(153)
is_armstrong(123)


# In[28]:


def prime_or_not(number):
    if number <= 1:
        print(f"{number} is NOT a prime number.")
        return

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is NOT a prime number.")
            return

    print(f"{number} is a prime number.")

# Example usage
prime_or_not(7)
prime_or_not(10)


# In[29]:


#Write a program to palindrome or not.


def is_palindrome(value):
    # Convert the value to string to handle both numbers and strings
    value_str = str(value)
    
    # Check if the string is equal to its reverse
    if value_str == value_str[::-1]:
        print(f"{value} is a palindrome.")
    else:
        print(f"{value} is NOT a palindrome.")

# Example usage
is_palindrome(121)       # Number
is_palindrome("madam")   # String
is_palindrome("hello")   # String


# In[30]:


#Program to check whether a number is EVEN or ODD using switch

def check_even_odd(number):
    # Use a dictionary to simulate the switch
    switch = {
        True: f"{number} is Even",
        False: f"{number} is Odd"
    }

    # Check if the number is even or odd using modulo operator
    print(switch[number % 2 == 0])

# Example usage
check_even_odd(10)
check_even_odd(7)


# In[31]:


#Print gender (Male/Female) program according to given M/F using switch

def print_gender(gender):
    # Simulating switch using a dictionary
    switch = {
        'M': "Male",
        'F': "Female"
    }

    # Use dictionary get method to get the result, with a default value if invalid input
    print(switch.get(gender, "Invalid input"))

# Example usage
print_gender('M')  # Output: Male
print_gender('F')  # Output: Female
print_gender('X')  # Output: Invalid input


# In[ ]:




