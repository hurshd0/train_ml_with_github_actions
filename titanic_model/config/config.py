import pathlib


# ==================   PATHS ================== #

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FOLDER = PACKAGE_ROOT / "data"
RAW_DATA = DATA_FOLDER / "raw_titanic.csv"
CLEANED_DATA = DATA_FOLDER / "cleaned_titanic.csv"
ML_ARTIFACTS_FOLDER = PACKAGE_ROOT / "trained_model_artifacts"
PIPELINE_NAME = "logistic_regression"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"

# ================== ML PARAMS ================ #
SEED = 42
REG_PARAM = 0.0005

# =============== FEATURE GROUPS =============== #

TARGET = "survived"

CATEGORICAL_VARS = ['sex', 'cabin', 'embarked', 'title']

NUMERICAL_VARS = ['age', 'fare']

CABIN = 'cabin'
