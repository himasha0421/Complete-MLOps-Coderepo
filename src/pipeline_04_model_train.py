# load the train and test
# train algo
# save the metrices, params
import argparse
import json
import os
import sys
import warnings

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet, LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

from utils import read_params


def eval_metrics(actual, pred):
    precision, recall, f1_score , _ = precision_recall_fscore_support(actual, pred, average='weighted')
    accuracy = accuracy_score(actual, pred)
    return precision, recall, f1_score, accuracy

def train_and_evaluate(config_path):
    """train and evaluate the model on preprocessed dataset"""

    #read configs
    config = read_params(config_path)
    base_split_dir =  config["split_data"]["base_path"]
    dev_data_path = config["split_data"]["dev_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]

    #define the traning meta dict
    traning_meta = config["training"]
    artifact_dir = traning_meta["artifact_dir"]

    # define the logistic regression model params
    penalty = traning_meta["estimators"]["LR"]["params"]["penalty"]
    inv_regularize = traning_meta["estimators"]["LR"]["params"]["inv_regularize"]
    solver = traning_meta["estimators"]["LR"]["params"]["solver"]
    max_iter = traning_meta["estimators"]["LR"]["params"]["max_iter"]

    target = config["base"]["target_col"]

    # load the train and dev dataframes
    train_df = pd.read_csv(os.path.join(base_split_dir, train_data_path), 
                        sep=",", 
                        index_col=0)
    dev_df = pd.read_csv(os.path.join(base_split_dir, dev_data_path), 
                       sep=",", 
                       index_col=0)


    train_y = train_df[target]
    dev_y = dev_df[target]

    train_x = train_df.drop(target, axis=1)
    dev_x = dev_df.drop(target, axis=1)

    lr = LogisticRegression(
        penalty=penalty,
        C=inv_regularize,
        solver=solver,
        max_iter=max_iter,
        random_state=random_state)
    
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(dev_x)
    
    precision, recall, f1_score, accuracy = eval_metrics(dev_y, predicted_qualities)

    print("Logistic Regression model (penalty=%s, C=%f, Solver=%s, max_iter=%f):" % (penalty, inv_regularize, solver, max_iter))
    print("  Precision: %s" % precision)
    print("  Recall: %s" % recall)
    print("  F1 Score: %s" % f1_score)
    print("  Accuracy: %s" % accuracy)

#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "accuracy": accuracy
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        params = {
            "penalty": penalty,
            "c": inv_regularize,
            "solver": solver,
            "max_iter": max_iter
        }
        json.dump(params, f, indent=4)
#####################################################

    # save the model
    os.makedirs(artifact_dir, exist_ok=True)
    model_path = os.path.join(artifact_dir, "model.joblib")

    joblib.dump(lr, model_path)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config) 