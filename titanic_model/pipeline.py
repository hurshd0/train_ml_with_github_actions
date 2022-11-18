from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

from titanic_model.processing import preprocessors as pp
from titanic_model.config import config
from titanic_model import __version__ as _version

from titanic_model import logger
import typing as t



titanic_pipe = Pipeline(

    [
        ('categorical_imputer',
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS)),
        ('missing_indicator',
            pp.MissingIndicator(variables=config.NUMERICAL_VARS)),
        ('numerical_imputer',
            pp.NumericalImputer(variables=config.NUMERICAL_VARS)),
        ('rare_label_encoder',
            pp.RareLabelCategoricalEncoder(
                tol=0.05,
                variables=config.CATEGORICAL_VARS)),
        ('categorical_encoder',
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS)),
        ('scaler',
            StandardScaler()),
        ('random_forest_classifier', RandomForestClassifier(random_state=config.SEED))
    ]

)


def save_pipeline(*, pipeline_to_persist) -> None:
    """Saves the pipeline"""
    file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
    save_path = config.TRAINED_MODEL_DIR / file_name
    joblib.dump(pipeline_to_persist, save_path)
    logger.info(f"**Saved pipeline at: {file_name}")


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted pipeline"""
    file_path = config.TRAINED_MODEL_DIR / file_name
    logger.info(f"**Loading pipeline from: {file_name}")
    trained_model = joblib.load(filename=file_path)
    return trained_model
