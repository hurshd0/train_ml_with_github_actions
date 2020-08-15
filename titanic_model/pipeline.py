from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from processing import preprocessors as pp
from config import config


titanic_pipe = Pipeline(

    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
        ('missing_indicator',
            pp.MissingIndicator(variables=config.NUMERICAL_VARS)),
        ('numerical_imputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
        ('cabin_letter_exctractor',
            pp.ExtractFirstLetter(variables=config.CABIN)),
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.05,
                variables=config.CATEGORICAL_VARS)),
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
        ('scaler',
            StandardScaler()),
        ('Linear_model', LogisticRegression(
            C=config.REG_PARAM, random_state=config.SEED))
    ]

)
