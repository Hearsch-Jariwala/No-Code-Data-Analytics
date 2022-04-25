import streamlit as st

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.decomposition import PCA
from scripts.data import get_dataset
from scripts.parameter import add_parameter_ui
from scripts.classifier import get_classifier


def run():
    st.title("Exploratory data analysis of different datasets")

    st.write("""
    # Explore different classifiers
    which one is the best
    """)

    dataset_name = st.sidebar.selectbox("Select Dataset",("Iris", "Breast Cancer", "Wine dataset"))
    classifier_name = st.sidebar.selectbox("Select Classifier",("KNN", "SVM", "Random Forest"))


    #st.write(dataset_name)


    X, y = get_dataset(dataset_name)
    st.write('Shape of the dataset: ', X.shape)
    st.write('Number of classes: ', len(np.unique(y)))

    params = add_parameter_ui(classifier_name)
    clf = get_classifier(classifier_name, params)


    # Classification
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=1234)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    st.write(f'Classifier: {classifier_name}' )
    st.write(f'Accuracy: {acc}')

    # Plot dataset
    # Project the data onto the 2 primary principal components
    pca = PCA(2)
    X_projected = pca.fit_transform(X)

    x1 = X_projected[:,0]
    x2 = X_projected[:,1]

    fig = plt.figure()
    plt.scatter(x1, x2, c=y, alpha =0.8, cmap = 'viridis')

    plt.xlabel('Principal component 1')
    plt.ylabel('principal component 2')
    plt.colorbar()

    #plt.show()
    st.pyplot(fig)


if __name__ == "__main__":
    run()
