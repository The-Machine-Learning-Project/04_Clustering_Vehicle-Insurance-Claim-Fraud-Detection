# Download data from Kaggle


# Import Libraries
import pandas as pd
import requests


# URL to the file
path = 'https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/download?datasetVersionNumber=1'

# Send a GET request to the URL
response = requests.get(path)

# Check if the request was successful (status code 200)
if response.status_code == 200:

    # Save the content to a local CSV file
    with open('././02_data/01_raw/vehicle_insurance_data.csv', 'wb') as local_file:
        local_file.write(response.content)
    print('File downloaded successfully.')

else:
    print(f'Failed to download the file. Status code: {response.status_code}')

