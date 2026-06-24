import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("Housing.csv")

print("\ndisplaying first 10 rows")
print(df.head(10))

print("\nprinting the information of data")
print(df.info())

print("missing values before processing : ")
print(df.isnull().sum())

for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].mean())

for col in df.select_dtypes(include="object").columns:
    df[col].fillna(df[col].mode()[0])

le = LabelEncoder()

for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

print("\nMissing Values After Processing:")
print(df.isnull().sum())

y = df["price"]
X = df.drop("price", axis= 1)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"mae : {mae:.2f}")
print(f"mse : {mse:.2f}")
print(f"rmse : {rmse:.2f}")
print(f"r2 score : {r2:.2f}")


plt.figure(figsize=(6,5))
plt.scatter(
    y_test,
    y_pred,
    alpha= 0.6
)
plt.plot(
    [y_test.min(),y_test.max()],
    [y_test.min(),y_test.max()],
    color = "red",
    linewidth = 2,
    label = "predicted prices",
)
plt.xlabel("actual prices")
plt.ylabel("predictied prices")
plt.title("actual vs predicted prices")
plt.legend()
plt.grid(True)
plt.show()