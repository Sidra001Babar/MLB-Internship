# Multivariate Imputation

## Definition

Multivariate Imputation is a missing value handling technique that uses **other features (columns)** in the dataset to estimate and fill missing values.

Unlike simple techniques (mean, median, or mode), it considers the relationship between multiple features before imputing the missing value.

---

# KNN Imputer

## Definition

KNN (K-Nearest Neighbors) Imputer replaces missing values using the values of the **nearest similar rows** in the dataset.

It assumes that **similar observations have similar values**.

---

## How KNN Imputer Works

1. Identify the row containing the missing value.
2. Calculate the distance between this row and every other row.
3. Find the **K nearest neighbors** (most similar rows).
4. Replace the missing value using the neighbors' values.
   - For numerical data, the average of the neighbors is used.
   - If `weights='distance'`, closer neighbors have a greater influence.

---

## Distance Used

KNN Imputer uses **Euclidean Distance** to measure similarity between rows.

The rows with the smallest distance are considered the nearest neighbors.

---

## Parameters

- **n_neighbors**
  - Number of nearest neighbors used for imputation.
  - Example:
    ```python
    n_neighbors=3
    ```
    Uses the 3 nearest rows.

- **weights**
  - `'uniform'` → All neighbors contribute equally.
  - `'distance'` → Closer neighbors have more influence.

---

## Advantages

- Uses information from multiple columns.
- Preserves relationships between features.
- Usually performs better than mean or median imputation.
- Suitable for both numerical and categorical data (after appropriate encoding).

---

## Disadvantages

- Computationally expensive for large datasets.
- Performance decreases with high-dimensional data.
- Sensitive to feature scaling.
- Choosing the correct value of **K** is important.

---

## When to Use

- When features are correlated.
- When missing values are not too many.
- When preserving relationships between variables is important.
# Code (Only for Imputing Missing Values)

```python
import pandas as pd
from sklearn.impute import KNNImputer

# Load dataset
df = pd.read_csv('train.csv')[['Age', 'Pclass', 'Fare']]

# Create KNN Imputer
knn = KNNImputer(
    n_neighbors=3,
    weights='distance'
)

# Impute missing values
df_imputed = knn.fit_transform(df)

# Convert back to DataFrame
df_imputed = pd.DataFrame(
    df_imputed,
    columns=df.columns
)

df_imputed.head()
```
# Using on Train and Test Data

```python
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer

X_train, X_test = train_test_split(df, test_size=0.2, random_state=2)

knn = KNNImputer(
    n_neighbors=3,
    weights='distance'
)

X_train = knn.fit_transform(X_train)
X_test = knn.transform(X_test)
```