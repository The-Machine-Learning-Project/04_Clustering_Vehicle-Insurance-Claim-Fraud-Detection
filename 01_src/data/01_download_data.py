# Download data from Kaggle

# TODO: STUDY HOW TO DOWNLOAD FILES FROM KAGGLE USING THE API -- https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection

# import subprocess

# def download_kaggle_dataset(username, dataset_name, destination_path='.'):
#     # Replace 'username/dataset-name' with the actual username and dataset name
#     dataset_full_name = f'{username}/{dataset_name}'

#     # Download the dataset to the specified destination path
#     download_command = f'kaggle datasets download {dataset_full_name} -p {destination_path}'
#     subprocess.run(download_command, shell=True)

# if __name__ == "__main__":
#     # Replace 'your_username' and 'your_dataset_name' with your Kaggle username and dataset name
#     kaggle_username = 'shivamb'
#     kaggle_dataset_name = 'vehicle-claim-fraud-detection'

#     # Specify the destination path (default is the current directory)
#     destination_path = '././02_data/01_raw/vehicle_insurance_data.csv'

#     # Call the function to download the dataset
#     download_kaggle_dataset(kaggle_username, kaggle_dataset_name, destination_path)

