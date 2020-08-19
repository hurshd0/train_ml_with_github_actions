## Demo showcasing simple MLOps workflow

### Follow below instructions to try out 👇

1. Fork this repo 🍴
![](https://i.imgur.com/3fjO1eA.png)
2. Checkout a branch and test out a different ML model via `git checkout -b random_forest` 
3. Add ML classifier of your choice to `titanic_model/pipeline.py`
![](https://i.imgur.com/jiDyhmW.png)
4. Create a Pull Request to master
![](https://i.imgur.com/yhUaqXu.png)
5. Go get a sip of ☕ while your model trains
Once traininig is completed it should look like this
![](https://i.imgur.com/4NWGQXp.gif)

### To run it locally follow below instructions

#### Pre-requisites

- Python 3
- Conda [Optional, but recommended]

1. If you have conda, than install `pipenv` via `conda install pipenv`, if you don't just do `pip install pipenv`
2. To install dependencies do `pipenv install`
3. To activate virtual environment do `pipenv shell`
4. Run Jupyter Notebook by `jupyter notebook` command
5. Run `tox` to train ML model and generate reports, and pickled model saved in `titanic_model/trained_model_artifacts`

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
