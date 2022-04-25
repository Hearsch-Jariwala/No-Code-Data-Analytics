# parameter.py
import streamlit as st


def add_parameter_ui(clf_name):
    params = dict()

    if clf_name == 'KNN':
        K = st.sidebar.slider('K',1,15)
        params['K'] = K
    elif clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params