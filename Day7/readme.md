# Classification

Classification is a **Supervised Machine Learning** technique used to predict **categorical (discrete) classes** based on input features. The model learns from labeled training data and assigns new, unseen data to one of the predefined classes.

### Examples

- Flower → Setosa, Versicolor, or Virginica

---

# Difference Between Regression and Classification

| Classification | Regression |
|----------------|------------|
| Predicts categorical (discrete) values or classes. | Predicts continuous numerical values. |
| Output is a class label. | Output is a numeric value. |
| Used when the target variable is categorical. | Used when the target variable is continuous. |
| Examples: Spam Detection, Disease Diagnosis, Pass/Fail Prediction. | Examples: House Price Prediction, Temperature Forecasting, Sales Prediction. |
| Common algorithms include Logistic Regression, Decision Tree, Random Forest, KNN, and SVM. | Common algorithms include Linear Regression, Decision Tree Regressor, and Random Forest Regressor. |
| Evaluation metrics include Accuracy, Precision, Recall, F1-Score, and Confusion Matrix. | Evaluation metrics include MAE, MSE, RMSE, and R² Score. |

---

# Evaluation Metrics Used

The following metrics are commonly used to evaluate the performance of classification models:

### Accuracy
Accuracy measures the overall proportion of correctly classified samples out of all predictions.

### Precision
Precision measures how many of the samples predicted as positive are actually positive. It is important when minimizing false positives is a priority.

### Recall
Recall measures how many actual positive samples are correctly identified by the model. It is important when minimizing false negatives is critical.

### F1-Score
The F1-Score is the harmonic mean of Precision and Recall. It provides a balanced measure when both Precision and Recall are important.

### Confusion Matrix
A Confusion Matrix compares the actual class labels with the predicted class labels. It provides a detailed summary of correct and incorrect predictions and helps identify where the model makes errors.

---

# Model Performance and Observations

The performance of a classification model is evaluated using Accuracy, Precision, Recall, F1-Score, and the Confusion Matrix.

### General Observations

- Higher Accuracy indicates better overall prediction performance.
- High Precision means the model produces fewer false positive predictions.
- High Recall means the model correctly identifies most of the actual positive instances.
- A high F1-Score indicates a good balance between Precision and Recall.
- In a Confusion Matrix, most values should appear along the diagonal, indicating correct classifications.
- Large differences between training and testing performance may indicate overfitting, while low performance on both datasets may indicate underfitting.

A well-performing classification model should achieve high evaluation metric values while maintaining good generalization on unseen data.