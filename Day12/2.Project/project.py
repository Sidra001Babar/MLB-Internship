import os
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense


########## Save outputs in the same folder as this Python file
output_dir = os.path.dirname(os.path.abspath(__file__))

########## Dataset Path
dataset_path = r"D:\Downloads\kagglecatsanddogs_5340\PetImages"

########## Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
SEED = 42
EPOCHS = 5

######### Load Dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_dataset.class_names

print("\nClasses:", class_names)

########## Display Sample Images
plt.figure(figsize=(8, 8))

for images, labels in train_dataset.take(1):

    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

plt.tight_layout()
plt.show()

######### Preprocessing

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.map(
    lambda x, y: (preprocess_input(x), y),
    num_parallel_calls=AUTOTUNE
)

validation_dataset = validation_dataset.map(
    lambda x, y: (preprocess_input(x), y),
    num_parallel_calls=AUTOTUNE
)

train_dataset = train_dataset.prefetch(AUTOTUNE)
validation_dataset = validation_dataset.prefetch(AUTOTUNE)

########## Load MobileNetV2

base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

############## Freeze pretrained model
base_model.trainable = False

############### Build Model

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(1, activation="sigmoid")
])

############# Compile Model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

############# Model Summary
model.summary()

############# Train Model
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=EPOCHS
)

############ Evaluate Model
loss, accuracy = model.evaluate(validation_dataset)

print("\n==============================")
print(f"Validation Loss     : {loss:.4f}")
print(f"Validation Accuracy : {accuracy * 100:.2f}%")
print("==============================")

############### Accuracy Graph
plt.figure(figsize=(8, 5))

plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")

plt.title("Training vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)

accuracy_path = os.path.join(output_dir, "accuracy_graph.png")
plt.savefig(accuracy_path, dpi=300, bbox_inches="tight")

plt.show()

############# Loss Graph
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.title("Training vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)

loss_path = os.path.join(output_dir, "loss_graph.png")
plt.savefig(loss_path, dpi=300, bbox_inches="tight")

plt.show()

############ Display Sample Predictions
plt.figure(figsize=(10, 10))

for images, labels in validation_dataset.take(1):

    predictions = model.predict(images, verbose=0)

    for i in range(9):

        plt.subplot(3, 3, i + 1)

        # Convert back to displayable image
        display_image = (images[i].numpy() + 1) / 2
        display_image = display_image.clip(0, 1)

        plt.imshow(display_image)

        predicted = "Dog" if predictions[i][0] > 0.5 else "Cat"
        actual = class_names[labels[i]]

        plt.title(f"Pred: {predicted}\nActual: {actual}")
        plt.axis("off")

plt.tight_layout()
plt.show()

############### Save Model


model_path = os.path.join(output_dir, "cats_vs_dogs_mobilenet.keras")
model.save(model_path)
