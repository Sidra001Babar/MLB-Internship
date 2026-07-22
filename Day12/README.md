# Cats vs Dogs Image Classifier using Transfer Learning

## What is Transfer Learning?

Transfer Learning is a machine learning technique in which a model that has already been trained on a large dataset is reused for a different but related task. Instead of training a neural network from scratch, the pretrained model is used as a feature extractor, and only the final classification layers are trained on the new dataset. This approach reduces training time, requires fewer computational resources, and often achieves high accuracy.

---

## Why did you choose MobileNetV2?

MobileNetV2 was selected because it is a lightweight and efficient convolutional neural network pretrained on the ImageNet dataset. It provides strong feature extraction capabilities while requiring fewer computational resources than many larger models. Since this project involves binary image classification (Cats vs Dogs), MobileNetV2 offers an excellent balance between accuracy and speed. It also performs well even when the pretrained layers are frozen.

---

## What experiments did you perform to improve accuracy?

The following experiments and preprocessing steps were performed:

- Loaded the Cats vs Dogs dataset from a local directory.
- Cleaned the dataset by removing corrupted and unreadable images before training.
- Resized all images to **224 × 224** pixels.
- Applied MobileNetV2's `preprocess_input()` function.
- Split the dataset into **80% training** and **20% validation**.
- Used the pretrained **MobileNetV2** model with **ImageNet** weights.
- Froze the pretrained base model.
- Added a **GlobalAveragePooling2D** layer.
- Added a single **Dense** output layer with **sigmoid** activation.
- Used the **Adam** optimizer and **Binary Crossentropy** loss function.
- Trained the model for **5 epochs**.
- Plotted training and validation accuracy and loss graphs.
- Saved the trained model after training.

---

## Final Validation Accuracy

**Final Validation Accuracy:** **98.7%**


---

## Key Challenges and Lessons Learned

### Challenges

- The original Kaggle Cats vs Dogs dataset contained corrupted and unreadable image files.
- Some images had invalid formats or unsupported channel configurations, causing TensorFlow decoding errors.
- A separate preprocessing script was created to remove corrupted images before model training.
- Ensuring graphs and the trained model were automatically saved in the project directory.

### Lessons Learned

- Transfer Learning significantly reduces training time while achieving high accuracy.
- MobileNetV2 provides excellent performance without requiring a complex neural network architecture.
- Proper dataset preprocessing is essential for successful model training.
- Monitoring both training and validation accuracy helps evaluate how well the model generalizes to unseen data.
- Separating dataset cleaning from model training results in a cleaner and more maintainable project structure.

---
### Workflow 

1. Run `clean_dataset.py` once to remove corrupted images.
2. Run `transferLearning.py` to train and evaluate the model.
3. View the generated accuracy and loss graphs.
4. Use the saved `.keras` model for future predictions.