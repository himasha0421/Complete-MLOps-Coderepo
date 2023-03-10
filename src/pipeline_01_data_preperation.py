import argparse
import logging
import os

import pandas as pd
import yaml


def read_dataset(main_dir, file_paths):
    #define df placeholder
    dfs = []
    # read each dataframe 
    for i_file in file_paths:
        full_path = os.path.join(main_dir, i_file)
        #read the csv
        df = pd.read_csv(full_path, delimiter=",")
        dfs.append(df)

    # concat all the dataframes into one
    final_df = pd.concat(dfs, axis=0)
    return final_df


def read_params(config_path):
    # read the config path
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def main(config_path, stage):
    """main operation function"""

    # step1 . read config file
    config_meta =  read_params(config_path=config_path)
    # step2. load the csv files based on the stage
    main_dir =  config_meta['data_source'][stage]
    #step3. read the csv files inside the main dir
    csv_files =  os.listdir(main_dir)
    #step4. read the csv files and collate into one single file
    df = read_dataset(main_dir=main_dir,
                      file_paths=csv_files
                      )
    #print some stasts
    print("Dataset Stats n.rows : {} n.columns : {}".format(df.shape[0],df.shape[1]))
    return df

if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='config/params.yaml')
    args.add_argument("--stage", default="train")
    parsed_args =  args.parse_args()

    # call the main function
    df = main(config_path=parsed_args.config, stage=parsed_args.stage )
