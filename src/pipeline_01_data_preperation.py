import argparse
import logging
import os
import pathlib

import pandas as pd
import yaml

from utils import read_params


def read_dataset(main_dir, file_paths):
    """read the csv data files and check for good files and remove bad file
    that not having Good/Bad column
    
    """
    #define df placeholder
    dfs = []
    # read each dataframe 
    for i_file in file_paths:
        if(i_file.endswith(".csv")):
            full_path = os.path.join(main_dir, i_file)
            #read the csv
            df = pd.read_csv(full_path, index_col=0)
            # need to check whether dataset having the target column like Good/Bad if not disregard the df for traning
            cols =  df.columns
            if( 'Good/Bad' in cols ):
                dfs.append(df)

    # concat all the dataframes into one
    final_df = pd.concat(dfs, axis=0)
    return final_df


def main(config_path, stage):
    """main operation function"""

    # step1 . read config file
    config_meta =  read_params(config_path=config_path)
    # step2. load the csv files based on the stage
    main_dir =  config_meta['data_source'][stage]["raw_files"]
    #step3. read the csv files inside the main dir
    csv_files =  os.listdir(main_dir)
    #step4. read the csv files and collate into one single file
    df = read_dataset(main_dir=main_dir,
                      file_paths=csv_files
                      )
    #print some stasts
    print("Dataset Stats n.rows : {} n.columns : {}".format(df.shape[0],df.shape[1]))

    #step5. save the dataset into raw folder
    base_save_dir = config_meta['data_source']["base_path"]
    pathlib.Path(base_save_dir).mkdir(parents=True, exist_ok=True) 
    # save to csv
    df.to_csv(os.path.join(base_save_dir, config_meta['data_source'][stage]["final_file"] ),
              index=True,
              )

    return df

if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='params.yaml')
    args.add_argument("--stage", default="train")
    parsed_args =  args.parse_args()

    # call the main function
    df = main(config_path=parsed_args.config, stage=parsed_args.stage )
