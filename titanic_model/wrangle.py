import re
import pandas as pd
import numpy as np
from config import config

import logging

_logger = logging.getLogger(__name__)

def get_first_cabin(row):
    try:
        return row.split()[0]
    except:
        return np.nan


def get_title(passenger):
    line = passenger
    if re.search('Mrs', line):
        return 'Mrs'
    elif re.search('Mr', line):
        return 'Mr'
    elif re.search('Miss', line):
        return 'Miss'
    elif re.search('Master', line):
        return 'Master'
    else:
        return 'Other'


if __name__ == "__main__":
    _logger.info("**Loading raw titanic dataset")
    data = pd.read_csv(config.RAW_DATA)
    _logger.info("**Started data wrangling")
    data = data.replace('?', np.nan)
    data['cabin'] = data['cabin'].apply(get_first_cabin)
    data['title'] = data['name'].apply(get_title)
    data['fare'] = data['fare'].astype('float')
    data['age'] = data['age'].astype('float')
    data.drop(labels=['name', 'ticket', 'boat', 'body',
                      'home.dest'], axis=1, inplace=True)
    _logger.info("**Completed data wrangling")
    data.to_csv(config.CLEANED_DATA, index=False)
    _logger.info("**Saving cleaned titanic dataset")