# Image Classification Workflow

Image classification is the process of training a deep learning model to identify and assign a label to an input image. A CNN learns patterns from images and predicts the correct class.

## Workflow


Collect Image Dataset >> Explore the Dataset >> Preprocess Images(Resize, Normalize) >> Split Dataset(Training, Validation, Testing)  >> Data Augmentation (Optional) >> Build CNN Model >> Train the Model >> Validate During Training >> Evaluate on Test Data >> Make Predictions




# Training vs Validation Data

Deep learning datasets are usually divided into three parts.

```
Dataset

100%

│

├── Training Data (70–80%)

├── Validation Data (10–20%)

└── Testing Data (10–20%)
```

---

## Training Data

Training data is used to teach the neural network.

The model:

- Learns features
- Updates weights
- Reduces training loss

Example

```
48,000 Images
```

The CNN learns from these images.

---

## Validation Data

Validation data is **not used to update weights**.

Instead, it is used to:

- Monitor performance
- Tune hyperparameters
- Detect overfitting
- Select the best model

Example

```
12,000 Images
```

The CNN only evaluates these images after each epoch.

---

## Testing Data

Testing data is used only after training is complete.

Purpose:

- Measure final performance
- Evaluate generalization ability

The model has never seen these images before.

---

## Comparison

| Feature | Training Data | Validation Data | Testing Data |
|----------|---------------|-----------------|--------------|
| Used to Learn |  Yes |  No |  No |
| Updates Weights |  Yes |  No |  No |
| Used During Training |  Yes |  Yes |  No |
| Used After Training |  No | Sometimes |  Yes |
| Purpose | Learn patterns | Tune and monitor model | Final evaluation |

---

# Epochs and Batch Size

## What is an Epoch?

An **epoch** means the model has processed the **entire training dataset once**.

Example

Training Images

```
60,000
```

Epoch = 1

The CNN has seen all 60,000 images once.

Epoch = 5

The CNN has seen the complete dataset five times.

---

## What is Batch Size?

Instead of processing all images together, they are divided into smaller groups called batches.

Example

Training Images

```
60,000
```

Batch Size

```
32
```

Number of batches

```
60,000 / 32 ≈ 1,875 batches
```

The model updates its weights after each batch.

---

## Example

Suppose

```
100 Images
Batch Size = 20
```

Then

```
Batch 1 → 20 Images

Batch 2 → 20 Images

Batch 3 → 20 Images

Batch 4 → 20 Images

Batch 5 → 20 Images
```

After all five batches are processed,

```
1 Epoch Completed
```

---

## Effect of Batch Size

| Small Batch | Large Batch |
|--------------|-------------|
| Slower training | Faster training |
| Uses less memory | Uses more memory |
| More frequent weight updates | Fewer weight updates |
| Better generalization | Can converge faster but may generalize less well |

---

# Overfitting in Deep Learning

Overfitting occurs when the model learns the **training data too well**, including its noise and specific details, causing poor performance on new data.

---

## Signs of Overfitting

Example

```
Training Accuracy

99%

Validation Accuracy

84%
```

Large gap

↓

Overfitting

---



Training accuracy keeps increasing.

Validation accuracy stops improving or decreases.

---

## Causes

- Too many epochs
- Very complex model
- Small dataset
- No regularization
- No data augmentation

---

## Solutions

- Data Augmentation
- Dropout
- Early Stopping
- Regularization
- Collect more data
- Simpler model

---

# Data Augmentation (Concept)

Data augmentation artificially increases the size and diversity of the training dataset by creating modified versions of existing images.

It helps improve generalization and reduce overfitting.

---

## Common Techniques

### 1. Rotation
### 2. Horizontal Flip
### 3. Zoom
### 4. Shift
### 5. Brightness
### 6. Shear: Tilt the image slightly.
## Benefits

- More training data
- Better generalization
- Reduces overfitting
- Improves robustness
- Helps recognize objects in different orientations

---

# Model Evaluation

After training, we evaluate how well the model performs on unseen test data.

Common evaluation metrics include:

---

## Accuracy

Measures the percentage of correctly classified images.

Formula

```
Accuracy

=

Correct Predictions

/

Total Predictions
```

Example

```
Correct Predictions

900

Total Images

1000

Accuracy

=

90%
```

---

## Loss

Loss measures how far the model's predictions are from the true labels.

- Lower loss indicates better performance.
- During training, we aim to minimize the loss.

---

## Confusion Matrix

Shows how many predictions are correct and where the model makes mistakes.

Example

| Actual \ Predicted | Cat | Dog |
|--------------------|-----|-----|
| Cat | 45 | 5 |
| Dog | 3 | 47 |

---

## Precision

Out of all images predicted as a certain class, precision tells us how many were actually correct.

---

## Recall

Out of all actual images belonging to a class, recall tells us how many the model correctly identified.

---

## F1-Score

The F1-score combines precision and recall into a single metric, providing a balanced measure of model performance, especially for imbalanced datasets.

---


