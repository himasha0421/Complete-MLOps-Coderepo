"""this module responsible for data preprocessing
apply null value imputation
apply robust scaler 
clip outliers from column values
"""

import argparse
import logging
import os
import pathlib

import pandas as pd
import yaml

from utils import read_params


def main(config_path, stage):
    """main function to handle data preprocessing"""
    config_meta = read_params(config_path=config_path)
    source_meta = config_meta["data_source"][stage]
    preprocessing_meta = config_meta["data_preprocessing"][stage]

    #read the raw csv
    df_raw = pd.read_csv(os.path.join(config_meta["data_source"]["base_path"], source_meta['final_file']) , 
                         index_col=0 )

    #save the preprocessed csv
    pathlib.Path(preprocessing_meta['base_dir']).mkdir(parents=True, exist_ok=True) 
    # dump to csv
    df_raw.to_csv(os.path.join(preprocessing_meta['base_dir'],preprocessing_meta['filepath']) ,
                  index=True  )


if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='config/params.yaml')
    args.add_argument("--stage", default="train")
    parsed_args =  args.parse_args()

    # call the main function
    df = main(config_path=parsed_args.config, stage=parsed_args.stage )

