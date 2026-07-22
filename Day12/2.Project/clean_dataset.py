import os
import tensorflow as tf

################# Dataset Path
dataset_path = r"D:\Downloads\kagglecatsanddogs_5340\PetImages"

removed = 0

print("Checking dataset for invalid images...\n")

for folder in ["Cat", "Dog"]:

    folder_path = os.path.join(dataset_path, folder)

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        try:
            # Read image
            image = tf.io.read_file(file_path)
            image = tf.io.decode_jpeg(image, channels=3)
            _ = image.numpy()

        except Exception as e:

            print(f"Deleting: {file_path}")
            print(f"Reason: {e}\n")

            try:
                os.remove(file_path)
                removed += 1
            except Exception as delete_error:
                print(f"Could not delete {file_path}")
                print(delete_error)

print(f"Removed {removed} invalid images.")
