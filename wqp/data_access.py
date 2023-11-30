from sklearn.model_selection import train_test_split
import pandas as pd


def fetch_csv_data(url, separator):

    try:
        if separator:
            return pd.read_csv(url, sep=separator)
        else:
            return pd.read_csv(url)
    except Exception as e:
        raise Exception(f'Error while fetching data at url {url}: {e}')


def build_train_test_sets(data, label_col, train_size):
   
    try:
        X = data.drop(label_col, axis=1)
        y = data[label_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size)

        return dict(train=(X_train, y_train), test=(X_test, y_test))
    
    except Exception as e:
        raise Exception(f'Error while splitting data: {e}')