# Breast Cancer Wisconsin Classification using Logistic Regression

## Overview

This project implements a **Breast Cancer Classification** model using the **Breast Cancer Dataset** available in Scikit-learn. The objective is to classify tumors as **Malignant (Cancerous)** or **Benign (Non-cancerous)** using the Logistic Regression algorithm. The project also demonstrates data preprocessing, feature scaling, model evaluation, and hyperparameter tuning using GridSearchCV.

---

# Dataset

The dataset is loaded from the Scikit-learn built-in datasets.

- **Dataset:** Breast Cancer Wisconsin Dataset
- **Total Samples:** 569
- **Features:** 30 numerical features
- **Target Classes:**
  - **0:** Malignant (Cancerous)
  - **1:** Benign (Non-cancerous)

---

# Project Workflow

1. Load the Breast Cancer Wisconsin Dataset.
2. Explore the dataset using:
   - `head()`
   - `info()`
   - `describe()`
3. Visualize the target class distribution.
4. Check for missing values and duplicate records.
5. Separate features and target variable.
6. Split the dataset into training and testing sets.
7. Apply feature scaling using `StandardScaler`.
8. Train a Logistic Regression model.
9. Evaluate the model using multiple evaluation metrics.
10. Perform Hyperparameter Tuning using `GridSearchCV`.
11. Compare model performance before and after tuning.
12. Display the Confusion Matrix.

---

# Data Preprocessing

The following preprocessing steps were performed:

- Checked for missing values.
- Checked for duplicate records.
- Separated features (`X`) and target (`y`).
- Split the dataset into training and testing sets.
- Applied feature scaling using `StandardScaler`.

---

# Machine Learning Algorithm

**Logistic Regression**

Logistic Regression is a supervised machine learning algorithm used for binary classification problems. It predicts the probability that an input belongs to one of two classes and assigns the class with the higher probability.

---

# Hyperparameter Tuning

Hyperparameter tuning was performed using **GridSearchCV**.

The following hyperparameters were explored:

- **C**
- **Penalty**
- **Solver**

GridSearchCV evaluated multiple combinations using **5-Fold Cross Validation** and selected the best-performing model based on accuracy.

---

# Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score

These metrics help assess the classification performance from different perspectives.

---

# Results

## Before Hyperparameter Tuning

| Metric | Score |
|---------|------:|
| Accuracy | 0.98 |
| Precision | 0.99 |
| Recall | 0.99 |
| F1-Score | 0.99 |

---

## After Hyperparameter Tuning

| Metric | Score |
|---------|------:|
| Accuracy | 0.9737 |
| Precision | 0.9726 |
| Recall | 0.9861 |
| F1-Score | 0.9793 |

---

# Observations
- Why after hyperparameter tunning accuracy,recall,precision,f1 score reduce: Hyperparameter tuning does not always increase performance; it may select a more generalized model that reduces slight test-set performance to avoid overfitting.
Feature scaling already improved the model significantly, and the tuned model results are still strong
- Logistic Regression achieved excellent performance on the Breast Cancer Wisconsin dataset.
- Feature scaling improved the training process by bringing all numerical features to a common scale.
- GridSearchCV selected the best hyperparameters using 5-Fold Cross Validation.
- Although the tuned model achieved a slightly lower test accuracy than the default model, this is normal because hyperparameter tuning optimizes performance on the cross-validation folds of the training data rather than the test data.
- The model demonstrated strong generalization with high Accuracy, Precision, Recall, and F1-Score.

---

# Libraries Used

- Pandas
- Matplotlib
- Scikit-learn

---

# Conclusion

This project demonstrates the complete machine learning workflow for a binary classification problem, including data exploration, preprocessing, feature scaling, model training, evaluation, and hyperparameter tuning. Logistic Regression proved to be an effective classifier for the Breast Cancer  dataset, achieving high predictive performance and reliable classification results.