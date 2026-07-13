# Fashion MNIST Classification using Artificial Neural Network (ANN)

## Project Overview

This project demonstrates the implementation of a simple **Artificial Neural Network (ANN)** using **TensorFlow/Keras** to classify images from the **Fashion MNIST** dataset. The project includes dataset exploration, preprocessing, hyperparameter tuning using **Keras Tuner**, model training, evaluation, and prediction.

---

# What is Deep Learning?

**Deep Learning (DL)** is a subset of **Machine Learning (ML)** that uses **Artificial Neural Networks (ANNs)** with multiple hidden layers to automatically learn patterns from large amounts of data.

Unlike traditional machine learning, deep learning automatically extracts important features from raw data such as images, text, audio, and videos without requiring manual feature engineering.

**Applications of Deep Learning include:**
- Image Classification
- Object Detection
- Self-Driving Cars
- Virtual Assistants
- Speech Recognition
- Language Translation
- Medical Image Analysis
- Recommendation Systems

---

# Difference Between Machine Learning and Deep Learning

| Machine Learning | Deep Learning |
|------------------|---------------|
| Requires manual feature engineering | Learns features automatically |
| Works well with smaller datasets | Requires large datasets |
| Faster training | Longer training time |
| Can run efficiently on CPUs | Often requires GPUs/TPUs |
| Easier to interpret | More difficult to interpret (Black Box) |

---

# What is a Perceptron?

A **Perceptron** is the simplest form of an Artificial Neural Network and serves as the basic building block of deep learning models.

A perceptron:
- Receives one or more input values.
- Multiplies each input by a corresponding weight.
- Adds a bias.
- Applies an activation function.
- Produces an output.

It is mainly used for **binary classification** problems where the output is either **0** or **1**.

Mathematically,

```
Output = Activation((Inputs × Weights) + Bias)
```

---

# Activation Functions Explored

The following activation functions were explored during this project.

## ReLU (Rectified Linear Unit)

**Output Range:** 0 to ∞

**Common Uses:**
- Hidden layers of deep neural networks
- Image classification
- Computer vision applications

**Advantages**
- Fast computation
- Reduces the vanishing gradient problem
- Most commonly used hidden-layer activation

---

## Sigmoid

**Output Range:** 0 to 1

**Common Uses:**
- Binary classification
- Logistic Regression
- Output layer for binary classification models

**Advantages**
- Produces probability values
- Smooth and continuous output

---

## Tanh (Hyperbolic Tangent)

**Output Range:** -1 to 1

**Common Uses:**
- Hidden layers in some neural networks
- Recurrent Neural Networks (RNNs)

**Advantages**
- Zero-centered output
- Often converges faster than Sigmoid

---

## Softmax

**Output Range:** 0 to 1 (probabilities sum to 1)

**Common Uses:**
- Multi-class classification
- Image classification
- Text classification

**Advantages**
- Produces a probability distribution over all classes
- Selects the class with the highest probability

---

# Model Architecture

The implemented ANN consists of:

- Flatten Layer (28 × 28 → 784)
- Hidden Layer 1 (Dense)
- Hidden Layer 2 (Dense)
- Output Layer (10 Neurons, Softmax)

Hyperparameters such as:
- Number of neurons
- Activation functions
- Learning rate

were optimized using **Keras Tuner RandomSearch**.

---

# Dataset

Dataset Used:

- Fashion MNIST
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Number of Classes: 10

---

# Data Preprocessing

The following preprocessing steps were performed:

- Loaded the Fashion MNIST dataset
- Explored dataset shape and labels
- Displayed sample images
- Normalized pixel values from **0–255** to **0–1**

---

# Model Performance

## Model Performance

- **Final Training Accuracy:** **91.30%**
- **Final Validation Accuracy:** **89.03%**
- **Final Testing Accuracy:** **88.51%**



---

# Technologies Used

- Python
- TensorFlow
- Keras
- Keras Tuner
- NumPy
- Matplotlib

---

# Conclusion

This project demonstrates how an Artificial Neural Network can classify Fashion MNIST images effectively. Hyperparameter tuning with **Keras Tuner** improved the model by identifying suitable values for the number of neurons, activation functions, and learning rate. The trained model achieved strong classification performance on the Fashion MNIST test dataset.