# data.py
from sklearn import datasets


def get_dataset(name):
    data = None

    if name == 'Iris':
        data = datasets.load_iris()
    elif name == 'Wine':
        data = datasets.load_wine()
    else:
        data = datasets.load_breast_cancer()

    X = data.data
    y = data.target
    return X, y