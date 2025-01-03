# Advanced Python: Dictionaries

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python dictionaries.
We will explore:
1. Dictionary basics - Creation, accessing, and updating.
2. All dictionary methods and their uses.
3. Integrating dictionaries with lists and tuples for complex data structures.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Dictionary Basics
# ----------------------------
# Dictionaries in Python are unordered collections that store data in key-value pairs.

# Example 1: Creating and Using Dictionaries
simple_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(simple_dict["city"])
# print(simple_dict['address'])  # Accessing value by key
print(simple_dict.get('age', 0))  # Accessing value by key
print(simple_dict.get('address', 'Texas'))  # Accessing value by key


# Updating dictionary
simple_dict['age'] = 31  # Updates the age
simple_dict['country'] = 'USA'  # Adds a new key-value pair
# print("Updated Dictionary: ", simple_dict)

# Dictionary Methods
# keys(), values(), items()
print(simple_dict.keys())  # Prints all keys
print(simple_dict.values())  # Prints all values
print(simple_dict.items())  # Prints all key-value pairs as tuples

# get()
print(simple_dict.get('name'))  # Returns 'John'

# pop()
removed_value = simple_dict.pop('country')  # Removes 'country' key and returns its value
print("Removed Value:", removed_value)
print("Dictionary after pop(): ", simple_dict)

# popitem()
last_item = simple_dict.popitem()  # Removes and returns the last inserted key-value pair
print("Last Item:", last_item)
print("Dictionary after popitem(): ", simple_dict)

# update()
simple_dict.update({'age': 32, 'email': 'john@example.com'})  # Updates the dictionary
print("Dictionary after update(): ", simple_dict)

# clear()
# simple_dict.clear()  # Empties the dictionary
# print("Dictionary after clear(): ", simple_dict)

# copy()
dict_copy = simple_dict.copy()  # Creates a shallow copy of the dictionary
print("Dictionary Copy: ", dict_copy)

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.
# Creating a dictionary representing a student
student = {
    'name': 'Alice',
    'roll_number': 101,
    'grades': {'Math': 85, 'Science': 90, 'English': 78}
}

# Printing the original dictionary
print("Original Student Dictionary:")
print(student)

# Adding a new subject to the grades
student['grades']['History'] = 88
print("\nAfter Adding a New Subject:")
print(student)

# Modifying the grade for an existing subject
student['grades']['Math'] = 95
print("\nAfter Modifying a Grade:")
print(student)

# Removing a subject from the grades
removed_grade = student['grades'].pop('English', None)
print("\nAfter Removing a Subject:")
print("Removed Grade (English):", removed_grade)
print(student)

# Adding a new key-value pair to the student dictionary
student['email'] = 'alice@example.com'
print("\nAfter Adding a New Key-Value Pair (Email):")
print(student)

# Removing the 'roll_number' key
removed_roll_number = student.pop('roll_number', None)
print("\nAfter Removing Roll Number:")
print("Removed Roll Number:", removed_roll_number)
print(student)

# Printing all keys, values, and items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())



# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------
# Dictionaries can be used with lists and tuples to create complex data structures.

# Example 2: List of Dictionaries
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 78}
]

# Sorting list of dictionaries by grade
students_sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Students sorted by grade: ", students_sorted_by_grade)

# Example 3: Dictionary of Tuples
# Using tuples as keys
coordinates_info = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Dictionary with student names as keys and lists of grades as values
student_grades = {
    'Alice': [85, 90, 78],
    'Bob': [92, 88, 84],
    'Charlie': [75, 80, 70],
    'Diana': [88, 85, 91]
}

# Calculate the average grade for each student
average_grades = {name: sum(grades) / len(grades) for name, grades in student_grades.items()}

# Printing the results
print("Average grades for each student:")
for name, avg_grade in average_grades.items():
    print(f"{name}: {avg_grade:.2f}")


# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.
