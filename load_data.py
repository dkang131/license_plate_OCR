import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_data(dataset, destination_folder):
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=destination_folder, unzip=True)
    print(f"Finished Download and extract {dataset} to {destination_folder}")


dataset = 'nickyazdani/license-plate-text-recognition-dataset'
destination_folder = 'license_plate_dataset'

os.makedirs(destination_folder, exist_ok=True)

download_data(dataset, destination_folder)
