## What is Pandas?

**Pandas** is an open-source Python library used for **data manipulation, analysis, and cleaning**. It provides powerful and easy-to-use data structures that allow you to work with structured data such as tables, spreadsheets, CSV files, and databases.

The two main data structures in Pandas are:

- **Series**: A one-dimensional labeled array.
- **DataFrame**: A two-dimensional table with rows and columns.

---

## Why Use Pandas?

Pandas is widely used because it simplifies working with data.

### Benefits of Pandas

- Easy to read and write data from different file formats (CSV, Excel, JSON, SQL, etc.).
- Fast and efficient data processing.
- Handles missing data easily.
- Supports filtering, sorting, grouping, and merging datasets.
- Provides built-in statistical functions.
- Integrates well with NumPy, Matplotlib, and Scikit-learn.
- Saves time by reducing the amount of code needed for data analysis.

---

## Where is Pandas Used?

Pandas is used in many fields where data needs to be processed or analyzed.

### Common Applications

- Data Analysis
- Data Cleaning and Preprocessing
- Machine Learning
- Data Science
- Financial Analysis
- Business Intelligence
- Scientific Research
- Web Scraping Data Processing


---

## Example Use Cases

| Field | How Pandas is Used |
|--------|--------------------|
| Data Science | Analyze and prepare datasets for machine learning |
| Finance | Analyze stock prices and financial reports |
| Healthcare | Process patient records and medical datasets |
| Business | Generate sales reports and customer insights |
| Education | Analyze student performance data |
| Research | Clean and analyze experimental data |
| Marketing | Study customer behavior and campaign performance |

---

# Pandas Basics - Important Functions

Note: A Series in Pandas is a one-dimensional labeled array. Think of it as a single column of data where each value has an associated index (label).

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **Series** | `pd.Series(data)` | Create a Series | `s = pd.Series([10,20,30])` |
| | `series.head()` | Show first 5 values | `s.head()` |
| | `series.tail()` | Show last 5 values | `s.tail()` |
| | `series.shape` | Number of elements | `s.shape` |
| | `series.dtype` | Data type | `s.dtype` |
| | `series.describe()` | Statistical summary | `s.describe()` |
| | `series.max()` | Maximum value | `s.max()` |
| | `series.min()` | Minimum value | `s.min()` |
| | `series.mean()` | Average value | `s.mean()` |
| | `series.sum()` | Sum of values | `s.sum()` |
| | `series.value_counts()` | Count unique values | `s.value_counts()` |

---

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **DataFrame** | `pd.DataFrame(data)` | Create a DataFrame | `df = pd.DataFrame(data)` |
| | `df.head()` | Show first 5 rows | `df.head()` |
| | `df.tail()` | Show last 5 rows | `df.tail()` |
| | `df.shape` | Number of rows and columns | `df.shape` |
| | `df.columns` | Show column names | `df.columns` |
| | `df.index` | Show row labels | `df.index` |
| | `df.dtypes` | Show data types | `df.dtypes` |
| | `df.describe()` | Statistical summary | `df.describe()` |
| | `df.info()` | Dataset information | `df.info()` |

---

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **Reading CSV Files** | `pd.read_csv()` | Read a CSV file | `df = pd.read_csv("students.csv")` |
| | `pd.read_csv(..., index_col=0)` | Set first column as index | `pd.read_csv("students.csv", index_col=0)` |
| | `pd.read_csv(..., usecols=[])` | Read selected columns | `pd.read_csv("students.csv", usecols=["Name","Marks"])` |
| | `pd.read_csv(..., nrows=5)` | Read first *n* rows | `pd.read_csv("students.csv", nrows=5)` |

---

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **Exploring Datasets** | `df.head()` | First 5 rows | `df.head()` |
| | `df.tail()` | Last 5 rows | `df.tail()` |
| | `df.shape` | Number of rows and columns | `df.shape` |
| | `df.columns` | Column names | `df.columns` |
| | `df.index` | Row labels | `df.index` |
| | `df.info()` | Dataset summary | `df.info()` |
| | `df.describe()` | Statistical summary | `df.describe()` |
| | `df.dtypes` | Data types | `df.dtypes` |
| | `df.sample(5)` | Random 5 rows | `df.sample(5)` |

---

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **Selecting Rows and Columns** | `df["Name"]` | Select one column | `df["Name"]` |
| | `df[["Name","Age"]]` | Select multiple columns | `df[["Name","Age"]]` |
| | `df.loc[row, column]` | Select by label | `df.loc[0, "Name"]` |
| | `df.iloc[row, column]` | Select by position | `df.iloc[0, 1]` |
| | `df.loc[0:3]` | Select rows by label | `df.loc[0:3]` |     .... search later
| | `df.iloc[0:3]` | Select rows by position | `df.iloc[0:3]` | ... search later

---

| Topic | Function | Purpose | Example |
|-------|----------|---------|---------|
| **Filtering Data** | `df[df["Age"] > 20]` | Filter rows by condition | `df[df["Age"] > 20]` |
| | `df[df["Marks"] >= 80]` | Filter by marks | `df[df["Marks"] >= 80]` |
| | `df[(df["Age"] > 20) & (df["Marks"] > 80)]` | Multiple conditions (AND) | `df[(df["Age"] > 20) & (df["Marks"] > 80)]` |
| | `df[(df["Age"] > 20) \| (df["Marks"] > 80)]` | Multiple conditions (OR) | `df[(df["Age"] > 20) \| (df["Marks"] > 80)]` |
| | `df.query("Age > 20")` | Filter using query | `df.query("Age > 20")` |

---

