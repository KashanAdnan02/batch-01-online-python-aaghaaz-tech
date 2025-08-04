# Assignment: Mastering Python Dictionary Methods with For Loops
# This assignment covers all Python dictionary methods, requiring the use of for loops to solve challenging problems.
# Each problem must be solved using the specified dictionary method and a for loop.
# Instructions: Write the code to achieve the expected output for each problem. Test your solutions thoroughly.

# Problem 1: clear() - Clear and Rebuild with Conditions
# Description: Given a dictionary of student grades, clear it and rebuild it using a for loop, including only students with grades above 70.
students = {'Alice': 85, 'Bob': 60, 'Charlie': 92, 'David': 45}
# Task: Use clear() to empty the dictionary, then use a for loop to add back only students with grades > 70 from the original data.
# Expected Output: {'Alice': 85, 'Charlie': 92}

# Problem 2: copy() - Create a Modified Copy
# Description: Create a copy of a dictionary of prices and use a for loop to increase each price by 10% if the item name contains the letter 'a'.
prices = {'apple': 1.0, 'banana': 2.0, 'cherry': 3.0, 'date': 4.0}
# Task: Use copy() to create a duplicate dictionary, then use a for loop to update prices for items with 'a' in their name.
# Expected Output: {'apple': 1.1, 'banana': 2.2, 'cherry': 3.0, 'date': 4.4}

# Problem 3: fromkeys() - Initialize and Populate with Calculated Values
# Description: Create a dictionary using fromkeys() with days of the week as keys, then use a for loop to assign each day a value representing the number of tasks (input as a list of task counts).
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
task_counts = [3, 0, 5, 2, 1]
# Task: Use fromkeys() to initialize the dictionary with None, then use a for loop to assign task counts to each day.
# Expected Output: {'Mon': 3, 'Tue': 0, 'Wed': 5, 'Thu': 2, 'Fri': 1}

# Problem 4: get() - Safe Summation
# Description: Given a dictionary of monthly expenses, use get() in a for loop to sum the expenses for a specific category across multiple months, handling missing keys safely.
expenses = {'Jan': {'food': 200, 'rent': 1000}, 'Feb': {'food': 250, 'utils': 150}, 'Mar': {'rent': 1000}}
# Task: Use a for loop with get() to calculate the total 'food' expenses across all months, defaulting to 0 for missing categories.
# Expected Output: Total food expenses: 450

# Problem 5: items() - Filter and Transform
# Description: Given a dictionary of products and quantities, use items() in a for loop to create a new dictionary with only products having quantities greater than 5, doubling their quantities.
inventory = {'pens': 10, 'books': 3, 'erasers': 7, 'pencils': 2}
# Task: Use items() in a for loop to create a new dictionary with products where quantity > 5, setting their values to quantity * 2.
# Expected Output: {'pens': 20, 'erasers': 14}

# Problem 6: keys() - Key-Based Validation
# Description: Given a dictionary of user IDs and names, use keys() in a for loop to check if all keys are valid numeric IDs (integers) and create a list of invalid (non-integer) keys.
users = {123: 'Alice', 'bob': 'Bob', 456: 'Charlie', '789abc': 'David'}
# Task: Use keys() in a for loop to identify and collect non-integer keys in a list.
# Expected Output: Invalid keys: ['bob', '789abc']

# Problem 7: values() - Count Specific Values
# Description: Given a dictionary of employee roles, use values() in a for loop to count how many employees are in a specific role (e.g., 'Manager').
employees = {'e1': 'Manager', 'e2': 'Developer', 'e3': 'Manager', 'e4': 'Analyst'}
# Task: Use values() in a for loop to count the number of 'Manager' roles.
# Expected Output: Number of Managers: 2

# Problem 8: pop() - Selective Removal
# Description: Given a dictionary of scores, use pop() in a for loop to remove entries where the score is below 50 and collect the removed values in a list.
scores = {'Alice': 45, 'Bob': 75, 'Charlie': 30, 'David': 80}
# Task: Use a for loop with pop() to remove entries with scores < 50 and store the removed scores in a list.
# Expected Output: Removed scores: [45, 30], Updated dictionary: {'Bob': 75, 'David': 80}

# Problem 9: popitem() - Sequential Removal with Processing
# Description: Given a dictionary of tasks and priorities, use popitem() in a for loop to remove all items one by one, collecting high-priority tasks (priority > 5) in a list.
tasks = {'task1': 8, 'task2': 3, 'task3': 7, 'task4': 4}
# Task: Use popitem() in a for loop to process all items, collecting tasks with priority > 5 in a list, and stop when the dictionary is empty.
# Expected Output: High-priority tasks: ['task1', 'task3']

# Problem 10: setdefault() - Initialize and Update
# Description: Given a list of words, use setdefault() in a for loop to create a dictionary counting the frequency of each word’s first letter.
words = ['apple', 'ant', 'banana', 'berry', 'cherry']
# Task: Use setdefault() in a for loop to build a dictionary where keys are first letters and values are counts of words starting with that letter.
# Expected Output: {'a': 2, 'b': 2, 'c': 1}

# Problem 11: update() - Merge and Increment
# Description: Given two dictionaries of item sales, use update() in a for loop to merge them, summing the values for common keys.
sales1 = {'apple': 10, 'banana': 5}
sales2 = {'banana': 3, 'orange': 7}
# Task: Use a for loop with update() to merge sales2 into sales1, adding values for shared keys.
# Expected Output: {'apple': 10, 'banana': 8, 'orange': 7}

# Problem 12: Nested Dictionary with Multiple Methods
# Description: Given a nested dictionary of departments and employee salaries, use a for loop with get(), items(), and setdefault() to create a new dictionary summarizing total salaries per department, handling missing departments.
company = {'HR': {'Alice': 50000, 'Bob': 60000}, 'IT': {'Charlie': 70000}}
# Task: Use a for loop with get(), items(), and setdefault() to calculate total salaries per department, adding a new department 'Sales' with no employees (total 0).
# Expected Output: {'HR': 110000, 'IT': 70000, 'Sales': 0}