# split the raw data 
# save it in data/processed folder
import argparse
import os
import pathlib

import pandas as pd
from sklearn.model_selection import train_test_split

from pipeline_01_data_preperation import read_params


def split_and_saved_data(config_path):
    # load the config meta
    config = read_params(config_path)
    base_save_dir = config["split_data"]["base_path"] 
    dev_data_path = config["split_data"]["dev_path"] 
    train_data_path = config["split_data"]["train_path"]

    # load the raw preprocessed dataset
    base_dir , file_path =  config["data_preprocessing"]["train"] , config["data_preprocessing"]["train_filepath"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    df = pd.read_csv(os.path.join(base_dir, file_path), delimiter=",", index_col=0)
    #split data
    train, dev = train_test_split(
        df, 
        test_size=split_ratio, 
        random_state=random_state
        )
    # save csv files
    pathlib.Path(base_save_dir).mkdir(parents=True, exist_ok=True) 
    train.to_csv(os.path.join(base_save_dir, train_data_path),
                 sep=",",
                 index=True)
    dev.to_csv(os.path.join(base_save_dir, dev_data_path), 
               sep=",", 
               index=True)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="config/params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)
