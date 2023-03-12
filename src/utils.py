import argparse
import logging
import os
import pathlib

import pandas as pd
import yaml


def read_params(config_path):
    """read the config file and restore into dict"""
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
