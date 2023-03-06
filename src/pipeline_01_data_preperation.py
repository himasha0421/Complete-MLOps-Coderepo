import argparse
import logging
import os

import yaml

if __name__=='__main__':
    args =  argparse.ArgumentParser()
    # add arguments
    args.add_argument("--config", default='config/pipeline.yaml')
    args.add_argument("--datasource", default='data/raw/wafer-dataset-main')

    parsed_args =  args.parse_args()
