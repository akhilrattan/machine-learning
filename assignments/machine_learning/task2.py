import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

data = load_breast_cancer()

X = data.data
y = data.target

print(X.shape)
print(data.feature_names)
print(data.target_names)

scaler = StandardScaler()

X_scaler = scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(
    X_scaler,
    y,
    test_size=0.20,
    random_state = 42
)

model = LogisticRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

print("confusion matrix : ", cm)

accuracy = accuracy_score(y_test , y_pred)
precision = precision_score(y_test , y_pred)
recall = recall_score(y_test , y_pred)
f1score = f1_score(y_test , y_pred)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1score:.4f}")

print(classification_report(
    y_test,
    y_pred
))

plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=data.target_names,
    yticklabels=data.target_names
)
plt.xlabel("predicted")
plt.ylabel("actual")
plt.title("confusion matrix")
plt.show()