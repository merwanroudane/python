import streamlit as st
import pandas as pd
import numpy as np
import sys
import io
from contextlib import redirect_stdout
import traceback

st.set_page_config(
	page_title="Python Data Science Basics",
	page_icon="📊",
	layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
    }
    .section-header {
        font-size: 1.8rem;
        color: #0D47A1;
        padding-top: 1rem;
    }
    .subsection-header {
        font-size: 1.4rem;
        color: #1565C0;
        padding-top: 0.5rem;
    }
    .code-explanation {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #1E88E5;
    }
    .correct-output {
        background-color: #f1f8e9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #4CAF50;
    }
    .error-message {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #F44336;
    }
    .highlight {
        font-weight: bold;
        color: #D81B60;
    }
    .note {
        font-style: italic;
        color: #455A64;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: #616161;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


def execute_code(code_string):
	"""Execute the provided code and capture output and errors"""
	local_env = {}
	output_buffer = io.StringIO()
	error_message = None

	try:
		with redirect_stdout(output_buffer):
			exec(code_string, local_env)
		output = output_buffer.getvalue()
		success = True
	except Exception as e:
		error_message = f"{type(e).__name__}: {str(e)}\n\n{traceback.format_exc()}"
		output = ""
		success = False

	return success, output, error_message


# Header Section
st.markdown("<h1 class='main-header'>Python for Data Science: NumPy & Pandas Fundamentals</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Interactive guide by Dr. Merwan Roudane</p>", unsafe_allow_html=True)

# Introduction
st.markdown("<h2 class='section-header'>Introduction</h2>", unsafe_allow_html=True)
st.markdown("""
This interactive app will guide you through the basics of Python data analysis using NumPy and Pandas libraries.
Each section contains examples you can run directly in the app, along with explanations and common errors to avoid.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
	"Choose a section:",
	["NumPy Basics", "NumPy Operations", "Pandas Basics", "Pandas Operations", "Common Errors & Solutions"]
)

# NumPy Basics Section
if section == "NumPy Basics":
	st.markdown("<h2 class='section-header'>NumPy Basics</h2>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Creating NumPy Arrays</h3>", unsafe_allow_html=True)

	example1_code = """
import numpy as np

# Creating a simple array
simple_array = np.array([1, 2, 3, 4, 5])
print("Simple array:")
print(simple_array)
print("Type:", type(simple_array))
print("Shape:", simple_array.shape)

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\\n2D array (matrix):")
print(matrix)
print("Shape:", matrix.shape)

# Array of zeros
zeros = np.zeros((3, 4))
print("\\nArray of zeros:")
print(zeros)

# Array of ones
ones = np.ones((2, 3))
print("\\nArray of ones:")
print(ones)

# Array with a range of values
range_array = np.arange(0, 10, 2)  # start, stop, step
print("\\nRange array:")
print(range_array)

# Linspace - evenly spaced values within a specified interval
linspace = np.linspace(0, 1, 5)  # start, stop, num
print("\\nLinspace array:")
print(linspace)

# Random numbers
random_array = np.random.rand(3, 3)  # 3x3 array of random numbers between 0 and 1
print("\\nRandom array:")
print(random_array)
"""

	st.code(example1_code, language="python")

	if st.button("Run NumPy Array Creation Examples"):
		success, output, error = execute_code(example1_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Key NumPy Array Creation Functions:**

    * `np.array()`: Creates an array from a list or tuple
    * `np.zeros()`: Creates an array filled with zeros
    * `np.ones()`: Creates an array filled with ones
    * `np.arange()`: Creates an array with a range of values
    * `np.linspace()`: Creates an array with evenly spaced values
    * `np.random.rand()`: Creates an array with random values
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Array Attributes and Methods</h3>", unsafe_allow_html=True)

	example2_code = """
import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Original array:")
print(arr)

# Array attributes
print("\\nArray attributes:")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# Array methods
print("\\nArray methods:")
print("Sum of all elements:", arr.sum())
print("Sum along rows (axis=1):", arr.sum(axis=1))
print("Sum along columns (axis=0):", arr.sum(axis=0))
print("Minimum value:", arr.min())
print("Maximum value:", arr.max())
print("Mean value:", arr.mean())
print("Standard deviation:", arr.std())

# Reshape the array
reshaped = arr.reshape(4, 3)
print("\\nReshaped array (4x3):")
print(reshaped)

# Flatten the array
flattened = arr.flatten()
print("\\nFlattened array:")
print(flattened)

# Transpose the array
transposed = arr.T
print("\\nTransposed array:")
print(transposed)
"""

	st.code(example2_code, language="python")

	if st.button("Run NumPy Array Methods Examples"):
		success, output, error = execute_code(example2_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

# NumPy Operations Section
elif section == "NumPy Operations":
	st.markdown("<h2 class='section-header'>NumPy Operations</h2>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Array Indexing and Slicing</h3>", unsafe_allow_html=True)

	example3_code = """
import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Original array:")
print(arr)

# Indexing
print("\\nIndexing:")
print("Element at position [1, 2]:", arr[1, 2])  # row 1, column 2
print("First row:", arr[0])
print("Last row:", arr[-1])

# Slicing
print("\\nSlicing:")
print("First two rows:")
print(arr[0:2])
print("\\nLast two columns:")
print(arr[:, 2:4])
print("\\nSubmatrix (top-left 2x2):")
print(arr[0:2, 0:2])

# Boolean indexing
print("\\nBoolean indexing:")
bool_mask = arr > 6
print("Boolean mask (arr > 6):")
print(bool_mask)
print("\\nElements greater than 6:")
print(arr[bool_mask])

# Fancy indexing
print("\\nFancy indexing:")
row_indices = np.array([0, 2])
col_indices = np.array([1, 3])
print("Selected rows:", arr[row_indices])
print("Selected elements:", arr[row_indices[:, np.newaxis], col_indices])
"""

	st.code(example3_code, language="python")

	if st.button("Run NumPy Indexing Examples"):
		success, output, error = execute_code(example3_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<h3 class='subsection-header'>Array Operations</h3>", unsafe_allow_html=True)

	example4_code = """
import numpy as np

# Create sample arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print("Array a:", a)
print("Array b:", b)

# Element-wise operations
print("\\nElement-wise operations:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** 2 =", a ** 2)  # Square each element

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\\nMatrix A:")
print(A)
print("Matrix B:")
print(B)

print("\\nMatrix operations:")
print("A + B:")
print(A + B)
print("\\nMatrix multiplication (A @ B):")
print(A @ B)  # Matrix multiplication
print("\\nElement-wise multiplication (A * B):")
print(A * B)

# Dot product
print("\\nDot product of vectors a and b:", np.dot(a, b))

# Matrix-vector multiplication
v = np.array([1, 2])
print("\\nMatrix A:")
print(A)
print("Vector v:", v)
print("Matrix-vector multiplication (A @ v):")
print(A @ v)

# Universal functions (ufuncs)
print("\\nUniversal functions:")
print("sin(a):", np.sin(a))
print("exp(a):", np.exp(a))
print("sqrt(a):", np.sqrt(a))
print("log(a):", np.log(a))
"""

	st.code(example4_code, language="python")

	if st.button("Run NumPy Operations Examples"):
		success, output, error = execute_code(example4_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Key NumPy Operations:**

    * **Element-wise operations**: `+`, `-`, `*`, `/`, `**`
    * **Matrix multiplication**: `@` operator or `np.matmul()`
    * **Dot product**: `np.dot()`
    * **Universal functions (ufuncs)**: `np.sin()`, `np.exp()`, `np.sqrt()`, etc.

    NumPy operations are significantly faster than equivalent operations using Python lists, especially for large arrays.
    """)
	st.markdown("</div>", unsafe_allow_html=True)

# Pandas Basics Section
elif section == "Pandas Basics":
	st.markdown("<h2 class='section-header'>Pandas Basics</h2>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Creating DataFrames and Series</h3>", unsafe_allow_html=True)

	example5_code = """
import pandas as pd
import numpy as np

# Creating a Series
print("Creating a Series:")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame from a dictionary
print("\\nCreating a DataFrame from a dictionary:")
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 80000, 75000]
}
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a NumPy array
print("\\nCreating a DataFrame from a NumPy array:")
array_data = np.random.randn(5, 4)  # 5 rows, 4 columns
df_array = pd.DataFrame(
    array_data,
    index=pd.date_range('20230101', periods=5),
    columns=list('ABCD')
)
print(df_array)

# Creating a DataFrame from a CSV file (using a simple string as an example)
print("\\nCreating a DataFrame from CSV data:")
csv_data = '''
Name,Age,Gender,Occupation
Alice,24,F,Data Scientist
Bob,27,M,Engineer
Charlie,31,M,Designer
Diana,29,F,Doctor
'''
import io
df_csv = pd.read_csv(io.StringIO(csv_data))
print(df_csv)

# Series and DataFrame attributes
print("\\nSeries attributes:")
print("Shape:", s.shape)
print("Size:", s.size)
print("Data type:", s.dtype)

print("\\nDataFrame attributes:")
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print("Data types:")
print(df.dtypes)
"""

	st.code(example5_code, language="python")

	if st.button("Run Pandas Creation Examples"):
		success, output, error = execute_code(example5_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Key Pandas Data Structures:**

    * **Series**: 1D labeled array capable of holding any data type
    * **DataFrame**: 2D labeled data structure with columns of potentially different types

    **Common Ways to Create DataFrames:**

    * From dictionaries with `pd.DataFrame(dict)`
    * From NumPy arrays with `pd.DataFrame(array)`
    * From CSV files with `pd.read_csv()`
    * From Excel files with `pd.read_excel()`
    * From SQL queries with `pd.read_sql()`
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Viewing and Selecting Data</h3>", unsafe_allow_html=True)

	example6_code = """
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Max', 'Sofia'],
    'Age': [28, 24, 35, 32, 45, 37],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'Madrid'],
    'Department': ['Sales', 'Engineering', 'Marketing', 'HR', 'Sales', 'Engineering'],
    'Salary': [65000, 70000, 80000, 75000, 90000, 85000],
    'Experience': [3, 2, 7, 5, 10, 8]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Basic viewing methods
print("\\nFirst 3 rows (head):")
print(df.head(3))

print("\\nLast 2 rows (tail):")
print(df.tail(2))

print("\\nSummary statistics:")
print(df.describe())

print("\\nInformation about DataFrame:")
df_info_buffer = io.StringIO()
df.info(buf=df_info_buffer)
print(df_info_buffer.getvalue())

# Basic selection
print("\\nSelecting a single column (returns a Series):")
print(df['Name'])

print("\\nSelecting multiple columns:")
print(df[['Name', 'Salary']])

# Selection by label
print("\\nSelection by label (loc):")
print("Row at index 2:")
print(df.loc[2])

print("\\nRows 1-3, columns 'Name' and 'Salary':")
print(df.loc[1:3, ['Name', 'Salary']])

# Selection by position
print("\\nSelection by position (iloc):")
print("Row at position 0:")
print(df.iloc[0])

print("\\nRows 1-3, columns 0 and 4:")
print(df.iloc[1:4, [0, 4]])

# Boolean indexing
print("\\nBoolean indexing:")
print("People older than 30:")
print(df[df['Age'] > 30])

print("\\nEngineers with salary > 75000:")
print(df[(df['Department'] == 'Engineering') & (df['Salary'] > 75000)])

# Sorting
print("\\nSorting by Age (ascending):")
print(df.sort_values('Age'))

print("\\nSorting by Salary (descending) and Age (ascending):")
print(df.sort_values(['Salary', 'Age'], ascending=[False, True]))
"""

	st.code(example6_code, language="python")

	if st.button("Run Pandas Viewing and Selection Examples"):
		success, output, error = execute_code(example6_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

# Pandas Operations Section
elif section == "Pandas Operations":
	st.markdown("<h2 class='section-header'>Pandas Operations</h2>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>Data Cleaning and Preparation</h3>", unsafe_allow_html=True)

	example7_code = """
import pandas as pd
import numpy as np

# Create a DataFrame with some missing values
data = {
    'Name': ['John', 'Anna', 'Peter', None, 'Max', 'Sofia'],
    'Age': [28, None, 35, 32, 45, None],
    'City': ['New York', 'Paris', None, 'London', 'Tokyo', 'Madrid'],
    'Salary': [65000, 70000, np.nan, 75000, 90000, 85000]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values:")
print(df)

# Check for missing values
print("\\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values
print("\\nDropping rows with any missing values:")
print(df.dropna())

# Drop columns with missing values
print("\\nDropping columns with any missing values:")
print(df.dropna(axis=1))

# Fill missing values
print("\\nFilling missing values with a specific value:")
print(df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown', 'Salary': df['Salary'].median()}))

# Replace values
print("\\nReplacing 'New York' with 'NYC':")
print(df.replace('New York', 'NYC'))

# Remove duplicates
df_with_duplicates = pd.concat([df, df.iloc[0:2]])
print("\\nDataFrame with duplicates:")
print(df_with_duplicates)

print("\\nAfter removing duplicates:")
print(df_with_duplicates.drop_duplicates())

# Data type conversion
print("\\nCurrent data types:")
print(df.dtypes)

# Convert Salary to integer (after filling NaN values)
df_clean = df.copy()
df_clean['Salary'] = df_clean['Salary'].fillna(0).astype(int)
print("\\nAfter converting Salary to integer:")
print(df_clean)
print(df_clean.dtypes)

# String operations
print("\\nString operations (uppercase city names):")
print(df['City'].str.upper())

# Apply custom function to a column
def age_category(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 30:
        return "Young"
    elif age < 40:
        return "Mid"
    else:
        return "Senior"

print("\\nApplying custom function to categorize ages:")
print(df['Age'].apply(age_category))
"""

	st.code(example7_code, language="python")

	if st.button("Run Data Cleaning Examples"):
		success, output, error = execute_code(example7_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<h3 class='subsection-header'>Data Analysis and Grouping</h3>", unsafe_allow_html=True)

	# Corrected example8_code with numeric_only=True for groupby mean and explicit column selection
	example8_code = """
import pandas as pd
import numpy as np

# Create a sample DataFrame with numeric data for analysis
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Max', 'Sofia', 'Tom', 'Emma'],
    'Age': [28, 24, 35, 32, 45, 37, 28, 24],
    'Department': ['Sales', 'Engineering', 'Marketing', 'HR', 'Sales', 'Engineering', 'Marketing', 'HR'],
    'Salary': [65000, 70000, 80000, 75000, 90000, 85000, 67000, 72000],
    'Experience': [3, 2, 7, 5, 10, 8, 4, 3],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Grouping data with numeric_only to avoid string column errors
print("\\nGrouping by Department (mean of numeric columns only):")
print(df.groupby('Department').mean(numeric_only=True))

print("\\nGrouping by Department and Gender (mean of numeric columns only):")
print(df.groupby(['Department', 'Gender']).mean(numeric_only=True))

# Aggregation with explicit column selection
print("\\nMultiple aggregations on numeric columns:")
result = df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max'],
    'Age': ['mean', 'min', 'max'],
    'Experience': 'mean'
})
print(result)

# Transformation 
print("\\nCalculating salary deviation from department average:")
df['Salary_Deviation'] = df['Salary'] - df.groupby('Department')['Salary'].transform('mean')
print(df[['Name', 'Department', 'Salary', 'Salary_Deviation']])

# Pivot tables with numeric values only
print("\\nPivot table - Average salary by Department and Gender:")
pivot = pd.pivot_table(
    df, 
    values='Salary',  # Specify only numeric column
    index='Department', 
    columns='Gender', 
    aggfunc='mean'
)
print(pivot)

# Crosstab - count of employees by Department and Gender
print("\\nCrosstab - Count of employees by Department and Gender:")
crosstab = pd.crosstab(df['Department'], df['Gender'])
print(crosstab)

# Value counts
print("\\nCounts of each department:")
print(df['Department'].value_counts())

# Applying functions to groups
print("\\nApplying custom function to each department group:")
def top_earner(group):
    return group.loc[group['Salary'].idxmax()]

top_earners = df.groupby('Department').apply(top_earner)
print("Top earner in each department:")
print(top_earners[['Name', 'Department', 'Salary']])
"""

	st.code(example8_code, language="python")

	if st.button("Run Data Analysis Examples"):
		success, output, error = execute_code(example8_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Key Pandas Grouping Operations:**

    * **`groupby()`**: Group DataFrame by one or more columns
    * **Aggregation**: Compute summary statistics for groups (use `numeric_only=True` to avoid errors with string columns)
    * **Transformation**: Apply operations while preserving the original DataFrame structure
    * **Pivot tables**: Reshape and summarize data
    * **Crosstab**: Compute a cross-tabulation of two or more factors

    **Important Note**: When using `mean()`, `sum()`, and other statistical methods with mixed data types, 
    specify `numeric_only=True` to prevent errors from attempting calculations on non-numeric data.
    """)
	st.markdown("</div>", unsafe_allow_html=True)

# Common Errors & Solutions Section
elif section == "Common Errors & Solutions":
	st.markdown("<h2 class='section-header'>Common Errors & Solutions</h2>", unsafe_allow_html=True)

	st.markdown("<h3 class='subsection-header'>1. Syntax Errors in Python</h3>", unsafe_allow_html=True)

	# Example 1: Multiline string not closed
	error1_code = """
# Error: Unterminated string literal (missing closing quote)
message = "Hello, this is a multiline string
that is not properly closed.
print(message)
"""

	st.code(error1_code, language="python")

	if st.button("Run Error Example 1"):
		success, output, error = execute_code(error1_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Error**: SyntaxError: EOL while scanning string literal

    **Solution**: Ensure all string literals are properly closed with matching quotes. For multiline strings, use triple quotes:
    ```python
    message = '''Hello, this is a properly formatted
    multiline string.'''
    print(message)
    ```

    Or concatenate strings:
    ```python
    message = "Hello, this is a " + \\
              "properly concatenated multiline string."
    print(message)
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	# Example 2: Indentation error
	st.markdown("<h3 class='subsection-header'>2. Indentation Errors</h3>", unsafe_allow_html=True)

	error2_code = """
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
return total / count  # This line should be indented

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average is: {average}")
"""

	st.code(error2_code, language="python")

	if st.button("Run Error Example 2"):
		success, output, error = execute_code(error2_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Error**: IndentationError: expected an indented block

    **Solution**: Python uses indentation to define code blocks. Ensure consistent indentation (typically 4 spaces):
    ```python
    def calculate_average(numbers):
        total = sum(numbers)
        count = len(numbers)
        return total / count  # Properly indented
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	# Example 3: Missing parentheses in print
	st.markdown("<h3 class='subsection-header'>3. NumPy Shape Mismatch</h3>", unsafe_allow_html=True)

	error3_code = """
import numpy as np

# Create two arrays with incompatible shapes
array1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
array2 = np.array([[7, 8], [9, 10]])       # Shape: (2, 2)

# Attempt to add them together
result = array1 + array2
print(result)
"""

	st.code(error3_code, language="python")

	if st.button("Run Error Example 3"):
		success, output, error = execute_code(error3_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Error**: ValueError: operands could not be broadcast together with shapes (2,3) (2,2)

    **Solution**: NumPy operations require compatible shapes. Ensure arrays have compatible dimensions for broadcasting:
    ```python
    # Make arrays compatible
    array1 = np.array([[1, 2, 3], [4, 5, 6]])  # Shape: (2, 3)
    array2 = np.array([[7, 8, 9], [10, 11, 12]])  # Shape: (2, 3)

    # Now addition works
    result = array1 + array2
    ```

    Or reshape one of the arrays to make it compatible:
    ```python
    array2_reshaped = array2.reshape(2, 2, 1)  # For specific broadcasting scenarios
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	# Example 4: Pandas key error
	st.markdown("<h3 class='subsection-header'>4. Pandas Key Error</h3>", unsafe_allow_html=True)

	error4_code = """
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'City': ['New York', 'Paris', 'Berlin']}

df = pd.DataFrame(data)

# Try to access a column that doesn't exist
result = df['Salary']
print(result)
"""

	st.code(error4_code, language="python")

	if st.button("Run Error Example 4"):
		success, output, error = execute_code(error4_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Error**: KeyError: 'Salary'

    **Solution**: Check if a column exists before accessing it:
    ```python
    if 'Salary' in df.columns:
        result = df['Salary']
    else:
        print("Column 'Salary' does not exist")
        # Optionally, create the column
        df['Salary'] = [65000, 70000, 80000]
    ```

    Or use the `get` method from pandas:
    ```python
    result = df.get('Salary', 'Column not found')
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	# Example 5: Pandas Chained Assignment Warning
	st.markdown("<h3 class='subsection-header'>5. Pandas Chained Assignment Warning</h3>", unsafe_allow_html=True)

	error5_code = """
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Chained assignment that may not work as expected
df[df['Age'] > 30]['City'] = 'Changed'  # This is a chained assignment
print("\\nAfter attempted modification:")
print(df)
"""

	st.code(error5_code, language="python")

	if st.button("Run Error Example 5"):
		success, output, error = execute_code(error5_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Warning**: SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame

    **Problem**: The change doesn't actually apply to the original DataFrame.

    **Solution**: Use loc for assignments:
    ```python
    # Correct way to modify values based on a condition
    df.loc[df['Age'] > 30, 'City'] = 'Changed'
    ```

    Or create a copy explicitly if you want to work with a subset:
    ```python
    subset = df[df['Age'] > 30].copy()
    subset['City'] = 'Changed'
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

	# Example 6: Type Error in Pandas calculations with mixed types
	st.markdown("<h3 class='subsection-header'>6. TypeError in Pandas Calculations with Mixed Types</h3>",
				unsafe_allow_html=True)

	error6_code = """
import pandas as pd

# Create a DataFrame with mixed types
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 80000, 75000]
}
df = pd.DataFrame(data)

# Attempt to calculate mean of all columns including non-numeric ones
print(df.groupby('City').mean())  # This will cause an error
"""

	st.code(error6_code, language="python")

	if st.button("Run Error Example 6"):
		success, output, error = execute_code(error6_code)
		if success:
			st.markdown("<div class='correct-output'></div>", unsafe_allow_html=True)
			st.text(output)
		else:
			st.markdown("<div class='error-message'></div>", unsafe_allow_html=True)
			st.error(error)

	st.markdown("<div class='code-explanation'>", unsafe_allow_html=True)
	st.markdown("""
    **Error**: TypeError: agg function failed [how->mean,dtype->object]

    **Solution**: Specify numeric_only=True when using statistical methods with DataFrames containing mixed types:
    ```python
    # Correct way to calculate mean on mixed type DataFrames
    print(df.groupby('City').mean(numeric_only=True))
    ```

    Or select specific numeric columns manually:
    ```python
    print(df.groupby('City')[['Age', 'Salary']].mean())
    ```
    """)
	st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
	"<div class='footer'>Developed by Dr. Merwan Roudane - A comprehensive guide for Python Data Science Education</div>",
	unsafe_allow_html=True)