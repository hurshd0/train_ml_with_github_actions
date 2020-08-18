### Demo showcasing how to automate your training ML models on Github actions and use DVC for data versioning

### USAGE

#### Pre-requisites

- Python 3
- Conda [Optional]

#### Project structure
```
.
├── notebooks
└── titanic_model
    ├── config
    ├── processing
    └── trained_model_artifacts

5 directories
```
#### Instructions
1. If you have conda, than install `pipenv` via `conda install pipenv`, if you don't just do `pip install pipenv`
2. To install dependencies do `pipenv install`
3. To activate virtual environment do `pipenv shell`
4. Run Jupyter Notebook by `jupyter notebook` command
5. Run `tox` to train ML model and generated reports and pipeline is saved in `titanic_model/trained_model_artifacts`


