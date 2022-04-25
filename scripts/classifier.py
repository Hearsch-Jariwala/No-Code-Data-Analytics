# classifier.py
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


def get_classifier(clf_name, params):
    clf = None
    if clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors = params['K'])
    elif clf_name == 'SVM':
        clf = SVC(C = params['C'])
    else:
        clf = RandomForestClassifier(max_depth = params['max_depth'], n_estimators = params['n_estimators'], random_state = 1234)
    return clf