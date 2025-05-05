#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary
1.2. Updating the values in dictionary
1.3. Accessing the value in dictionary
1.4. Create a nested loop dictionary
1.5. Access the values of nested loop dictionary
1.6. Print the keys present in a particular dictionary
1.7. Delete a value from a dictionary


# In[1]:


'''
Create a Dictionary with at least 5 key value pairs of the Student ID and Name
1.1. Adding the values in dictionary'''

# Creating a dictionary with 5 student ID and Name pairs
students = {
    "S101": "Abhishek",
    "S102": "Priya",
    "S103": "Ravi",
    "S104": "Sneha",
    "S105": "Karan"
}
students


# In[3]:


#1.1 Adding the values in dictionary

# Adding more student entries
students["S106"] = "Neha"
students["S107"] = "Amith"
students["S108"] = "Ram"

students


# In[4]:


#1.2 Upadting the values in Dictionary
# Original dictionary
students = {
    "S101": "Abhishek",
    "S102": "Priya",
    "S103": "Ravi",
    "S104": "Sneha",
    "S105": "Karan",
    "S106": "Neha",
    "S107": "Amit"
}

# Updating student names
students["S102"] = "Priyanka"   # Changed 'Priya' to 'Priyanka'
students["S105"] = "Karan Mehta"  # Added last name

# Print updated dictionary
print(students)


# In[5]:


#Accessing the value in dictionary

students = {
    "S101": "Abhishek",
    "S102": "Priyanka",
    "S103": "Ravi",
    "S104": "Sneha",
    "S105": "Karan Mehta",
    "S106": "Neha",
    "S107": "Amit"
}

# Accessing using square brackets
print(students["S101"])  # Output: Abhishek

# Accessing using get() method
print(students.get("S104"))  # Output: Sneha

# Using get() with a non-existing key to avoid error
print(students.get("S999", "Student not found"))  # Output: Student not found


# In[6]:


# Create a netsed loop inside the  dictionary


# Define classes and students
classes = ["Class A", "Class B"]
students = ["John", "Alice", "Bob"]
marks = [85, 90, 78]

# Initialize empty dictionary
school = {}

# Outer loop for each class
for cls in classes:
    school[cls] = {}  # Each class is a key, value is a dictionary

    # Inner loop for each student
    for i in range(len(students)):
        school[cls][f"S10{i+1}"] = {
            "Name": students[i],
            "Marks": marks[i]
        }

# Print the nested dictionary
print(school)



# In[7]:


#Access  the elemnt from the nested loop 


for cls, students in school.items():
    print(f"\n{cls}:")
    for student_id, info in students.items():
        name = info['Name']
        marks = info['Marks']
        print(f"  {student_id} - Name: {name}, Marks: {marks}")


# In[9]:


# Print the keys present in a particular dictionary


# Print all keys
print(students.keys())



# In[10]:


students = {
    "S101": "Abhishek",
    "S105": "Priya",
    "S103": "Ravi"
}

# Delete entry with key 'S102'
del students["S105"]

print(students)


# In[ ]:




