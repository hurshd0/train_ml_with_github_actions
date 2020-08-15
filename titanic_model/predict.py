import pandas as pd

import joblib
from config import config


def make_prediction(input_data):
    """
    Loads pipeline and makes predictions
    """
    _titanic_pipe = joblib.load(filename=config.PIPELINE_NAME)
    results = _titanic_pipe.predict(input_data)
    return results


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function plots the confusion matrix and saves it to artifact folder.
    Normalization can be applied by setting `normalize=True`.

    Credit: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        file_name = "normalized_confusion_matrix.png"
    else:
        file_name = "unormalized_confusion_matrix.png"

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(".png", dpi=120)


if __name__ == '__main__':

    # test pipeline
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    data = pd.read_csv(config.CLEANED_DATA)

    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(config.TARGET, axis=1),
        data[config.TARGET],
        test_size=0.2,
        random_state=config.SEED)

    pred = make_prediction(X_test)

    # report metrics

    # determine the accuracy
    print('test accuracy: {}'.format(accuracy_score(y_test, pred)))
    print()
