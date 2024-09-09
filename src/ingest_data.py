"""
Data Ingestion Script for Housing Dataset.

This script downloads, processes, and splits the housing dataset into training and validation sets, 
and saves them to the specified output path. It also provides logging capabilities to track the 
progress of the ingestion process.

Modules
-------
- `os`: For file and directory operations.
- `pandas`: For data manipulation and analysis.
- `sklearn.model_selection`: For splitting data into training and validation sets.
- `argparse`: For parsing command-line arguments.
- `logging`: For logging information to a file or console.

Functions
---------
- `setup_logging(log_level, log_file, console)`: Configures logging for the script.
- `fetch_housing_data(housing_url, housing_path)`: Downloads and extracts the housing dataset from the specified URL.
- `load_housing_data(housing_path)`: Loads the housing data from a CSV file.
- `save_data(data, output_path, file_name)`: Saves a pandas DataFrame to a CSV file.
- `main(output_path, log_level, log_file, console)`: The main entry point of the script that orchestrates the data ingestion process.

Usage
-----
1. Run the script from the command line with the necessary arguments:
   
   ```bash
   python ingest_data.py --output_path <output_directory> --log_level INFO --log_file ingest_data.log --console
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse
import logging


def setup_logging(log_level, log_file, console):
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=log_level, format=log_format,
                        filename=log_file, filemode='w')

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(console_handler)


def fetch_housing_data(housing_url, housing_path):
    logging.info("Fetching housing data...")
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    logging.info("Housing data fetched successfully.")


def load_housing_data(housing_path):
    logging.info("Loading housing data...")
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def save_data(data, output_path, file_name):
    output_file = os.path.join(output_path, file_name)
    data.to_csv(output_file, index=False)
    logging.info(f"Data saved to {output_file}")


def main(output_path, log_level, log_file, console):
    setup_logging(log_level, log_file, console)

    housing_url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz"
    housing_path = os.path.join(output_path, "housing")

    fetch_housing_data(housing_url, housing_path)
    housing = load_housing_data(housing_path)

    train_set, val_set = train_test_split(housing, test_size=0.2, random_state=42)

    save_data(train_set, output_path, "train.csv")
    save_data(val_set, output_path, "val.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest data script")
    parser.add_argument("--output_path", type=str, required=True,
                        help="Output folder path for the datasets")
    parser.add_argument("--log_level", type=str, default="INFO",
                        help="Logging level (\
                                                DEBUG, INFO, WARNING, ERROR,\
                                                      CRITICAL)")
    parser.add_argument("--log_file", type=str,
                        default="ingest_data.log", help="Log file path")
    parser.add_argument("--console", action="store_true",
                        help="Enable console logging")
    args = parser.parse_args()

    main(args.output_path, args.log_level, args.log_file, args.console)
