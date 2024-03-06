# Download data from Kaggle

""" SETUP REQUIREMENTS:
    1. Download API Key (kaggle.json) from kaggle
    2. Move the kaggle.json file to the same directory as this code
"""

import opendatasets
import os
import shutil

def download_and_move_kaggle_dataset(dataset_full_path, source_folder, destination_folder):
    # Download the dataset to the specified destination folder
    opendatasets.download(dataset_full_path)

    # Move files to the specified folder
    move_files(source_folder, destination_folder)

def move_files(source_folder, destination_folder):
    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Move the file to the destination folder
        shutil.move(source_path, destination_path)

        # Delete the source folder
        os.rmdir(source_folder)

if __name__ == "__main__":
    # Replace 'your_username' and 'your_dataset_name' with your Kaggle username and dataset name
    dataset_full_path = 'https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection'

    # Specify the folder for downloading
    source_folder = dataset_full_path.split('/')[-1]

    # Specify the folder where you want to move the files
    destination_folder = '../../02_data/01_raw/'

    # Call the function to download and move the dataset
    download_and_move_kaggle_dataset(dataset_full_path, source_folder, destination_folder)
    
    print(f"Downloaded file successfully to {destination_folder}!")