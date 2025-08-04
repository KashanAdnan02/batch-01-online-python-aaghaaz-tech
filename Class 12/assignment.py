# Assignment: Learning Python's dict.fromkeys() Method
# The fromkeys() method creates a new dictionary with specified keys and a default value for all keys.
# Syntax: dict.fromkeys(keys, value)
# - keys: An iterable of keys (e.g., list, tuple, set)
# - value: A single value assigned to all keys (default is None if not specified)

# Problem 1: Create a Dictionary with Default Value
# Description: Use fromkeys() to create a dictionary with a list of fruits as keys and "Fresh" as the default value.
fruits = ['apple', 'banana', 'orange']
# Task: Create a dictionary where each fruit is a key with value "Fresh".
# Expected Output: {'apple': 'Fresh', 'banana': 'Fresh', 'orange': 'Fresh'}
problem1 = dict.fromkeys(fruits, 'Fresh')
print("Problem 1:", problem1)

# Problem 2: Create a Dictionary with Default None
# Description: Use fromkeys() to create a dictionary from a tuple of numbers (1, 2, 3, 4) as keys with no value specified.
numbers = (1, 2, 3, 4)

# From Keys
# Task: Create a dictionary with these numbers as keys and None as the default value.
# Expected Output: {1: None, 2: None, 3: None, 4: None}

# Problem 3: Create a Dictionary from a String
# Description: Use fromkeys() to create a dictionary where each character in the string "hello" is a key, with 
# Task: Create a dictionary with each unique character as a key and 0 as the value.
# Expected Output: {'h': 0, 'e': 0, 'l': 0, 'o': 0}


# Problem 4: Handle Duplicate Keys
# Description: Use fromkeys() with a list containing duplicate values (e.g., ['a', 'b', 'a', 'c']) and set the default value to 100.
# Task: Create a dictionary and observe how fromkeys() handles duplicates.
# Expected Output: {'a': 100, 'b': 100, 'c': 100}







# Problem 5: Using a Set as Keys
# Description: Use fromkeys() with a set of mixed types (e.g., {1, 'x', 2, 'y'}) and set the default value to 'Unknown'.
mixed_keys = {1, 'x', 2, 'y'}
# Task: Create a dictionary with these keys and 'Unknown' as the value.
# Expected Output: {1: 'Unknown', 'x': 'Unknown', 2: 'Unknown', 'y': 'Unknown'}



# Problem 6: Create a Scoreboard
# Description: Create a scoreboard for a game with players ['Alice', 'Bob', 'Charlie'] where each starts with a score of 0.
players = ['Alice', 'Bob', 'Charlie']
# Task: Use fromkeys() to create a dictionary with players as keys and 0 as the default score.
# Expected Output: {'Alice': 0, 'Bob': 0, 'Charlie': 0}


# Problem 7: Empty Iterable
# Description: Try using fromkeys() with an empty list as the keys and 'Empty' as the default value.

# Task: Create a dictionary and observe the result.
# Expected Output: {}




# Problem 8: Mutable Default Value Issue
# Description: Use fromkeys() with a list [1, 2, 3] as keys and an empty list [] as the default value. Then modify the list for one key.
keys = [1, 2, 3]
# Task: Create the dictionary, append 'test' to the list of key 1, and print the result. Explain why all keys are affected.
# Expected Output: {1: ['test'], 2: ['test'], 3: ['test']}


# Note: All keys share the same list object because fromkeys() uses the same reference for mutable default values.

# Problem 9: Create a Configuration Dictionary
# Description: Create a dictionary for configuration settings with keys ['host', 'port', 'user'] and default value 'TBD'.
config_keys = ['host', 'port', 'user']
# Task: Use fromkeys() to create the dictionary.
# Expected Output: {'host': 'TBD', 'port': 'TBD', 'user': 'TBD'}



# Problem 10: Combine fromkeys() with User Input
# Description: Ask the user for a comma-separated list of names, split it into a list, and create a dictionary with those names as keys and 'Guest' as the default value.
user_input = input("Enter names (comma-separated): ")
names = user_input.split(',')
# Task: Use fromkeys() to create a dictionary with the names as keys and 'Guest' as the value.
# Example Input: "John, Jane, Doe"
# Expected Output: {'John': 'Guest', 'Jane': 'Guest', 'Doe': 'Guest'}

