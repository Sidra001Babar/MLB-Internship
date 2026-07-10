# Iris Clustering using K-Means

## Overview

This project demonstrates **unsupervised learning** using the **K-Means Clustering** algorithm on the **Iris dataset**. Since clustering works without labeled data, the target column was removed before training the model. The project includes data exploration, preprocessing, determining the optimal number of clusters using the Elbow Method, clustering with K-Means, dimensionality reduction using PCA, and visualization of the resulting clusters.

---

# Dataset

- **Dataset:** Iris Dataset (Scikit-learn)
- **Total Samples:** 150
- **Features:** 4 numerical features
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **Target Classes:** 3 (used only for reference and not for clustering)

---

# Project Workflow

1. Load the Iris dataset.
2. Convert the dataset into a Pandas DataFrame.
3. Explore the dataset using:
   - `head()`
   - `info()`
   - `describe()`
4. Visualize the dataset using different plots.
5. Check for missing values and duplicate records.
6. Separate features and target variable.
7. Remove the target column before clustering.
9. Apply K-Means clustering with **5 clusters**.
10. Use the **Elbow Method** to determine the optimal number of clusters.
11. Observe that the Elbow Method suggests **3 clusters**.
12. Apply K-Means again using **3 clusters**.
13. Apply **Principal Component Analysis (PCA)** to reduce the data to two dimensions.
14. Visualize the final clusters and cluster centroids using a scatter plot.

---

# What is Clustering?

Clustering is an **unsupervised machine learning** technique that groups similar data points together without using labeled data. The objective is to discover hidden patterns or natural groupings within a dataset. In this project, **K-Means Clustering** was used to partition the Iris dataset into groups based on the similarity of flower measurements.

---

# What is PCA?

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms high-dimensional data into a smaller number of features called **principal components** while preserving most of the important information. Since the Iris dataset has four features, PCA was used to reduce them to **two principal components**, making it easier to visualize the clusters on a 2D scatter plot.


# Results

- Successfully explored and preprocessed the Iris dataset.
- Removed the target column before clustering since K-Means is an unsupervised algorithm.
- Initially clustered the data into **5 clusters**.
- Used the **Elbow Method**, which suggested that **3 clusters** are optimal.
- Reapplied K-Means using **3 clusters**.
- Reduced the dataset to two dimensions using **PCA**.
- Successfully visualized the final clusters and their centroids.

---

# Observations

- K-Means creates exactly the number of clusters specified by the user.
- Increasing the number of clusters always reduces WCSS, but does not necessarily produce better clustering.
- The Elbow Method helped identify **3** as the optimal number of clusters for the Iris dataset.
- PCA simplified the four-dimensional dataset into two dimensions, making cluster visualization easier.
- The resulting clusters closely matched the natural grouping of the Iris dataset.

---

# Libraries Used

- Pandas
- Matplotlib
- Scikit-learn

---
