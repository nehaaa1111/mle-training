import os
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
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

def load_model(model_path):
    logging.info(f"Loading model from {model_path}")
    return joblib.load(model_path)

def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def score_model(model, data):
    logging.info("Scoring model...")
    X = data.drop("median_house_value", axis=1)
    y = data["median_house_value"].copy()
    
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    rmse = np.sqrt(mse)
    
    logging.info(f"Model RMSE: {rmse}")
    return rmse

def main(model_path, dataset_path, output_path, log_level, log_file, console):
    setup_logging(log_level, log_file, console)

    model = load_model(model_path)
    val_data = load_data(dataset_path)
    
    rmse = score_model(model, val_data)
    
    with open(os.path.join(output_path, "score.txt"), "w") as f:
        f.write(f"RMSE: {rmse}")
    logging.info(f"Score saved to {output_path}/score.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score model script")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the model pickle file")
    parser.add_argument("--dataset_path", type=str, required=True, help="Validation dataset path")
    parser.add_argument("--output_path", type=str, required=True, help="Output folder path for saving the score")
    parser.add_argument("--log_level", type=str, default="INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    parser.add_argument("--log_file", type=str, default="score.log", help="Log file path")
    parser.add_argument("--console", action="store_true", help="Enable console logging")
    args = parser.parse_args()
    
    main(args.model_path, args.dataset_path, args.output_path, args.log_level, args.log_file, args.console)
