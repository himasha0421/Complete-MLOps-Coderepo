"""this module responsible for data preprocessing
apply null value imputation
apply robust scaler 
clip outliers from column values
"""

import argparse
import logging
import os
import pathlib

import numpy as np
import pandas as pd
import yaml
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler

from utils import read_params


def scaler(df):
    """apply robust scaling"""
    scaler_obj = RobustScaler()
    #apply transform
    df_scaled = scaler_obj.fit_transform(df)
    return df_scaled


def knnimputer(df, meta_data):
    """null value imputation with knn imputer"""
    # init params
    neighbors = meta_data['KNNImputer']['n_neighbors']
    weights = meta_data['KNNImputer']['weights']
    missing_values = meta_data['KNNImputer']['missing_values']

    # init the imputer object
    imputer = KNNImputer(
        n_neighbors=neighbors,
        weights=weights,
        missing_values=np.nan
    )
    df_imputed = imputer.fit_transform(df)
    return df_imputed



def main(config_path, stage):
    """main function to handle data preprocessing"""
    config_meta = read_params(config_path=config_path)
    source_meta = config_meta["data_source"][stage]
    preprocessing_meta = config_meta["data_preprocessing"][stage]

    #read the raw csv
    df_raw = pd.read_csv(os.path.join(config_meta["data_source"]["base_path"], source_meta['final_file']) , 
                         index_col=0 )
    # remap the target variable to 0/1
    df_raw['Good/Bad'] = df_raw['Good/Bad'].apply(lambda x:( 0 if x<0 else 1 ))

    #drop target variable
    df_target = df_raw[['Good/Bad']]
    # apply knnimputation
    df_imputed = knnimputer(df_raw.drop(columns=['Good/Bad'],axis=1),
                            meta_data=config_meta["data_preprocessing"]
                            )
    # aply robust scaler
    scaled_features = scaler(df_imputed)
    df_scaled = pd.DataFrame(scaled_features, 
                             index=df_raw.index, columns=df_raw.drop(columns=['Good/Bad'],axis=1).columns)

    # concat the targets
    df_scaled['Good/Bad'] =  df_target

    #dataset stats
    print("Dataset Stats:", df_scaled.describe())
    print("Null Values :", df_scaled.isna().sum())

    #save the preprocessed csv
    pathlib.Path(preprocessing_meta['base_dir']).mkdir(parents=True, exist_ok=True) 
    # dump to csv
    df_scaled.to_csv(os.path.join(preprocessing_meta['base_dir'],preprocessing_meta['filepath']) ,
                  index=True  )


if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='params.yaml')
    args.add_argument("--stage", default="train")
    parsed_args =  args.parse_args()

    # call the main function
    df = main(config_path=parsed_args.config, stage=parsed_args.stage )

