import argparse
import logging
import os

import yaml


def read_params(config_path):
    # read the config path
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
        print("Config Info : \n",config)
    return config

def main(config_path, datasource):
    """main operation function"""

    # step1 . read config file
    config_meta =  read_params(config_path=config_path)

    return None

if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='config/pipeline.yaml')
    args.add_argument("--datasource", default='data/raw/wafer-dataset-main')

    parsed_args =  args.parse_args()

    # call the main function
    main(config=parsed_args.config, datasource=parsed_args.datasource )
