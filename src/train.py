import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
import argparse
import logging

def setup_logging(log_level, log_file, console):
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=log_level, format=log_format, filename=log_file, filemode='w')

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(console_handler)

def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def train_model(train_data):
    logging.info("Training model...")
    housing = train_data.drop("median_house_value", axis=1)
    housing_labels = train_data["median_house_value"].copy()

    model = LinearRegression()
    model.fit(housing, housing_labels)
    logging.info("Model training complete.")
    
    return model

def save_model(model, output_path):
    os.makedirs(output_path, exist_ok=True)
    model_file = os.path.join(output_path, "model.pkl")
    joblib.dump(model, model_file)
    logging.info(f"Model saved to {model_file}")

def main(input_path, output_path, log_level, log_file, console):
    setup_logging(log_level, log_file, console)

    train_data = load_data(input_path)
    model = train_model(train_data)
    save_model(model, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train model script")
    parser.add_argument("--input_path", type=str, required=True, help="Input dataset path for training")
    parser.add_argument("--output_path", type=str, required=True, help="Output folder path for saving the model")
    parser.add_argument("--log_level", type=str, default="INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    parser.add_argument("--log_file", type=str, default="train.log", help="Log file path")
    parser.add_argument("--console", action="store_true", help="Enable console logging")
    args = parser.parse_args()
    
    main(args.input_path, args.output_path, args.log_level, args.log_file, args.console)
