import streamlit as st
import sys
from io import StringIO
import traceback

st.set_page_config(page_title="Python Basics for Beginners", layout="wide")

st.title("Python Basics for Beginners")
st.markdown("An interactive guide to learn Python fundamentals")

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Select a topic:", [
    "Introduction",
    "Variables",
    "Data Types",
    "Strings",
    "Numbers",
    "Lists",
    "Tuples",
    "Dictionaries",
    "Sets",
    "Operators",
    "Conditional Statements",
    "Common Errors"
])


# Function to run code safely and capture output
def run_code(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    try:
        exec(code)
        sys.stdout = old_stdout
        return redirected_output.getvalue(), None
    except Exception as e:
        sys.stdout = old_stdout
        error_msg = traceback.format_exc()
        return redirected_output.getvalue(), error_msg


# Introduction Section
if section == "Introduction":
    st.header("Welcome to Python Basics!")
    st.markdown("""
    Python is a powerful, easy-to-learn programming language. It's great for beginners because of its simple syntax and readability.

    In this interactive guide, you'll learn:
    - How to work with variables
    - Different data types and structures
    - How to perform operations
    - How to use conditional statements

    Each section includes examples that you can run and modify to see the results immediately!
    """)

    st.subheader("Your First Python Program")
    code = '''print("Hello, World!")'''

    st.code(code, language="python")

    if st.button("Run 'Hello World'"):
        output, error = run_code(code)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Variables Section
elif section == "Variables":
    st.header("Variables in Python")
    st.markdown("""
    Variables are containers for storing data values. In Python, you don't need to declare variables with specific types.

    **Rules for Python variables:**
    - A variable name must start with a letter or the underscore character
    - A variable name cannot start with a number
    - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
    - Variable names are case-sensitive (age, Age and AGE are different variables)
    """)

    st.subheader("Example 1: Creating Variables")
    code1 = '''# Valid variable names
name = "John"
age = 25
_private = "Secret"
user_score = 95.5

# Displaying variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Private data: {_private}")
print(f"User score: {user_score}")'''

    st.code(code1, language="python")

    if st.button("Run Variables Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Example 2: Invalid Variable Names")
    code2 = '''# This will cause an error
1name = "John"  # Variable name cannot start with a number'''

    st.code(code2, language="python")

    if st.button("Run Variables Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
            st.info("Correction: Variable names cannot start with numbers. Use 'name1' instead of '1name'.")
        else:
            st.success(f"Output: {output}")

    st.subheader("Example 3: Variable Reassignment")
    code3 = '''# Variables can be reassigned
x = 10
print(f"Initial value: {x}")

x = 20
print(f"After reassignment: {x}")

x = "Hello"
print(f"Changed data type: {x}")'''

    st.code(code3, language="python")

    if st.button("Run Variables Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Data Types
elif section == "Data Types":
    st.header("Python Data Types")
    st.markdown("""
    Python has several built-in data types:

    1. **Text Type**: `str`
    2. **Numeric Types**: `int`, `float`, `complex`
    3. **Sequence Types**: `list`, `tuple`, `range`
    4. **Mapping Type**: `dict`
    5. **Set Types**: `set`, `frozenset`
    6. **Boolean Type**: `bool`
    7. **None Type**: `NoneType`

    Let's explore each of these types with examples.
    """)

    st.subheader("Checking Data Types with type()")
    code = '''# Different data types
text = "Hello"
number = 42
decimal = 3.14
is_active = True
nothing = None

# Check the type of each variable
print(f"text is {type(text)}")
print(f"number is {type(number)}")
print(f"decimal is {type(decimal)}")
print(f"is_active is {type(is_active)}")
print(f"nothing is {type(nothing)}")'''

    st.code(code, language="python")

    if st.button("Run Data Types Example"):
        output, error = run_code(code)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Type Conversion")
    code2 = '''# Converting between types
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(f"String '123' converted to integer: {num_int}")

float_num = 9.99
int_num = int(float_num)  # Convert float to integer (truncates decimal part)
print(f"Float 9.99 converted to integer: {int_num}")

age = 30
age_str = str(age)  # Convert integer to string
print(f"Integer 30 converted to string: {age_str}, type: {type(age_str)}")

# This will cause an error
num_error = int("hello")  # Cannot convert non-numeric string to integer'''

    st.code(code2, language="python")

    if st.button("Run Type Conversion Example"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
            st.info(
                "Correction: The string 'hello' cannot be converted to an integer because it doesn't contain numeric characters. Use only numeric strings with int().")
        else:
            st.success(f"Output: {output}")

# Strings
elif section == "Strings":
    st.header("Python Strings")
    st.markdown("""
    Strings are sequences of characters enclosed in quotes (single or double).

    **Key features:**
    - Strings are immutable (cannot be changed after creation)
    - You can access individual characters using indexing
    - Python strings support slicing to get substrings
    - Many built-in methods for string manipulation
    """)

    st.subheader("String Creation and Basic Operations")
    code1 = '''# Creating strings
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a multi-line
string that spans
multiple lines."""

# Concatenation
greeting = single_quotes + " " + double_quotes
print(f"Concatenated string: {greeting}")

# String length
print(f"Length of greeting: {len(greeting)}")

# Accessing characters (indexing)
print(f"First character: {greeting[0]}")
print(f"Last character: {greeting[-1]}")

# Slicing
print(f"First five characters: {greeting[0:5]}")
print(f"From 6th character to end: {greeting[6:]}") 
'''

    st.code(code1, language="python")

    if st.button("Run String Basics Example"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("String Methods")
    code2 = '''# Common string methods
text = "  Python Programming  "

# Remove whitespace
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")

# Change case
print(f"Uppercase: '{text.upper()}'")
print(f"Lowercase: '{text.lower()}'")

# Replace
print(f"Replace 'P' with 'J': '{text.replace('P', 'J')}'")

# Split into list
sentence = "Python is awesome"
words = sentence.split()
print(f"Split result: {words}")

# Find substrings
print(f"Position of 'Programming': {text.find('Programming')}")

# Check content
print(f"Starts with 'Python'?: {text.strip().startswith('Python')}")
print(f"Ends with 'ming'?: {text.strip().endswith('ming')}")
'''

    st.code(code2, language="python")

    if st.button("Run String Methods Example"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("String Error Example")
    code3 = '''# Common string error - trying to modify a string
text = "Python"
text[0] = "J"  # This will cause an error because strings are immutable

print(text)'''

    st.code(code3, language="python")

    if st.button("Run String Error Example"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
            st.info(
                "Correction: Strings in Python are immutable, meaning they cannot be changed after creation. To change a string, you need to create a new one: `text = 'J' + text[1:]`")
        else:
            st.success(f"Output: {output}")

# Numbers
elif section == "Numbers":
    st.header("Python Numbers")
    st.markdown("""
    Python has three numeric types:

    1. **int**: Integer numbers (whole numbers without decimals)
    2. **float**: Floating-point numbers (decimal numbers)
    3. **complex**: Complex numbers (with real and imaginary parts)

    Let's explore these types with examples.
    """)

    st.subheader("Integers and Floats")
    code1 = '''# Integer examples
x = 10
y = -5
z = 0
big_num = 1_000_000  # Underscore for readability

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")
print(f"z = {z}, type: {type(z)}")
print(f"big_num = {big_num}, type: {type(big_num)}")

# Float examples
a = 3.14
b = -0.001
c = 2.0
scientific = 1.23e5  # Scientific notation (123000.0)

print(f"a = {a}, type: {type(a)}")
print(f"b = {b}, type: {type(b)}")
print(f"c = {c}, type: {type(c)}")
print(f"scientific = {scientific}, type: {type(scientific)}")
'''

    st.code(code1, language="python")

    if st.button("Run Numbers Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Number Operations")
    code2 = '''# Basic arithmetic operations
a, b = 10, 3

# Addition
print(f"{a} + {b} = {a + b}")

# Subtraction
print(f"{a} - {b} = {a - b}")

# Multiplication
print(f"{a} * {b} = {a * b}")

# Division (returns float)
print(f"{a} / {b} = {a / b}")

# Floor division (returns int)
print(f"{a} // {b} = {a // b}")

# Modulus (remainder)
print(f"{a} % {b} = {a % b}")

# Exponentiation
print(f"{a} ** {b} = {a ** b}")

# Order of operations
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")

result_with_parentheses = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result_with_parentheses}")
'''

    st.code(code2, language="python")

    if st.button("Run Numbers Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Number Errors and Precision")
    code3 = '''# Division by zero error
a = 10
b = 0
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# Float precision issues
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # May not be exactly 0.3 due to floating-point precision

# Handling large numbers
large_number = 10**20
print(f"10^20 = {large_number}")
'''

    st.code(code3, language="python")

    if st.button("Run Numbers Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Lists
elif section == "Lists":
    st.header("Python Lists")
    st.markdown("""
    Lists are ordered, changeable collections that can contain items of different data types.

    **Key features:**
    - Created with square brackets []
    - Items are ordered, indexed (starting from 0)
    - Lists are mutable (can be changed after creation)
    - Can contain duplicates and different data types
    - Can be nested (lists within lists)
    """)

    st.subheader("Creating and Accessing Lists")
    code1 = '''# Creating lists
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "Hello", 3.14, True]
empty_list = []
nested_list = [1, 2, ["a", "b", "c"], 3]

# Accessing items
print(f"fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Accessing nested lists
print(f"Nested list: {nested_list}")
print(f"Nested item 'b': {nested_list[2][1]}")

# List length
print(f"Number of fruits: {len(fruits)}")
'''

    st.code(code1, language="python")

    if st.button("Run Lists Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Modifying Lists")
    code2 = '''# List operations
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

# Adding items
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert at position 1: {fruits}")

# Removing items
fruits.remove("banana")
print(f"After removing 'banana': {fruits}")

popped_fruit = fruits.pop()  # Removes last item
print(f"Popped item: {popped_fruit}")
print(f"After pop: {fruits}")

# Changing items
fruits[0] = "pear"
print(f"After changing first item: {fruits}")

# List concatenation
more_fruits = ["kiwi", "mango"]
all_fruits = fruits + more_fruits
print(f"Combined list: {all_fruits}")
'''

    st.code(code2, language="python")

    if st.button("Run Lists Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("List Methods and Operations")
    code3 = '''# More list operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original list: {numbers}")

# Sorting
numbers.sort()
print(f"Sorted: {numbers}")

# Reversing
numbers.reverse()
print(f"Reversed: {numbers}")

# Counting occurrences
print(f"Count of 1: {numbers.count(1)}")

# Finding index
print(f"Index of 5: {numbers.index(5)}")

# Slicing
print(f"First three items: {numbers[0:3]}")
print(f"Every second item: {numbers[::2]}")
print(f"Reversed list using slicing: {numbers[::-1]}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares using list comprehension: {squares}")

# Common error - index out of range
try:
    value = numbers[20]  # This will cause an error
    print(value)
except IndexError:
    print("Error: Index out of range")
'''

    st.code(code3, language="python")

    if st.button("Run Lists Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Tuples
elif section == "Tuples":
    st.header("Python Tuples")
    st.markdown("""
    Tuples are ordered, unchangeable collections that can contain items of different data types.

    **Key features:**
    - Created with parentheses ()
    - Items are ordered, indexed (starting from 0)
    - Tuples are immutable (cannot be changed after creation)
    - Can contain duplicates and different data types
    - Can be nested (tuples within tuples)

    The main difference between lists and tuples is that tuples are immutable.
    """)

    st.subheader("Creating and Accessing Tuples")
    code1 = '''# Creating tuples
colors = ("red", "green", "blue")
mixed_tuple = (1, "Hello", 3.14, True)
single_item_tuple = (42,)  # Note the comma
empty_tuple = ()
nested_tuple = (1, 2, ("a", "b", "c"), 3)

# Accessing items
print(f"colors: {colors}")
print(f"First color: {colors[0]}")
print(f"Last color: {colors[-1]}")

# Accessing nested tuples
print(f"Nested tuple: {nested_tuple}")
print(f"Nested item 'b': {nested_tuple[2][1]}")

# Tuple length
print(f"Number of colors: {len(colors)}")

# Important: Creating a single-item tuple requires a comma
print(f"Type of (42,): {type((42,))}")
print(f"Type of (42): {type((42))}")  # This is an integer, not a tuple
'''

    st.code(code1, language="python")

    if st.button("Run Tuples Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Tuple Operations")
    code2 = '''# Tuple operations
colors = ("red", "green", "blue", "green", "yellow")

# Counting occurrences
print(f"Count of 'green': {colors.count('green')}")

# Finding index
print(f"Index of 'blue': {colors.index('blue')}")

# Concatenation
more_colors = ("purple", "orange")
all_colors = colors + more_colors
print(f"Combined tuple: {all_colors}")

# Slicing
print(f"First three colors: {colors[0:3]}")
print(f"Every second color: {colors[::2]}")

# Unpacking
a, b, c, d, e = colors
print(f"Unpacked: a={a}, b={b}, c={c}, d={d}, e={e}")

# Partial unpacking
first, *middle, last = colors
print(f"Partial unpacking: first={first}, middle={middle}, last={last}")
'''

    st.code(code2, language="python")

    if st.button("Run Tuples Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Tuple Immutability and Errors")
    code3 = '''# Demonstrating tuple immutability
coordinates = (10, 20, 30)
print(f"Original tuple: {coordinates}")

# Trying to modify a tuple (will cause an error)
try:
    coordinates[0] = 100
    print(coordinates)
except TypeError as e:
    print(f"Error: {e}")

# Converting between tuples and lists
coordinates_list = list(coordinates)  # Convert tuple to list
coordinates_list[0] = 100  # Modify the list
new_coordinates = tuple(coordinates_list)  # Convert back to tuple
print(f"Modified using list conversion: {new_coordinates}")

# Error when unpacking wrong number of values
try:
    a, b = coordinates  # Too few variables
    print(a, b)
except ValueError as e:
    print(f"Error: {e}")
'''

    st.code(code3, language="python")

    if st.button("Run Tuples Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Dictionaries
elif section == "Dictionaries":
    st.header("Python Dictionaries")
    st.markdown("""
    Dictionaries are collections of key-value pairs. They are unordered, changeable, and indexed by keys.

    **Key features:**
    - Created with curly braces {}
    - Consists of key:value pairs
    - Keys must be unique and immutable (strings, numbers, tuples)
    - Values can be of any data type and can be duplicated
    - Dictionaries are mutable (can be changed after creation)
    """)

    st.subheader("Creating and Accessing Dictionaries")
    code1 = '''# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

empty_dict = {}
using_dict_function = dict(name="Alice", age=25)

# Accessing values
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Alternative access with get() method (safer)
print(f"City using get(): {person.get('city')}")
print(f"Country using get(): {person.get('country')}")  # Returns None
print(f"Country with default: {person.get('country', 'Unknown')}")  # Returns default value

# Dictionary keys, values, and items
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")
'''

    st.code(code1, language="python")

    if st.button("Run Dictionaries Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Modifying Dictionaries")
    code2 = '''# Modifying dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Original dictionary: {person}")

# Adding new key-value pairs
person["email"] = "john@example.com"
print(f"After adding email: {person}")

# Modifying values
person["age"] = 31
print(f"After changing age: {person}")

# Removing items
removed_value = person.pop("city")
print(f"Removed value: {removed_value}")
print(f"After pop: {person}")

# Adding multiple items
person.update({"city": "Boston", "country": "USA", "age": 32})
print(f"After update: {person}")

# Removing last inserted item
last_item = person.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem: {person}")

# Clearing the dictionary
person.clear()
print(f"After clear: {person}")
'''

    st.code(code2, language="python")

    if st.button("Run Dictionaries Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Nested Dictionaries and Common Errors")
    code3 = '''# Nested dictionaries
student = {
    "name": "Alice",
    "grades": {
        "math": 90,
        "science": 85,
        "history": 95
    },
    "activities": ["chess", "swimming"]
}

print(f"Student: {student}")
print(f"Math grade: {student['grades']['math']}")
print(f"First activity: {student['activities'][0]}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares}")

# Common error - accessing non-existent key
try:
    value = student["address"]  # This will cause an error
    print(value)
except KeyError as e:
    print(f"Error: {e}")
    print("Correct way to access a key that might not exist is with .get():")
    print(f"Address: {student.get('address', 'Not provided')}")

# Key restrictions
valid_dict = {1: "integer key", "2": "string key", (3, 4): "tuple key"}
print(f"Valid keys example: {valid_dict}")

try:
    invalid_dict = {[1, 2]: "list key"}  # Lists can't be keys
    print(invalid_dict)
except TypeError as e:
    print(f"Error: {e}")
'''

    st.code(code3, language="python")

    if st.button("Run Dictionaries Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Sets
elif section == "Sets":
    st.header("Python Sets")
    st.markdown("""
    Sets are unordered collections of unique items.

    **Key features:**
    - Created with curly braces {} or the set() function
    - Items are unordered (no indexing)
    - Sets contain only unique items (no duplicates)
    - Sets are mutable, but items must be immutable (strings, numbers, tuples)
    - Great for membership testing and removing duplicates
    """)

    st.subheader("Creating and Using Sets")
    code1 = '''# Creating sets
fruits = {"apple", "banana", "cherry"}
duplicates_demo = {"apple", "banana", "cherry", "apple", "cherry"}  # Duplicates will be removed
empty_set = set()  # Note: {} creates an empty dictionary, not a set
number_set = set([1, 2, 3, 2, 1])  # Convert list to set

print(f"Fruits set: {fruits}")
print(f"Set with duplicates: {duplicates_demo}")  # Duplicates are automatically removed
print(f"Empty set: {empty_set}")
print(f"Number set: {number_set}")

# Set length
print(f"Number of unique fruits: {len(fruits)}")

# Check if item exists
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'orange' in fruits? {'orange' in fruits}")
'''

    st.code(code1, language="python")

    if st.button("Run Sets Example 1"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Modifying Sets")
    code2 = '''# Modifying sets
fruits = {"apple", "banana", "cherry"}
print(f"Original set: {fruits}")

# Adding items
fruits.add("orange")
print(f"After add: {fruits}")

# Adding multiple items
fruits.update(["mango", "grapes"])
print(f"After update: {fruits}")

# Removing items
fruits.remove("banana")  # Raises an error if item doesn't exist
print(f"After remove: {fruits}")

try:
    fruits.remove("pear")  # Will raise an error
except KeyError as e:
    print(f"Error: {e}")

# Alternative removal with discard() (no error if item doesn't exist)
fruits.discard("mango")
print(f"After discard mango: {fruits}")
fruits.discard("pear")  # No error
print(f"After discard pear: {fruits}")

# Pop an item (random since sets are unordered)
popped = fruits.pop()
print(f"Popped item: {popped}")
print(f"After pop: {fruits}")

# Clearing the set
fruits.clear()
print(f"After clear: {fruits}")
'''

    st.code(code2, language="python")

    if st.button("Run Sets Example 2"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Set Operations")
    code3 = '''# Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Set A: {A}")
print(f"Set B: {B}")

# Union (all elements from both sets)
print(f"Union (A | B): {A | B}")
print(f"Union using method: {A.union(B)}")

# Intersection (elements common to both sets)
print(f"Intersection (A & B): {A & B}")
print(f"Intersection using method: {A.intersection(B)}")

# Difference (elements in A but not in B)
print(f"Difference (A - B): {A - B}")
print(f"Difference using method: {A.difference(B)}")

# Symmetric difference (elements in either A or B but not both)
print(f"Symmetric difference (A ^ B): {A ^ B}")
print(f"Symmetric difference using method: {A.symmetric_difference(B)}")

# Subset and superset
C = {1, 2}
print(f"Set C: {C}")
print(f"Is C subset of A? {C.issubset(A)}")
print(f"Is A superset of C? {A.issuperset(C)}")

# Common error - unhashable types
try:
    invalid_set = {[1, 2], "string"}  # Lists can't be in sets
    print(invalid_set)
except TypeError as e:
    print(f"Error: {e}")
'''

    st.code(code3, language="python")

    if st.button("Run Sets Example 3"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Operators
elif section == "Operators":
    st.header("Python Operators")
    st.markdown("""
    Python has several types of operators:

    1. **Arithmetic Operators**: perform mathematical operations
    2. **Assignment Operators**: assign values to variables
    3. **Comparison Operators**: compare values
    4. **Logical Operators**: combine conditional statements
    5. **Identity Operators**: compare object identities
    6. **Membership Operators**: test if a sequence contains an item
    7. **Bitwise Operators**: operate on bits
    """)

    st.subheader("Arithmetic Operators")
    code1 = '''# Arithmetic Operators
a, b = 10, 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# Special cases
print(f"Division by zero (try): ", end="")
try:
    result = a / 0
    print(result)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# String repetition with *
print(f"'Hi' * 3: {'Hi' * 3}")

# String concatenation with +
print(f"'Hello' + ' ' + 'World': {'Hello' + ' ' + 'World'}")
'''

    st.code(code1, language="python")

    if st.button("Run Arithmetic Operators"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Assignment Operators")
    code2 = '''# Assignment Operators
x = 10
print(f"Initial x: {x}")

# Simple assignment
x = 5
print(f"After x = 5: {x}")

# Add and assign
x += 3  # Same as x = x + 3
print(f"After x += 3: {x}")

# Subtract and assign
x -= 2  # Same as x = x - 2
print(f"After x -= 2: {x}")

# Multiply and assign
x *= 4  # Same as x = x * 4
print(f"After x *= 4: {x}")

# Divide and assign
x /= 2  # Same as x = x / 2
print(f"After x /= 2: {x}")

# Floor divide and assign
x //= 2  # Same as x = x // 2
print(f"After x //= 2: {x}")

# Modulus and assign
x %= 3  # Same as x = x % 3
print(f"After x %= 3: {x}")

# Exponentiate and assign
x **= 2  # Same as x = x ** 2
print(f"After x **= 2: {x}")

# Multiple assignment
a, b, c = 5, 10, 15
print(f"Multiple assignment: a = {a}, b = {b}, c = {c}")
'''

    st.code(code2, language="python")

    if st.button("Run Assignment Operators"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Comparison and Logical Operators")
    code3 = '''# Comparison Operators
a, b = 10, 5
print(f"a = {a}, b = {b}")

print(f"Equal (a == b): {a == b}")
print(f"Not Equal (a != b): {a != b}")
print(f"Greater Than (a > b): {a > b}")
print(f"Less Than (a < b): {a < b}")
print(f"Greater Than or Equal (a >= b): {a >= b}")
print(f"Less Than or Equal (a <= b): {a <= b}")

# Logical Operators
x = True
y = False
print(f"x = {x}, y = {y}")

print(f"AND (x and y): {x and y}")
print(f"OR (x or y): {x or y}")
print(f"NOT (not x): {not x}")
print(f"NOT (not y): {not y}")

# Complex conditions
a, b, c = 5, 10, 15
result = (a < b) and (b < c)
print(f"(a < b) and (b < c): {result}")

# Short-circuit evaluation
print(f"False and (1/0): ", end="")
try:
    result = False and (1/0)  # Second part not evaluated due to short-circuit
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError occurred")

print(f"True or (1/0): {True or (1/0)}")  # Second part not evaluated due to short-circuit
'''

    st.code(code3, language="python")

    if st.button("Run Comparison and Logical Operators"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Identity and Membership Operators")
    code4 = '''# Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")

print(f"a is b: {a is b}")  # False, different objects with same content
print(f"a is c: {a is c}")  # True, same object
print(f"a == b: {a == b}")  # True, same content

# None comparison
x = None
print(f"x is None: {x is None}")

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print(f"fruits = {fruits}")

print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")

# String membership
text = "Hello, World!"
print(f"text = '{text}'")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'Python' in text: {'Python' in text}")

# Dictionary membership (checks keys)
person = {"name": "John", "age": 30}
print(f"person = {person}")
print(f"'name' in person: {'name' in person}")
print(f"'John' in person: {'John' in person}")  # Checks keys, not values
print(f"'John' in person.values(): {'John' in person.values()}")
'''

    st.code(code4, language="python")

    if st.button("Run Identity and Membership Operators"):
        output, error = run_code(code4)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

# Conditional Statements
elif section == "Conditional Statements":
    st.header("Python Conditional Statements")
    st.markdown("""
    Conditional statements allow you to execute certain code blocks based on whether a condition is true or false.

    Python has the following conditional statements:

    1. **if statement**: executes a block of code if a specified condition is true
    2. **if-else statement**: executes one block if condition is true, another if false
    3. **if-elif-else statement**: tests multiple conditions sequentially
    4. **Nested if statements**: conditional statements inside other conditional statements
    """)

    st.subheader("Basic if Statement")
    code1 = '''# Basic if statement
x = 10

if x > 5:
    print("x is greater than 5")

# if with multiple conditions
if x > 5 and x < 15:
    print("x is between 5 and 15")

# Using bool values
is_active = True
if is_active:
    print("User is active")

# Note: Indentation is crucial in Python
if x > 0:
    print("x is positive")
    print("This line is also inside the if block")
print("This line is outside the if block")
'''

    st.code(code1, language="python")

    if st.button("Run Basic if Statement"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("if-else Statement")
    code2 = '''# if-else statement
age = 17

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# One-line if-else (ternary operator)
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# if-else with complex conditions
number = -5

if number > 0 and number % 2 == 0:
    print("Positive even number")
else:
    print("Either negative or odd number")

# Checking empty collections
my_list = []
if my_list:
    print("List has items")
else:
    print("List is empty")
'''

    st.code(code2, language="python")

    if st.button("Run if-else Statement"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("if-elif-else Statement")
    code3 = '''# if-elif-else statement
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Time of day example
import datetime
current_hour = datetime.datetime.now().hour
print(f"Current hour: {current_hour}")

if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(greeting)

# Multiple conditions in elif
x = 10

if x < 0:
    print("Negative number")
elif x == 0:
    print("Zero")
elif x < 5:
    print("Small positive number")
elif x < 10:
    print("Medium positive number")
else:
    print("Large positive number")
'''

    st.code(code3, language="python")

    if st.button("Run if-elif-else Statement"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Nested Conditional Statements")
    code4 = '''# Nested if statements
age = 25
income = 50000

if age >= 18:
    print("Adult")

    if income < 30000:
        print("Low income")
    elif income < 60000:
        print("Middle income")
    else:
        print("High income")
else:
    print("Minor")

    if age < 13:
        print("Child")
    else:
        print("Teenager")

# Checking multiple conditions with nesting
num = 15

if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number")
    else:
        print(f"{num} is a positive odd number")
elif num < 0:
    if num % 2 == 0:
        print(f"{num} is a negative even number")
    else:
        print(f"{num} is a negative odd number")
else:
    print("The number is zero")

# Common errors in conditional statements
x = 5
# Indentation error (uncomment to see the error)
# if x > 0:
# print("x is positive")

# Condition always evaluates to True (assignment instead of comparison)
if x = 10:  # This will cause a syntax error
    print("x is 10")
'''

    st.code(code4, language="python")

    if st.button("Run Nested Conditional Statements"):
        output, error = run_code(code4)
        if error:
            st.error(f"Error: {error}")
            st.info(
                "The code contains a deliberate syntax error: using '=' (assignment) instead of '==' (comparison) in the if condition. The correct syntax would be 'if x == 10:'")
        else:
            st.success(f"Output: {output}")

# Common Errors
elif section == "Common Errors":
    st.header("Common Python Errors for Beginners")
    st.markdown("""
    Understanding common errors helps beginners debug their code. Here are the most common types of errors you might encounter:

    1. **SyntaxError**: Incorrect syntax
    2. **IndentationError**: Improper indentation
    3. **NameError**: Using a variable that doesn't exist
    4. **TypeError**: Operations on incompatible types
    5. **IndexError**: Accessing an index out of range
    6. **KeyError**: Accessing a nonexistent key in a dictionary
    7. **ValueError**: Correct type but inappropriate value
    8. **ZeroDivisionError**: Division by zero
    9. **AttributeError**: Accessing nonexistent attribute
    10. **ImportError/ModuleNotFoundError**: Problems importing modules
    """)

    st.subheader("Syntax and Indentation Errors")
    code1 = '''# SyntaxError examples
# Uncomment to see errors:

# Missing closing parenthesis
# print("Hello, World!"

# Invalid syntax in if statement
# if x = 5:
#     print(x)

# IndentationError examples
# Inconsistent indentation
if True:
    print("First line")
  # print("Second line - incorrect indentation")

# Common beginner indentation errors
def my_function():
    print("Inside function")
# print("This line should be indented")  # Uncomment to see the error
'''

    st.code(code1, language="python")

    if st.button("Run Syntax Error Examples"):
        output, error = run_code(code1)
        if error:
            st.error(f"Error: {error}")
            st.info(
                "This example demonstrates syntax and indentation errors. Most lines are commented out because they would cause the code to fail. Uncomment them individually to see the specific errors.")
        else:
            st.success(f"Output: {output}")

    st.subheader("Name and Type Errors")
    code2 = '''# NameError examples
try:
    print(undefined_variable)  # Variable doesn't exist
except NameError as e:
    print(f"NameError: {e}")

# Corrected version
defined_variable = "I exist"
print(f"Corrected: {defined_variable}")

# TypeError examples
try:
    result = "5" + 5  # Can't add string and integer
    print(result)
except TypeError as e:
    print(f"TypeError: {e}")

# Corrected version
result = "5" + str(5)  # Convert int to string
print(f"Corrected: {result}")

# Alternative correction
result = int("5") + 5  # Convert string to int
print(f"Alternative correction: {result}")
'''

    st.code(code2, language="python")

    if st.button("Run Name and Type Error Examples"):
        output, error = run_code(code2)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Index and Key Errors")
    code3 = '''# IndexError examples
my_list = [1, 2, 3]

try:
    print(my_list[5])  # Index out of range
except IndexError as e:
    print(f"IndexError: {e}")

# Corrected version - check before accessing
index = 5
if index < len(my_list):
    print(f"Element at index {index}: {my_list[index]}")
else:
    print(f"Index {index} out of range. List has {len(my_list)} elements.")

# KeyError examples
my_dict = {"name": "John", "age": 30}

try:
    print(my_dict["address"])  # Key doesn't exist
except KeyError as e:
    print(f"KeyError: {e}")

# Corrected version - using get() method
address = my_dict.get("address", "N/A")
print(f"Address: {address}")

# Corrected version - check before accessing
key = "address"
if key in my_dict:
    print(f"{key}: {my_dict[key]}")
else:
    print(f"Key '{key}' not found in dictionary")
'''

    st.code(code3, language="python")

    if st.button("Run Index and Key Error Examples"):
        output, error = run_code(code3)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Value and Zero Division Errors")
    code4 = '''# ValueError examples
try:
    number = int("hello")  # Can't convert non-numeric string to int
    print(number)
except ValueError as e:
    print(f"ValueError: {e}")

# Corrected version - check if string is numeric
user_input = "hello"
if user_input.isdigit():
    number = int(user_input)
    print(f"Number: {number}")
else:
    print(f"'{user_input}' is not a valid number")

# ZeroDivisionError examples
try:
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# Corrected version - check denominator
denominator = 0
if denominator != 0:
    result = 10 / denominator
    print(f"Result: {result}")
else:
    print("Cannot divide by zero")
'''

    st.code(code4, language="python")

    if st.button("Run Value and Zero Division Error Examples"):
        output, error = run_code(code4)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

    st.subheader("Attribute and Import Errors")
    code5 = '''# AttributeError examples
text = "Hello"

try:
    result = text.append("World")  # String has no append method
    print(result)
except AttributeError as e:
    print(f"AttributeError: {e}")

# Corrected version - use string concatenation
result = text + " World"
print(f"Corrected: {result}")

# ImportError/ModuleNotFoundError examples
try:
    import non_existent_module
except ImportError as e:
    print(f"ImportError: {e}")

# Safe import technique
try:
    import math  # This one should work
    print(f"Pi is approximately {math.pi}")
except ImportError as e:
    print(f"Failed to import math: {e}")
'''

    st.code(code5, language="python")

    if st.button("Run Attribute and Import Error Examples"):
        output, error = run_code(code5)
        if error:
            st.error(f"Error: {error}")
        else:
            st.success(f"Output: {output}")

st.markdown("---")
st.markdown("""
### About This App

This interactive application was designed to help beginners learn Python's fundamentals. Feel free to:

1. Select different topics from the sidebar
2. Read the explanations
3. Run the example code to see results
4. Experiment by modifying the code

Understanding these basics will provide a solid foundation for your Python programming journey!
""")