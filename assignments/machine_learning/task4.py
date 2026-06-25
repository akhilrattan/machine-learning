import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import (
    DecisionTreeClassifier,
    plot_tree
)

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv("Social_Network_Ads.csv")

print(df.info())

for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].mean())
for col in df.select_dtypes(include = "object").columns:
    df[col].fillna(df[col].mode()[0])

le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

X = df[['Gender','Age','EstimatedSalary']]
y = df['Purchased']

X_train,X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
depths = [3,5,10,None]
accuracies = []
models = []

for depth in depths:
    model = DecisionTreeClassifier(
        max_depth = depth,
        random_state= 42
    )
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test,y_pred)

    accuracies.append(accuracy)
    models.append(model)

    print(f"Depth = {depth}, Accuracy = {accuracy:.4f}")

best_index = np.argmax(accuracies)
best_model = models[best_index]
best_depth = depths[best_index]

print("\nBest Tree Depth:", best_depth)
print("Best Accuracy:", accuracies[best_index])

best_predictions = best_model.predict(X_test)

cm = confusion_matrix(y_test,best_predictions)
print("\nConfusion Matrix:")
print(cm)

print("classification report")
print(classification_report(y_test,best_predictions))

plt.figure(figsize=(15,8))
plot_tree(
     best_model,
     feature_names=X.columns,
     class_names=['Not Purchased', 'Purchased'],
     filled=True,
     rounded=True
)
plt.title(f"Decision Tree (Max Depth = {best_depth})")
plt.show()

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance':best_model.feature_importances_
})
feature_importance = feature_importance.sort(
    by = 'Importance',
    ascending = False
)

print("\nFeature Importance:")
print(feature_importance)


plt.figure(figsize=(8, 5))

plt.bar(
    feature_importance['Feature'],
    feature_importance['Importance']
)

plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.title("Feature Importance in Decision Tree")

plt.grid(True)

plt.show()
