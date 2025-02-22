# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12erf_6K_vL3wNdg7zvLXVeiGQWpG_gY2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate Gaussian Naïve Bayes without scaling
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred_unscaled = gnb.predict(X_test)

# Accuracy, Confusion Matrix, and Classification Report for unscaled data
print("Without Feature Scaling:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_unscaled):.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_unscaled))
print("Classification Report:\n", classification_report(y_test, y_pred_unscaled))

# Standardize features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and evaluate Gaussian Naïve Bayes with scaled features
gnb_scaled = GaussianNB()
gnb_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = gnb_scaled.predict(X_test_scaled)

# Accuracy, Confusion Matrix, and Classification Report for scaled data
print("\nWith Feature Scaling:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_scaled):.2f}")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_scaled))
print("Classification Report:\n", classification_report(y_test, y_pred_scaled))

# Compare Accuracy
plt.bar(["Unscaled", "Scaled"], [accuracy_score(y_test, y_pred_unscaled), accuracy_score(y_test, y_pred_scaled)], color=['blue', 'green'])
plt.xlabel("Feature Scaling")
plt.ylabel("Accuracy")
plt.title("Impact of Feature Scaling on Naïve Bayes")
plt.ylim(0, 1)
plt.show()