import os
import numpy as np

# Define the local file path
local_file_path = 'E:\\2nd semester\\nlp\\Project\\dataset.txt'  # Update this path to your actual dataset location

# Define the directory to store the processed data
data_dir = 'data/openwebtext'
os.makedirs(data_dir, exist_ok=True)

# Read the dataset from the local file
with open(local_file_path, 'r', encoding='utf-8') as file:
    raw_text = file.read()

# Convert the text to a sequence of integers (tokenization)
data = np.array([ord(c) for c in raw_text], dtype=np.uint16)

# Save the data to a binary file
with open(os.path.join(data_dir, 'train.bin'), 'wb') as f:
    data.tofile(f)

print("Dataset has been read from the local file and preprocessed successfully.")
