import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scikitplot as skplt
import itertools

from titanic_model.config import config
from titanic_model import __version__ as _version
from pipeline import load_pipeline

import logging
import typing as t

_logger = logging.getLogger(__name__)

pipeline_file_name = f"{config.PIPELINE_SAVE_FILE}{_version}.pkl"
_titanic_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
    """
    Makes prediction
    """
    results = _titanic_pipe.predict(input_data)
    return results


if __name__ == '__main__':

    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix

    data = pd.read_csv(config.CLEANED_DATA)

    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.TARGET, axis=1),
        data[config.TARGET],
        test_size=0.2,
        random_state=config.SEED)

    y_test_pred = make_prediction(input_data=X_test)
    y_train_pred = make_prediction(input_data=X_train)

    # report metrics
    # a) confusion matrix
    cm = confusion_matrix(y_test, y_test_pred)
    skplt.metrics.plot_confusion_matrix(y_test, y_test_pred)
    plt.savefig(config.TRAINED_MODEL_DIR /
                f"confustion_matrix_v{_version}.png")
    skplt.metrics.plot_confusion_matrix(y_test, y_test_pred, normalize=True)
    plt.savefig(config.TRAINED_MODEL_DIR /
                f"normalized_confustion_matrix_v{_version}.png")

    # b) accuracy score
    acs_test = accuracy_score(y_test, y_test_pred)
    acs_test_out = f"Test accuracy score: {acs_test}"
    acs_train = accuracy_score(y_train, y_train_pred)
    acs_train_out = f"Training accuracy score: {acs_train}"

    _logger.info(acs_train_out)
    _logger.info(acs_test_out)

    with open(config.TRAINED_MODEL_DIR / f"metrics_{_version}.txt", "w") as fobj:
        fobj.write(acs_train_out)
        fobj.write("\n")
        fobj.write(acs_test_out)
