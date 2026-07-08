# Training vs Testing Performance

Machine Learning models are evaluated using two datasets:

- **Training Data:** Used to train (learn) the model.
- **Testing Data:** Used to evaluate the model on unseen data.

A good model should perform well on both datasets.

| Training Performance | Testing Performance | Interpretation |
|----------------------|--------------------|----------------|
| High | High | Good Model |
| High | Low | Overfitting |
| Low | Low | Underfitting |

**Example:**

- Training Accuracy = 95%
- Testing Accuracy = 93%

This indicates that the model generalizes well to new data.

# Difference Between Overfitting and Underfitting

| Feature | Overfitting | Underfitting |
|---------|-------------|--------------|
| **Definition** | Overfitting occurs when a model learns the training data too well, including noise and outliers, causing poor performance on new data. | Underfitting occurs when a model is too simple to capture the underlying patterns in the data, resulting in poor performance on both training and testing data. |
| **Training Accuracy** | Very High | Low |
| **Testing Accuracy** | Low | Low |
| **Model Complexity** | Too Complex | Too Simple |
| **Generalization** | Poor generalization to unseen data | Poor learning of both training and unseen data |
| **Bias** | Low Bias | High Bias |
| **Variance** | High Variance | Low Variance |
| **Learning Behavior** | Memorizes the training data instead of learning patterns | Fails to learn important relationships in the data |
| **Training Error** | Very Low | High |
| **Testing Error** | High | High |
| **Cause** | Excessive model complexity, too many features, or too much training | Simple model, insufficient features, or inadequate training |
| **Effect on Predictions** | Performs well only on training data but poorly on new data | Performs poorly on both training and testing data |
| **Signs** | Large gap between training and testing accuracy | Both training and testing accuracy remain low |
| **Example** | A Decision Tree with unlimited depth memorizes every training sample. | A Linear Regression model used for a highly non-linear dataset. |
| **How to Reduce** | • Use more training data<br>• Apply Regularization (L1/L2)<br>• Reduce model complexity<br>• Perform Feature Selection<br>• Use Cross-Validation<br>• Apply Early Stopping<br>• Use Dropout (Neural Networks)<br>• Prune Decision Trees | • Increase model complexity<br>• Add more relevant features<br>• Train for more epochs/iterations<br>• Reduce regularization<br>• Use a more powerful algorithm |
| **Goal** | Reduce variance while maintaining accuracy | Reduce bias while improving learning |

---

# Accuracy

Accuracy is the percentage of correctly predicted observations out of all observations.

## Formula

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Where:

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

## Example

Suppose a model correctly predicts 90 out of 100 samples.

Accuracy = 90 / 100 = 90%

Accuracy is useful when the classes are balanced.

# Precision

Precision measures how many of the instances predicted as positive are actually positive.

It answers the question:

> Out of all predicted positive cases, how many are truly positive?

## Formula

Precision = TP / (TP + FP)

## Example

If a model predicts 50 students will pass and 45 actually pass,

Precision = 45 / 50 = 90%

Precision is important when false positives are costly.

# Recall

Recall measures how many actual positive instances are correctly identified by the model.

It answers the question:

> Out of all actual positive cases, how many did the model correctly detect?

## Formula

Recall = TP / (TP + FN)

## Example

Suppose there are 60 actual positive cases and the model correctly identifies 54 of them.

Recall = 54 / 60 = 90%

Recall is important when missing positive cases is costly, such as disease detection or fraud detection.

# F1-Score

The F1-Score combines Precision and Recall into a single metric.

It is the harmonic mean of Precision and Recall.

## Formula

F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

## Example

If

- Precision = 90%
- Recall = 80%

Then

F1-Score = 84.7%

A high F1-Score indicates a good balance between Precision and Recall.

# Confusion Matrix

A Confusion Matrix is a table used to evaluate the performance of a classification model by comparing actual values with predicted values.

| Actual \ Predicted | Positive | Negative |
|--------------------|----------|----------|
| Positive | True Positive (TP) | False Negative (FN) |
| Negative | False Positive (FP) | True Negative (TN) |

## Definitions

- **True Positive (TP):** Correctly predicted positive cases.
- **True Negative (TN):** Correctly predicted negative cases.
- **False Positive (FP):** Incorrectly predicted positive cases.
- **False Negative (FN):** Incorrectly predicted negative cases.

## Example

Suppose a model predicts whether an email is spam.

- TP = Spam email correctly classified as spam.
- TN = Normal email correctly classified as normal.
- FP = Normal email incorrectly classified as spam.
- FN = Spam email incorrectly classified as normal.

The confusion matrix is used to calculate Accuracy, Precision, Recall, and F1-Score.


# Understanding True, False, Positive, and Negative in a Confusion Matrix

Before understanding TP, TN, FP, and FN, it is important to know what **Positive**, **Negative**, **True**, and **False** mean.

## Positive

A **Positive** prediction means the model predicts that the condition or event is present.

**Spam Email Example:**
- Positive = The email is **Spam**.

## Negative

A **Negative** prediction means the model predicts that the condition or event is absent.

**Spam Email Example:**
- Negative = The email is **Not Spam (Normal Email)**.

## True

**True** means the model's prediction is **correct**.

## False

**False** means the model's prediction is **incorrect**.

---


# Explanation of Each Term

### True Positive (TP)

- Actual class is **Positive (Spam)**.
- Model also predicts **Positive (Spam)**.
- **Prediction is correct.**

**Example:**

Actual Email = Spam

Predicted = Spam 

---

### True Negative (TN)

- Actual class is **Negative (Normal)**.
- Model predicts **Negative (Normal)**.
- **Prediction is correct.**

**Example:**

Actual Email = Normal

Predicted = Normal 

---

### False Positive (FP)

- Actual class is **Negative (Normal)**.
- Model predicts **Positive (Spam)**.
- **Prediction is incorrect.**

**Example:**

Actual Email = Normal

Predicted = Spam 

This is called a **False Alarm** because a normal email is wrongly marked as spam.

---

### False Negative (FN)

- Actual class is **Positive (Spam)**.
- Model predicts **Negative (Normal)**.
- **Prediction is incorrect.**

**Example:**

Actual Email = Spam

Predicted = Normal 

This means the spam email was missed.

---

# Classification Algorithms in Machine Learning

Classification algorithms are supervised learning algorithms used to predict categorical labels (classes), such as Spam/Not Spam, Yes/No, or Disease/No Disease.

---

# 1. Linear Models

| Algorithm | Description |
|-----------|-------------|
| Logistic Regression | Predicts the probability of class membership using the logistic (sigmoid) function. |
| Ridge Classifier | Linear classifier with L2 regularization. |
| SGD Classifier | Uses Stochastic Gradient Descent for large datasets. |
| Perceptron | A simple linear binary classifier and the foundation of neural networks. |

---

# 2. Tree-Based Algorithms

| Algorithm | Description |
|-----------|-------------|
| Decision Tree Classifier | Splits data into branches based on feature values. |
| Random Forest Classifier | Ensemble of multiple decision trees. |
| Extra Trees Classifier | Similar to Random Forest but uses more randomness. |

---

# 3. Support Vector Machines

| Algorithm | Description |
|-----------|-------------|
| Support Vector Machine (SVM) | Finds the optimal hyperplane to separate classes. |
| Linear SVM | SVM with a linear kernel. |
| Kernel SVM | Uses kernels (RBF, Polynomial, Sigmoid) for non-linear classification. |

---

# 4. Instance-Based (Lazy Learning)

| Algorithm | Description |
|-----------|-------------|
| K-Nearest Neighbors (KNN) | Classifies a sample based on the majority class of its nearest neighbors. |
| Radius Neighbors Classifier | Uses neighbors within a specified radius instead of a fixed number. |

---

# 5. Probabilistic Algorithms

| Algorithm | Description |
|-----------|-------------|
| Gaussian Naive Bayes | Assumes features follow a Gaussian distribution. |
| Multinomial Naive Bayes | Suitable for text classification and count data. |
| Bernoulli Naive Bayes | Designed for binary features. |
| Complement Naive Bayes | Improved Naive Bayes for imbalanced datasets. |

---

# 6. Ensemble Learning Algorithms

| Algorithm | Description |
|-----------|-------------|
| Random Forest | Ensemble of decision trees using bagging. |
| AdaBoost | Combines weak learners into a stronger classifier. |
| Gradient Boosting | Sequentially improves previous models' errors. |
| XGBoost | Optimized Gradient Boosting algorithm. |
| LightGBM | Fast Gradient Boosting algorithm by Microsoft. |
| CatBoost | Gradient Boosting algorithm designed for categorical features. |
| Bagging Classifier | Uses bootstrap sampling to improve stability. |
| Voting Classifier | Combines predictions from multiple classifiers. |
| Stacking Classifier | Uses multiple models and a meta-model for final prediction. |

---

# 7. Neural Networks

| Algorithm | Description |
|-----------|-------------|
| Multi-Layer Perceptron (MLP) | Feedforward artificial neural network. |
| Deep Neural Network (DNN) | Neural network with many hidden layers. |
| Convolutional Neural Network (CNN) | Mainly used for image classification. |
| Recurrent Neural Network (RNN) | Used for sequential data classification. |
| Long Short-Term Memory (LSTM) | A type of RNN for long-term dependencies. |
| Gated Recurrent Unit (GRU) | Simplified version of LSTM. |

---

# 8. Discriminant Analysis

| Algorithm | Description |
|-----------|-------------|
| Linear Discriminant Analysis (LDA) | Finds linear combinations of features for classification. |
| Quadratic Discriminant Analysis (QDA) | Similar to LDA but models each class separately. |

---

# 9. Rule-Based Algorithms

| Algorithm | Description |
|-----------|-------------|
| One Rule (OneR) | Creates one simple rule based on a single feature. |
| RIPPER | Rule-based classification algorithm. |
| Decision Rules | Classifies data using IF-THEN rules. |

---

# 10. Other Classification Algorithms

| Algorithm | Description |
|-----------|-------------|
| Nearest Centroid Classifier | Uses the centroid of each class. |
| Passive Aggressive Classifier | Online learning algorithm for large datasets. |
| Gaussian Process Classifier | Probabilistic non-parametric classifier. |
| Label Propagation | Semi-supervised classification algorithm. |
| Label Spreading | Improved version of Label Propagation. |

---



---
# What is Classification?

Classification is a **Supervised Machine Learning** technique used to predict **categorical (discrete) labels or classes** based on input data.

In classification, the target variable has a fixed number of categories, such as **Yes/No**, **Spam/Not Spam**, or **Pass/Fail**.

The model learns from labeled training data and predicts the class of new, unseen data.

## Examples

- Email → Spam or Not Spam
- Student → Pass or Fail
- Transaction → Fraud or Not Fraud
- Patient → Disease or No Disease
- Image → Cat or Dog

## Characteristics

- Predicts categorical values.
- Uses labeled training data.
- Used for binary and multi-class classification problems.

**Example:**

Input: Student's marks = 85

Output: Pass

# Classification vs Regression

Classification and Regression are both Supervised Machine Learning techniques, but they solve different types of problems.

| Feature | Classification | Regression |
|---------|---------------|------------|
| Purpose | Predicts categories or classes | Predicts continuous numerical values |
| Output | Discrete values | Continuous values |
| Target Variable | Categorical | Numerical |
| Example Output | Yes/No, Spam/Not Spam | House Price, Temperature |
| Algorithms | Logistic Regression, Decision Tree, Random Forest, SVM, KNN | Linear Regression, Decision Tree Regressor, Random Forest Regressor |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-Score | MAE, MSE, RMSE, R² Score |

## Examples

### Classification

- Predict whether an email is Spam or Not Spam.
- Predict whether a customer will buy a product.
- Predict whether a student will Pass or Fail.

### Regression

- Predict the price of a house.
- Predict tomorrow's temperature.
- Predict a student's final marks.

# Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for **classification problems**, especially binary classification.

Although its name contains "Regression," it is actually a classification algorithm because it predicts the probability that an observation belongs to a particular class.

The predicted probability ranges from **0 to 1** and is converted into a class label using a threshold (usually 0.5).

## Characteristics

- Used mainly for binary classification.
- Predicts probabilities.
- Uses the Sigmoid (Logistic) function.
- Simple and fast algorithm.
- Easy to interpret.

## Advantages

- Easy to implement.
- Fast training and prediction.
- Works well for linearly separable data.
- Produces probability values.

## Disadvantages

- Cannot model complex non-linear relationships.
- Performance decreases if classes overlap significantly.

## Applications

- Spam Email Detection
- Disease Prediction
- Customer Churn Prediction
- Credit Approval
- Fraud Detection

## Example

Input: Email Features

Output:
- Spam
- Not Spam

# Decision Trees

A Decision Tree is a supervised machine learning algorithm used for both classification and regression tasks.

It works by splitting the dataset into smaller subsets based on feature values. Each internal node represents a decision, each branch represents an outcome, and each leaf node represents the final prediction.

## Characteristics

- Easy to understand and visualize.
- Works with both numerical and categorical data.
- Requires little data preprocessing.
- Can perform classification and regression.

## Advantages

- Easy to interpret.
- Handles missing values well.
- No feature scaling required.
- Can model non-linear relationships.

## Disadvantages

- Can easily overfit the training data.
- Sensitive to small changes in the dataset.
- Large trees become complex.

## Applications

- Medical Diagnosis
- Loan Approval
- Student Performance Prediction
- Customer Segmentation
- Fraud Detection


| Application | Input | Predicted Class |
|-------------|-------|-----------------|
| Spam Email Detection | Email Content | Spam / Not Spam |
| Disease Diagnosis | Patient Symptoms | Disease / No Disease |
| Loan Approval | Customer Details | Approved / Rejected |
| Fraud Detection | Transaction Details | Fraud / Not Fraud |
| Face Recognition | Image | Person's Identity |
| Sentiment Analysis | Customer Review | Positive / Negative / Neutral |
| Student Result Prediction | Marks, Attendance | Pass / Fail |
| Credit Card Approval | Financial Information | Approved / Rejected |
| Weather Prediction | Weather Data | Rain / No Rain |
| Animal Classification | Image | Cat / Dog |
| Handwritten Digit Recognition | Digit Image | 0–9 |
| Product Recommendation | Customer Behavior | Buy / Not Buy |