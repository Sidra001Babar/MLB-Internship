import tensorflow as tf
import os

# 1. Download from a reliable alternative mirror
# This alternative link hosts the exact same 'cats_and_dogs_filtered' structure
url = "https://msropendata.azureedge.net/datasets/72df10df-01aa-4752-9653-5d75cb11f268/kagglecatsanddogs_5340.zip"

print("Downloading dataset from mirror (this may take a moment)...")
try:
    zip_dir = tf.keras.utils.get_file('cats_and_dogs_mirror.zip', origin=url, extract=True)
    
    # Get the extraction directory path
    base_dir = os.path.dirname(zip_dir)
    
    # Standard Kaggle extraction folder structure is usually 'PetImages'
    # Let's dynamically locate where the data went
    print(f"Extraction completed. Checking path: {base_dir}")
    
    # We will adjust variables depending on the extraction structure
    # If the mirror provides the classic PetImages structure, image_dataset_from_directory
    # splits it automatically if given a root folder with classes inside.
    dataset_dir = os.path.join(base_dir, 'PetImages')
    
    if not os.path.exists(dataset_dir):
        # Fallback check if it extracted differently
        dataset_dir = os.path.join(base_dir, 'cats_and_dogs_filtered')

    print(f"Loading datasets from: {dataset_dir}")

    # 2. Load directly into your train dataset
    train_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="training",
        seed=1337,
        image_size=(150, 150),
        batch_size=32
    )

    validation_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.2,
        subset="validation",
        seed=1337,
        image_size=(150, 150),
        batch_size=32
    )
    
    print("\nSuccessfully loaded datasets!")
    print(f"Class names found: {train_dataset.class_names}")

except Exception as e:
    print(f"\nAn error occurred during download/loading: {e}")
    print("If this fails, download the zip manually in your browser, extract it,")
    print("and paste the 'train' and 'validation' folders directly inside 'Day12'.")