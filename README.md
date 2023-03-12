MLOps-Pipeline
==============================

a end to end mlops pipeline integrate tools for data lineage,experiment tracking,model registry,data drift,tfx

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    |
    ├── prediction_service <- folder initialize the prediction functions .
    │   └── model          <- best trained model
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── prediction.py  <- prediction python moddule
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures             <- Generated graphics and figures to be used in reporting
    │   └── metrics             <- Generated metrics for paramters & scores for model traning
    │       ├── params.json     <- keep track of traning model configuration params
    │       ├── scores.json     <- keep track of traning results 
    │
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
    │                               generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                     <- Source code for use in this project.
    │   ├── __init__.py         <- Makes src a Python module
    │   ├── pipeline_01_data_preperation.py         <- raw data preperation modeule
    │   ├── pipeline_02_data_preprocessing.py       <- data preprocessing module
    │   ├── pipeline_03_data_split.py               <- split data into train/dev
    │   ├── pipeline_04_model_train.py              <- model traning
    │   ├── utils.py                                <- util functions
    │   │
    │   ├── data                <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features            <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models              <- Scripts to train models and then use trained models to make
    │   │   │                       predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization       <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── webapp                  <- web application folder.
    │   │
    │   ├── static              <- css and js script foler
    │   │   └── css
    │   │   └── script
    │   │
    │   ├── templates           <- Scripts for web page rendering
    │   │   └── 404.html
    │   │   └── base.html
    │   │   └── index.heml
    │
    |── tox.ini                 <- tox file with settings for running tox; see tox.readthedocs.io
    ├── appp.py                 <- flask web application.
    ├── Procfile                <- Heroku trigger point.
    ├── params.yaml             <- define configurations and dvc params.
    ├── dvc.yaml                <- dvc dag configuration file.



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Follow the project wiki to build and test this repo
------------








