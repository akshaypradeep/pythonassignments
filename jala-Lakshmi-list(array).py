#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a function to add integer values of an array
2. Write a function to calculate the average value of an array of integers
3. Write a program to find the index of an array element
4. Write a function to test if array contains a specific value
5. Write a function to remove a specific element from an array
6. Write a function to copy an array to another array
7. Write a function to insert an element at a specific position in the array
8. Write a function to find the minimum and maximum value of an array
9. Write a function to reverse an array of integer values
10. Write a function to find the duplicate values of an array
11. Write a program to find the common values between two arrays
12. Write a method to remove duplicate elements from an array
13. Write a method to find the second largest number in an array
14. Write a method to find the second largest number in an array
15. Write a method to find number of even number and odd numbers in an array
16. Write a function to get the difference of largest and smallest value
17. Write a method to verify if the array contains two specified elements(12,23)
18. Write a program to remove the duplicate elements and return the new array


# In[1]:


#1.Write a function to add integer values of an list

def sum_of_integers(input_list):
    """
    Adds only integer values from the input list using a loop.
    """
    total = 0
    for item in input_list:
        if isinstance(item, int):
            total += item
    return total

# Example usage:
my_list = [10, 'b', 20, 3.14, 30]
result = sum_of_integers(my_list)
print("Sum of integers:", result)  # Output: Sum of integers: 60




# In[9]:


#Write a function to calculate the average value of an array of integers

def average_func(my_list):
    total=0
    count=0
    for i in my_list:
        if isinstance(i, int):
            total +=i
            count += 1
    avg=total/count     
    return avg   

my_list=[2,3,4, "Welcome",8.89,"9"]

average_func(my_list)
            


# In[15]:


# Write a function to test if array contains a specific value

def specific_value(my_list,n):
    for i in my_list:
        #if isinstance(i,int):
            if i == n:
               # print(i)
                return i
            
my_list=[2,3,4, "Welcome",8.89,"9"] 
specific_value(my_list, "Welcome")


# In[18]:


#Write a function to remove a specific element from an array
def remove_value(my_list, n):
    for i in my_list:
        if i==n:
            my_list.remove(n)
            return my_list

my_list=[2,3,4, "Welcome",8.89,"9"] 
remove_value(my_list, "Welcome")        


# In[20]:


#Write a function to copy an array to another array
def copy_list(source):
    dest=source.copy()
    return dest
    
source = [1, 2, 3, 4, 5,"Ram"]
dest = copy_list(source)
print(dest)


# In[21]:


def copy_array(source):
    return source[:]

# Example:
original = [10, 20, 30]
copied = copy_array(original)
print("Copied array:", copied)


# In[23]:


#Write a function to insert an element at a specific position in the array
def insert_ele(my_list,i,n):
    my_list[i]=n
    print(my_list)
    return my_list      

insert_ele(my_list, 3, 65)
my_list=[2,3,4, "Welcome",8.89,"9"]


# In[25]:


def insert_ele(my_list, i, n):
    """
    Inserts element n at index i in my_list without replacing existing elements.
    """
    my_list.insert(i, n)
    return my_list


my_list = [2, 3, 4, "Welcome", 8.89, "9"]
result = insert_ele(my_list, 3, 65)
print(result)  # Output: [2, 3, 4, 65, 'Welcome', 8.89, '9']


# In[45]:


#Write a function to find the minimum and maximum value of an array
def min_value(my_list):
    min=my_list[0]
    for i in my_list:
        if i<min:
            min=i
    return min

my_list=[2,3,4,5,5,1]
min_value(my_list)        
#my_list=[2,3,4,5,5,1]


def max_value(my_list):
    max=my_list[0]
    for i in my_list:
        if i>max:
            max=i
            #print(i)
    return max

my_list=[2,3,4,5,5,1]
max_value(my_list)        
#my_list=[2,3,4,5,5,1]


# In[49]:


#Write a function to reverse an array of integer values
def reverse_list(arr):
    return arr[::-1]

# Example usage
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print("Reversed:", reversed_list)  # Output: [5, 4, 3, 2, 1]


# In[50]:


#Write a function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example usage
my_list = [1, 2, 3, 2, 4, 5, 1, 6]
print("Duplicates:", find_duplicates(my_list))  # Output: [1, 2]


# In[53]:


a=[1,2,3,4,5]
a[::-1]
print(a)


# In[54]:


#Write a program to find the common values between two arrays

def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))


array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

common = find_common_elements(array1, array2)
print("Common elements:", common)  # Output: [3, 4, 5]


# In[55]:


# Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))


my_list = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(my_list))  
# Output (order not guaranteed): [1, 2, 3, 4, 5]


# In[56]:


#Write a method to find the second largest number in an array
def second_largest(arr):
    unique = list(set(arr))  # Remove duplicates
    if len(unique) < 2:
        return None  # No second largest if fewer than 2 unique elements
    unique.sort(reverse=True)
    return unique[1]

# Example usage
my_list = [10, 20, 4, 45, 99, 99]
print("Second largest:", second_largest(my_list))  # Output: 45


# In[ ]:


#Write a method to find the second smallest number in an array
def second_smallest(arr):
    unique = list(set(arr))  # Remove duplicates
    if len(unique) < 2:
        return None  # No second smallest if fewer than 2 unique elements
    unique.sort()
    return unique[1]

# Example usage
my_list = [10, 20, 4, 45, 99, 99]
print("Second smallest:", second_smallest(my_list))  # Output: 10


# In[57]:


#Write a method to find number of even number and odd numbers in an array

def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    
    for num in arr:
        if num % 2 == 0:  # Check if number is even
            even_count += 1
        else:  # If it's not even, it's odd
            odd_count += 1
            
    return even_count, odd_count

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
even, odd = count_even_odd(my_list)
print("Even numbers:", even)  # Output: Even numbers: 4
print("Odd numbers:", odd)    # Output: Odd numbers: 4


# In[4]:


#Write a function to get the difference of largest and smallest value

def difference_max_min(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers) - min(numbers)

# Example usage:
values = [10, 3, 15, 22, 8]
result = difference_max_min(values)
print("Difference between largest and smallest:", result)


# In[7]:


#Write a method to verify if the array contains two specified elements(12,23)

def specify_elemnt(my_list,a,b):
    for i in my_list:
        if i==a or b:
            print("Elements are present")
        return a,b        
            
            
my_list=[3,4,5,12,22,23,78,23] 
specify_elemnt(my_list,12,23)


# In[11]:


#Write a program to remove the duplicate elements and return the new array
def remove_duplicate(my_list):
    new_list=[]
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
        
my_list=[1,2,3,2,3,2,4]        
remove_duplicate(my_list)        


# In[ ]:




