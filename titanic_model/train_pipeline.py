import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
import joblib

from pipeline import titanic_pipe, save_pipeline
from titanic_model.config import config
from titanic_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Train the model."""

    # read training data
    data = pd.read_csv(config.CLEANED_DATA)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.TARGET, axis=1),
        data[config.TARGET],
        test_size=0.2,
        random_state=config.SEED)  # we are setting the seed here

    # Fit ML pipeline
    titanic_pipe.fit(X_train, y_train)

    # save pipeline
    save_pipeline(pipeline_to_persist=titanic_pipe)


if __name__ == '__main__':
    run_training()
