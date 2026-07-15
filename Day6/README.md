# Student Performance Prediction using Linear Regression

## Project Overview

This project uses **Linear Regression** to predict the **Average Score** of students based on their academic performance and other related features. The project includes data preprocessing, feature engineering, model training, evaluation, and visualization of prediction results.

---

# What I Learned About Data Preprocessing

Data preprocessing is one of the most important steps in the machine learning pipeline because the quality of the input data directly affects the model's performance. During this project, I learned several preprocessing techniques.

## 1. Handling Missing Values

Before training a model, it is important to check for missing (null) values using functions such as `isnull()`. Missing values can either be removed or replaced using suitable techniques such as mean, median, or mode imputation.

---

## 2. Encoding Categorical Data

Machine learning algorithms cannot process text directly. Therefore, categorical features such as **Program** were converted into numerical values using encoding techniques like:

- Label Encoding
- One-Hot Encoding

---

## 3. Feature Engineering

Feature engineering involves creating new meaningful features from existing data.

In this project, a new column named **Average_Score** was created using the marks obtained in all subjects.

This feature was later used as the target variable for prediction.

---

## 4. Feature Selection

Not every column contributes to prediction.

Columns such as:

- Student_ID
- Name

were removed because they are identifiers and do not help predict student performance.

---

## 5. Feature Scaling

Numerical features were standardized using **StandardScaler** so that all features have a similar scale.

Feature scaling helps improve the stability and efficiency of many machine learning algorithms.

---

## 6. Outlier Detection

Outliers are unusually high or low values that may negatively affect machine learning models, especially Linear Regression.

I learned that outliers can be identified using:

- Box Plots
- IQR Method
- Z-Score

Removing or treating outliers can improve model performance.

---

## 7. Text Data Preprocessing

Although this project mainly contains numerical data, I also learned that datasets containing textual information require additional preprocessing before they can be used in machine learning.

Common text preprocessing techniques include:

- Convert text to lowercase
- Remove URLs
- Remove punctuation
- Remove numbers
- Tokenization
- Stopword removal
- Stemming
- Lemmatization
- Feature Extraction (Bag of Words, TF-IDF, Word Embeddings)

These techniques clean and transform raw text into numerical features that machine learning models can understand.

---

# Why Train-Test Splitting is Important

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

The training dataset is used to train the model, while the testing dataset evaluates how well the model performs on unseen data.

Train-test splitting helps:

- Prevent overfitting.
- Measure the model's generalization ability.
- Provide an unbiased estimate of model performance.

---

# Evaluation Metrics Used

The following regression evaluation metrics were used to assess the model:

- **Mean Absolute Error (MAE)** – Measures the average absolute prediction error.
- **Mean Squared Error (MSE)** – Measures the average squared prediction error.
- **Root Mean Squared Error (RMSE)** – Square root of MSE, expressed in the same units as the target variable.
- **R² Score (Coefficient of Determination)** – Measures how well the model explains the variance in the target variable.

## Model Evaluation Results

| Metric | Value |
|---------|------:|
| Mean Absolute Error (MAE) | **0.00** |
| Mean Squared Error (MSE) | **0.00** |
| Root Mean Squared Error (RMSE) | **0.00** |
| R² Score | **1.0000** |

---

# Model Performance

## Actual vs Predicted Scores

| Actual Score | Predicted Score | Difference |
|--------------|----------------:|-----------:|
| 85.75 | 85.75 | 0.00 |
| 97.25 | 97.25 | 0.00 |
| 89.50 | 89.50 | 0.00 |
| 74.25 | 74.25 | 0.00 |

The prediction results show that the predicted values exactly match the actual values for the test samples.

---

# Prediction Visualization

The **Actual vs Predicted Scatter Plot** shows that every prediction lies directly on the diagonal (ideal prediction) line.

This indicates that:

- Predicted values are identical to the actual values.
- Prediction error is zero.
- The model achieved perfect prediction on the test dataset.

---

# Observations

- The Linear Regression model achieved **perfect prediction accuracy** on the test dataset.
- All evaluation metrics (MAE, MSE, RMSE) are **0**, indicating no prediction error.
- The **R² Score of 1.0000** means the model explains **100% of the variance** in the target variable.
- The scatter plot confirms that all predicted values overlap with the actual values.

### Important Observation

Although these results appear excellent, they are **not typical of real-world machine learning problems**.

The target variable (**Average_Score**) was calculated directly from the subject scores (**Python, Mathematics, Statistics, and Machine_Learning**), and these same subject scores were also used as input features.

This causes **target leakage**, meaning the model is learning a direct mathematical relationship instead of discovering hidden patterns in the data.

In real-world applications, the target variable should not be derived directly from the input features. Instead, independent variables such as:

- Age
- Program
- Attendance
- Study Hours
- Previous Semester GPA
- Assignments
- Quiz Scores

should be used to predict student performance.

---

# Conclusion

This project provided practical experience in the complete machine learning workflow, including:

- Data exploration
- Data preprocessing
- Feature engineering
- Feature scaling
- Train-test splitting
- Building a Linear Regression model
- Model evaluation using regression metrics
- Visualizing prediction results
- Understanding target leakage and its impact on model performance

It also reinforced the importance of selecting appropriate features and applying preprocessing techniques to build reliable machine learning models.